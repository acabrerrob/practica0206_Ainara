# Escribir una función que pida un número entero entre 1 y 10,
# lea el fichero tabla-n.txt con la tabla de multiplicar de ese
# número, donde n es el número introducido, y la muestre por pantalla.
# Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.
def ficheroPrinter ():

    number = int(input('Introduzca un número entre 1 y 10: '))
    
    file = open(f'tabla-{number}.txt', 'r')
    
    print(file.read())

    return

ficheroPrinter()