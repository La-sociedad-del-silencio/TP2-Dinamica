from algoritmo import eliminar_enemigos, es_secuencia_correcta
from archivos import generarTestDe
import time

VERDE = '\033[92m'
ROJO  = '\033[91m'
FINCO = '\033[0m'

class Resultado:
    def __init__(self, obtenido, esperado, nombre_test, tiempo, datos):
        self.obtenido = obtenido

        self.esperado = esperado
        
        self.nombre_test = nombre_test            
        
        self.tiempo = tiempo
        self.datos = datos

    def __repr__(self) -> str:

        representacion = f"Test '{self.nombre_test}'" 
            
        representacion += "\n"
        representacion += "Tiempo total: " + str(self.tiempo) + " milisegundos"
        representacion += "\n"
        representacion += "Cantidad de tropas:\n" 
        representacion += "\tResultado esperado: " + str(self.esperado[0])
        representacion += "\n"
        representacion += "\tResultado obtenido: " + str(self.obtenido[0])
        representacion += "\n"
        coincide_tropas_eliminadas = self.obtenido[0] == self.esperado[0]
        secuencia_correcta = es_secuencia_correcta(self.datos[0], self.datos[1], self.obtenido[0], self.obtenido[1])
        rta_secuencia_correcta = "validada" if secuencia_correcta else ": es incorrecta"
        representacion += f"Generación de secuencia {rta_secuencia_correcta}" 
        representacion += "\n"
        # La cantidad de tropas eliminadas debe ser la misma, pero
        # la secuencia puede llegar a ser distinta a la de la cátedra
        # (nos dan todas iguales, excepto para el caso de 5000).
        # Por eso, usamos la función es_secuencia_correcta() que verifica que con la
        # secuencia obtenida se llegue a la misma cantidad de tropas eliminadas,
        # es decir, que la reconstrucción de la solución sea correcta.
        if coincide_tropas_eliminadas and secuencia_correcta:
            representacion += VERDE + "Resultado: :)" + FINCO
        else:
            representacion += ROJO + "Resultado: X" + FINCO
        representacion += "\n"

        return representacion

def generarRtasEsperadas(archivo):
    """ 
    Crea un diccionario con las respuestas esperadas para los ejemplos
    que figuran en el archivo. 
    """
    rtas = {}
    
    with open(archivo, "r") as f:
    
        nombre_archivo = None
        cantidad_tropas  = None
        estrategias = None
        
        for linea in f:
            linea = linea.strip()
            
            if linea.endswith('.txt'):
                nombre_archivo = linea
            elif linea.startswith('Cantidad de tropas eliminadas:'):
                cantidad_tropas = int(linea.split(': ')[1])
                rtas[nombre_archivo] = (cantidad_tropas, estrategias)
            elif linea.startswith('Estrategia: '):
                estrategias = linea.split(': ')[1].split(', ')
            
        rtas[nombre_archivo] = (cantidad_tropas, [estrategias])

    return rtas 

def generarResultados(carpeta):
    """ 
    Dado un directorio con ejemplos y las respuestas esperadas, ejecuta
    el programa en cada uno de ellos y devuelve una lista con los resultados.
    obtenidos.
    """
    archivo_rtas_esperadas = f"{carpeta}/Resultados_Esperados.txt"
    rtas = generarRtasEsperadas(archivo_rtas_esperadas)
    resultados = []
    for archivo, rtaEsperada in rtas.items():
        
        n, x, f = generarTestDe(carpeta + "/" + archivo)
        inicio = time.time()
        rta_obtenida = eliminar_enemigos(n, x, f)
        fin = time.time()
        tiempoQueLlevo = int((fin - inicio) * 1000)
        resultado = Resultado(rta_obtenida, rtaEsperada, archivo, tiempoQueLlevo, [x, f])

        resultados.append(str(resultado))

    return resultados

            


