CARGAR = "Cargar"
ATACAR = "Atacar"

def eliminar_enemigos(n,x, f):
    enemigos_eliminados = [0] * (n + 1)
    
    for minuto_actual in range(1, n + 1):
        max_enemigos_eliminables = min(f[0], x[minuto_actual-1]) 
        for minutos_desde_ultimo_ataque in range(0, minuto_actual):
            enemigos_actuales = min(f[minutos_desde_ultimo_ataque], x[minuto_actual-1]) 
            enemigos_ataque_anterior = enemigos_eliminados[minuto_actual-minutos_desde_ultimo_ataque-1]

            if enemigos_ataque_anterior + enemigos_actuales > max_enemigos_eliminables:
                max_enemigos_eliminables = enemigos_ataque_anterior + enemigos_actuales
                        
        enemigos_eliminados[minuto_actual] = max_enemigos_eliminables
            
    max_enemigos = enemigos_eliminados[-1]
    secuencia = obtener_secuencia_estrategias(x, f, enemigos_eliminados, n)
    #secuencia = obtener_secuencia_estrategias_recur(x, f, enemigos_eliminados, n, n-1, [])
    secuencia.reverse()
    return (max_enemigos, secuencia)

def obtener_secuencia_estrategias(x, f, enemigos_eliminados, minuto_actual):
    secuencia = []
    while minuto_actual > 0:
        minutos_desde_ultimo_ataque = minuto_actual-1
        
        while True:
            
            enemigos_ataque_anterior = enemigos_eliminados[minuto_actual-minutos_desde_ultimo_ataque-1]
            enemigos_actuales = min(f[minutos_desde_ultimo_ataque], x[minuto_actual-1])  

            if enemigos_ataque_anterior + enemigos_actuales == enemigos_eliminados[minuto_actual]:

                secuencia.append(ATACAR)
                minuto_actual = minuto_actual-minutos_desde_ultimo_ataque-1
                 
                secuencia.extend([CARGAR]*minutos_desde_ultimo_ataque) 
                
                break
        
            minutos_desde_ultimo_ataque -= 1
    return secuencia

def es_secuencia_correcta(x, f, cantidad_enemigos, secuencia):
    minutos_desde_ultimo_ataque = 0
    tropas_eliminadas = 0
    for minuto_actual, estrategia in enumerate(secuencia):
        
        if estrategia == 'Atacar':
           
            tropas_eliminadas += min(x[minuto_actual], f[minutos_desde_ultimo_ataque])
            minutos_desde_ultimo_ataque = 0
        else:
            minutos_desde_ultimo_ataque += 1    
    return tropas_eliminadas == cantidad_enemigos

# NO USARLA
def obtener_secuencia_estrategias_recur(x, f, enemigos_eliminados, minuto_actual, minutos_desde_ultimo_ataque, secuencia:list):
    if minuto_actual == 0:
        return secuencia
        
    enemigos_ataque_anterior = enemigos_eliminados[minuto_actual-minutos_desde_ultimo_ataque-1]
    enemigos_actuales = min(f[minutos_desde_ultimo_ataque], x[minuto_actual-1]) 
    
    if enemigos_ataque_anterior + enemigos_actuales == enemigos_eliminados[minuto_actual]:
        secuencia.append(ATACAR)
        minuto_actual = minuto_actual-minutos_desde_ultimo_ataque-1
        
        secuencia.extend([CARGAR]*minutos_desde_ultimo_ataque) 
        
        return obtener_secuencia_estrategias_recur(x, f, enemigos_eliminados, minuto_actual, minuto_actual-1, secuencia)
    
    return obtener_secuencia_estrategias_recur(x, f, enemigos_eliminados, minuto_actual, minutos_desde_ultimo_ataque-1, secuencia)

        
    
