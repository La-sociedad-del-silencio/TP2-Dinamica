from random import randint
import time

from algoritmo import eliminar_enemigos

import matplotlib.pyplot as plt

def generarAtaques(n: int):
    """ 
    Genera la cantidad deseada de ataques de la forma (n, [x_i], [f_i])
    utilizando números positivos aleatorios.
    """
    rafagas = [] 
    cargaAtaque = []
    for i in range(n):
        x_i = randint(1, 1000) 
        rafagas.append(x_i)
        f_i = randint(1, 3000) 
        cargaAtaque.append(f_i)

    cargaAtaque.sort()

    secuencia = (n, rafagas, cargaAtaque)

    return secuencia

        
def correrTest(cantidad):
    """ 
    Genera batallas y ejecuta el algoritmo greedy sobre las mismas.
    Devuelve el tiempo de ejecución en milisegundos
    """
    n, x, f = generarAtaques(cantidad)
    inicio = time.time()
    # A priori solo nos interesa el tiempo en esta seccion 
    cantidad_enemigos, secuencia = eliminar_enemigos(n, x, f)
    fin = time.time()

    msQueLlevo = int((fin - inicio) * 1000)

    return msQueLlevo


def generarEjemplos(cantidadElementos):
    """ Ejecuta tests de volumen """

    milisegs = [[]] * len(cantidadElementos)

    cantidadDeCorridas = 1
    
    for i in range(cantidadDeCorridas):
        for j in range(len(cantidadElementos)):
            msQueLlevo = correrTest(cantidadElementos[j])
            tmp = milisegs[j].copy()
            tmp.append(msQueLlevo)
            milisegs[j] = tmp

    milisegsPromedio = [0.0] * len(cantidadElementos)
    for i in range(len(cantidadElementos)):
        milisegsPromedio[i] = sum(milisegs[i]) / cantidadDeCorridas
                

    return cantidadElementos, milisegsPromedio

def generarGrafico():
    '''
    Genera un gráfico de cantidadBatallas-tiempoEjecución.
    WARNING ESTO TARDA ~5mins
    '''
    # Arrancamos con la misma cantidad que la catedra
    cantidadElementos = []
    maxNum = 100000
    # maxNum = 10000
    tasa = maxNum / 100
    # tasa = 10000000
    for i in range(maxNum):
        skip = randint(1,maxNum)
        if skip > tasa:
            continue
        cantidadElementos.append(i)

    cantidadElementos, milisegs = generarEjemplos(cantidadElementos)
    print(cantidadElementos)
    print(milisegs)

    # Lo hago string para que quede parejito uno al lado del otro
    cantidadElementosString = []
    for cantidad in cantidadElementos:
        cantidadElementosString.append(str(cantidad))

    plt.plot(cantidadElementos, milisegs, 'o', color='red')

    plt.ylabel('Tiempo en mili-segundos')
    plt.xlabel('Cantidad de batallas')

    plt.savefig('images/miliSegsFuncCantidadNativo.png', format="png")
    plt.show()

generarGrafico()
