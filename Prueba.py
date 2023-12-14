def ficheroPrinter ():
    """Función que pide un número entero entre 1 y 10 y lea 
        el fichero con el nombre tabla-n.txt con la tabla de
        multiplicar de ese número, donde n es el número 
        introducido, y la muestre por pantalla.
    
    Parámetro: 

    
    Salida: 
    
    """

    import os
    number = int(input('Introduzca un número entre 1 y 10: '))
    fileName = f'tabla-{number}.txt'
    
    
    if os.path.exists(f'tabla-{number}.txt'):
        file = open(fileName, 'r')
        print(file.read())

        return file.read()
    
    else:
        print('El fichero no existe.')
    
ficheroPrinter()