CARGAR = "Cargar"
ATACAR = "Atacar"

def eliminar_enemigos(n,x, f):
    enemigos_eliminados = [0] * (n + 1)
    
    for minuto_actual in range(1, n + 1):
        max_enemigos_eliminables = min(f[0], x[minuto_actual-1]) 
        for minutos_desde_ultimo_ataque in range(minuto_actual):
            enemigos_actuales = min(f[minutos_desde_ultimo_ataque], x[minuto_actual-1]) 
            offset = minuto_actual-minutos_desde_ultimo_ataque-1
            enemigos_ataque_anterior = enemigos_eliminados[offset]

            if enemigos_ataque_anterior + enemigos_actuales > max_enemigos_eliminables:
                max_enemigos_eliminables = enemigos_ataque_anterior + enemigos_actuales
                        
        enemigos_eliminados[minuto_actual] = max_enemigos_eliminables
            
    max_enemigos = enemigos_eliminados[-1]
    secuencia = obtener_secuencia_estrategias(x, f, enemigos_eliminados, n)
    secuencia.reverse()
    return (max_enemigos, secuencia)

def obtener_secuencia_estrategias(x, f, enemigos_eliminados, minuto_actual):
    secuencia = []
    while minuto_actual > 0:
        
        secuencia.append(ATACAR)
        
        for minutos_desde_ultimo_ataque in range(minuto_actual):
            
            offsetMins = minuto_actual-minutos_desde_ultimo_ataque-1
            enemigos_ataque_anterior = enemigos_eliminados[offsetMins]

            cantReales = min(f[minutos_desde_ultimo_ataque], x[minuto_actual-1])  
            enemigos_actuales = cantReales

            enemigosDerrotados = enemigos_ataque_anterior + enemigos_actuales 
            esIgual = enemigosDerrotados == enemigos_eliminados[minuto_actual]
            if esIgual:
                minuto_actual = minuto_actual-minutos_desde_ultimo_ataque-1
                break
            else:
                secuencia.append(CARGAR)
        
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
