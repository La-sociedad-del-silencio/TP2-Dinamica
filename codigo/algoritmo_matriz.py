CARGAR = "Cargar"
ATACAR = "Atacar"

def eliminar_enemigos(x, f):
    n = len(x)
    enemigos_eliminados = [[0] * (n + 1) for _ in range(n + 1)]
    
    for minuto_actual in range(1, n + 1):
        for minutos_desde_ultimo_ataque in range(1, n + 1):
            
            if minuto_actual >= minutos_desde_ultimo_ataque:
                
                enemigos_ataque_anterior = enemigos_eliminados[minuto_actual-minutos_desde_ultimo_ataque][minuto_actual-minutos_desde_ultimo_ataque]
                enemigos_actuales = min(f[minutos_desde_ultimo_ataque-1], x[minuto_actual-1])  
                enemigos_atacar_antes = enemigos_eliminados[minuto_actual][minutos_desde_ultimo_ataque-1]
                
                enemigos_eliminados[minuto_actual][minutos_desde_ultimo_ataque] = max(enemigos_ataque_anterior +  enemigos_actuales, enemigos_atacar_antes)
            
    max_enemigos = enemigos_eliminados[-1][-1]
    secuencia = obtener_secuencia_estrategias(x, f, enemigos_eliminados, n, n, [])
    secuencia.reverse()
    return (max_enemigos, secuencia)

def obtener_secuencia_estrategias(x, f, enemigos_eliminados, minuto_actual, minutos_desde_ultimo_ataque, secuencia):
   
    if minuto_actual == 0 or minutos_desde_ultimo_ataque == 0:
        return secuencia
    
    enemigos_ataque_anterior = enemigos_eliminados[minuto_actual-minutos_desde_ultimo_ataque][minuto_actual-minutos_desde_ultimo_ataque] if minuto_actual >= minutos_desde_ultimo_ataque else 0
    enemigos_actuales = min(f[minutos_desde_ultimo_ataque-1], x[minuto_actual-1])  
    enemigos_atacar_antes = enemigos_eliminados[minuto_actual][minutos_desde_ultimo_ataque-1]
    
    if enemigos_ataque_anterior + enemigos_actuales >= enemigos_atacar_antes:
        secuencia.append(ATACAR)
        i = minutos_desde_ultimo_ataque
        while i > 1:
            secuencia.append(CARGAR)
            i -= 1
        return obtener_secuencia_estrategias(x, f, enemigos_eliminados, minuto_actual-minutos_desde_ultimo_ataque, minuto_actual-minutos_desde_ultimo_ataque, secuencia)
    return obtener_secuencia_estrategias(x, f, enemigos_eliminados, minuto_actual, minutos_desde_ultimo_ataque-1, secuencia)
    