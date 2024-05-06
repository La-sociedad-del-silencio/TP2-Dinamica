CARGAR = "Cargar"
ATACAR = "Atacar"

def esOptimizable(n, x, f):
    """ 
    Indica si, dado el conjunto de datos de entrada, se puede 
    utilizar la versión optimizada del algoritmo.
    Se debe cumplir que cada x_i sea menor que f[0] = f(1)
    """
    for minuto_actual in range(n):
        if x[minuto_actual] > f[0]:
            return False
    return True

def eliminar_enemigos_optimizado(n, x):
    """ 
    Devuelve el resultado del algoritmo si el mismo esOptimizable().
    Se eliminan todos los enemigos y se ataca en cada minuto.
    """
    enemigos_eliminados = x
    max_enemigos = sum(enemigos_eliminados)
    secuencia = [ATACAR] * n
    return (max_enemigos,secuencia)

def eliminar_enemigos(n,x,f):
    """ 
    Algoritmo de programación dinámica para determinar la cantidad máxima de
    enemigos que pueden ser derrotados. Utiliza obtener_secuencia_estrategias()
    para reconstruir las estrategias de ataque empleadas.
    
    Recibe: n >= 0 y las listas x y f, cuyo tamaño es n. f toma valores
    monótonos crecientes.
    Devuelve: cantidad de enemigos eliminados y secuencia de estrategias
    """
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
    """ 
    Reconstruye la secuencia de estrategias usada para eliminar la mayor cantidad de
    enemigos.
    Empieza por el último minuto de combate sabiendo que la estrategia es 'atacar'. 
    Comparando valores del arreglo de óptimos 'enemigos_eliminados', busca el minuto 
    en el que se realizó el ataque anterior. Mientras que no lo encuentra, la estrategia
    es 'cargar'. Repite hasta llegar al minuto 0.
    """
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
    """ 
    Recibe un conjunto de datos 'x' y 'f', y el resultado obtenido al aplicar el algoritmo
    de programación dinámica, 'cantidad_enemigos' y 'secuencia'.
    Comprueba que siguiendo la secuencia de estrategias recibida, se puedan eliminar
    'cantidad_enemigos'.
    """
    minutos_desde_ultimo_ataque = 0
    tropas_eliminadas = 0
    for minuto_actual, estrategia in enumerate(secuencia):
        
        if estrategia == ATACAR:
           
            tropas_eliminadas += min(x[minuto_actual], f[minutos_desde_ultimo_ataque])
            minutos_desde_ultimo_ataque = 0
        else:
            minutos_desde_ultimo_ataque += 1    
    return tropas_eliminadas == cantidad_enemigos
