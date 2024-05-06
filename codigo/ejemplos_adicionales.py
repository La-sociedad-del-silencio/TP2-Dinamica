from random import randint

def generar_ejemplo_x_menor_a_f0_volumen(n):
    """ 
    Genera un test de volumen para el caso de que cada x_i es menor que f[0]
    """
    
    x = []
    f = []
    
    for _ in range(n):
        x_i = randint(0, 100) 
        
        f_j = randint(100, 110) if len(f) == 0 else randint(f[-1]+1, f[-1]+10)
        x.append(x_i)
        f.append(f_j)
        
    return x, f

def escribir_ejemplo_en_archivo():
    """ 
    Genera un test de volumen para el caso de que cada x_i es menor que f[0],
    guarda los datos en un archivo y coloca el resultado esperado en 
    ejemplos_adicionales/Resultados_Esperados.txt.
    """
    
    x, f =  generar_ejemplo_x_menor_a_f0_volumen(100)
    with open("ejemplos_adicionales/x_menor_a_f0_volumen.txt", "w") as file:
        file.write("# Ejemplo de 100 elementos: todos los valores de x son menores o iguales a f[0]\n100\n")
        for i in range(100):
            file.write(f'{x[i]}\n')
        for i in range(100):
            file.write(f'{f[i]}\n')
    
    with open("ejemplos_adicionales/Resultados_Esperados.txt", "a") as file:
        estrategias = "Atacar, " * 100
        file.write(f"\nx_menor_a_f0_volumen.txt\nEstrategia: {estrategias[:-2]}\nCantidad de tropas eliminadas: {sum(x)}")      
            
            
#escribir_ejemplo_en_archivo()