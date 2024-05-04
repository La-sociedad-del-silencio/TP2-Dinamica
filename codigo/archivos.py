import time
from algoritmo import eliminar_enemigos
FLAGMOSTRARSECUENCIA = "--mostrarSecuencia"

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
      
    # Seccion de stdout
    if len(argv) > 2 and argv[2] == FLAGMOSTRARSECUENCIA:
        ataqueIndice = 1
        for estrategia in secuencia:
            print(f"Decisión tomada en el ataque enemigo número {ataqueIndice}: {estrategia}")
            ataqueIndice += 1 
    print(f"La cantidad de enemigos derrotados fue: {cantidad_enemigos}")
    print(f"Tiempo total: {tiempoQueLlevo} mili segundos")    
        