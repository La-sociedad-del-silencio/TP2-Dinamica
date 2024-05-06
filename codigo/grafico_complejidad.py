from random import randint
import time

from algoritmo import eliminar_enemigos

import matplotlib.pyplot as plt

def generarAtaques(n: int):
    """ 
    Genera un test de tamaño n, con datos aleatorios.
    """
    
    rafagas = [] 
    cargaAtaque = []
    for _ in range(n):
        x_i = randint(1, 1000) 
        rafagas.append(x_i)
        f_j = randint(1, 1000) if len(cargaAtaque) == 0 else randint(cargaAtaque[-1]+1, cargaAtaque[-1]+100)
        cargaAtaque.append(f_j)

    secuencia = (n, rafagas, cargaAtaque)

    return secuencia

        
def correrTest(cantidad):
    """ 
    Ejecuta un test de tamaño 'cantidad' y devuelve el tiempo de 
    ejecución en milisegundos.
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
    
    for j in range(len(cantidadElementos)):
        print(f"Iteracion {j}/{len(cantidadElementos)}")
        msQueLlevo = correrTest(cantidadElementos[j])
        milisegs[j] = msQueLlevo                

    return milisegs
    
def generarGraficoPrimeraVez():  
    """ 
    Ejecuta tests de volumen y genera un gráfico con los resultados.
    Guarda los resultados en un archivo.
    
    Utilizar si se quiere generar un nuevo conjunto de mediciones
    """
    # Arrancamos con la misma cantidad que la catedra: 5000
    cantidadElementos = []
    maxNum = 5000
    for i in range(0, maxNum+1, 10): 
        cantidadElementos.append(i)

    milisegs = generarEjemplos(cantidadElementos)
    print(cantidadElementos)
    print(milisegs)
    
    with open("ejemplos_adicionales/grafico_complejidad_datos.txt", "w") as file:
        file.write(f"{cantidadElementos}\n{milisegs}")

    generarGraficoAuxiliar(cantidadElementos, milisegs, False)

#generarGraficoPrimeraVez()

def generarGrafico():
    
    """ 
    Lee de un archivo los resultados de los tests de volumen realizados.
    Genera un gráfico y lo guarda.
    
    Se utiliza cuando se tienen las mediciones, pero se quiere hacer cambios al
    gráfico.
    """
    cantidadElementos = None
    milisegs = None
    
    with open("ejemplos_adicionales/grafico_complejidad_datos.txt", "r") as file:
        for i, line in enumerate(file):
            if i == 0:
                cantidadElementos = line.strip()[1:-1].split(', ')
            else:
                milisegs = line.strip()[1:-1].split(', ')
    for i in range(len(cantidadElementos)):
        cantidadElementos[i] = int(cantidadElementos[i])
        milisegs[i] = int(milisegs[i])
        
    print(milisegs[100])
    print(milisegs[200])
    print(milisegs[400])
        
    generarGraficoAuxiliar(cantidadElementos, milisegs, True)
   
def generarGraficoAuxiliar(cantidadElementos, milisegs, agregarTicks): 
    """ 
    Genera un gráfico que compara la cantidad de minutos de combate con el
    tiempo de ejecución del algoritmo en cada caso.
    """
    plt.plot(cantidadElementos, milisegs, 'o', color='red')

    plt.ylabel('Tiempo en mili-segundos')
    plt.xlabel('Cantidad de minutos del ataque')
    if agregarTicks:
        # cambiar según el tamaño del conjunto de datos y/o los tiempos de ejecución
        plt.xticks([500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000])
        plt.yticks([500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000])
    
    plt.savefig('images/graficoComplejidad.png', format="png")
    plt.show()
    
#generarGrafico()