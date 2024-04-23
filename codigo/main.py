from sys import argv
import time

from archivos import procesar_archivo
from pruebas import *

FLAGMOSTRARSECUENCIA = "--mostrarSecuencia"

def main():
    f'''
    INPUT (argv):
        - argv[1] = Nombre del archvio a procesar
        - argv[2] = Si argv[2] existe y se llama {FLAGMOSTRARSECUENCIA}
                    imprime las estrategias utilizadas 
    OUTPUT (stdout):
        - Cantidad de enemigos eliminados
        - El tiempo que llevo calcular todo
        - Opcional: estrategias
    '''
    
    if len(argv) > 1:
        procesar_archivo(argv) # To-Do  
        
    else:
        print("---Ejemplos de la cátedra---\n")
        archivo_rtas_esperadas = "ejemplos_catedra/Resultados_Esperados.txt"
        for resultado in generarResultados("ejemplos_catedra", generarRtasEsperadasCatedra(archivo_rtas_esperadas)):
            print(resultado)
        
        # To-Do   
        """ print("---Ejemplos adicionales---\n")
        for resultado in generarResultados("ejemplos_adicionales", generarRtasEsperadasEjAdicionales()):
            print(resultado) """


main()