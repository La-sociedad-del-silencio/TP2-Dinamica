import time
from algoritmo_cambio import eliminar_enemigos

def generarTestDe(archivo):
    x = []
    f = []
    with open(archivo, "r") as file:
        next(file)
        n = int(next(file))
        elem_actual = 1
        for line in file:
            if elem_actual <= n:
                x.append(int(line.strip()))
                elem_actual += 1
            else:
                f.append(int(line.strip()))

    return n, x, f 

def procesar_archivo(argv):

    archivoAProcesar = argv[1]
    
    n, x, f = generarTestDe(archivoAProcesar)

    inicio = time.time()

    cantidad_enemigos, secuencia = eliminar_enemigos(n, x, f)

    fin = time.time()

    tiempoQueLlevo = int((fin - inicio) * 1000)

    # Seccion de stdout: TO-DO
    
        
        
        