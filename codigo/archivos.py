import time
from algoritmo_cambio import eliminar_enemigos

def generarTestDe(archivo):
    x = []
    f = []
    with open(archivo, "r") as file:
        n = None
        elem_actual = 1
        for i, line in enumerate(file):
            line = line.strip()
            if line.startswith("#"):
                continue
            if not n:
                n = int(line)
                continue
            if elem_actual <= n:
                x.append(int(line))
                elem_actual += 1
            else:
                f.append(int(line))

    return n, x, f 

def procesar_archivo(argv):

    archivoAProcesar = argv[1]
    
    n, x, f = generarTestDe(archivoAProcesar)

    inicio = time.time()

    cantidad_enemigos, secuencia = eliminar_enemigos(n, x, f)

    fin = time.time()

    tiempoQueLlevo = int((fin - inicio) * 1000)

    # Seccion de stdout: TO-DO        
        
        