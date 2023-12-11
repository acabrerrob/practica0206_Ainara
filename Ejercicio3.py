# Escribir una función que pida dos números n y m entre 1 y 10,
# lea el fichero tabla-n.txt con la tabla de multiplicar de ese
# número, y muestre por pantalla la línea m del fichero. Si el
# fichero no existe debe mostrar un mensaje por pantalla informando de ello.
def lineaFichero ():

    n = int(input('Introduzca un número entre 1 y 10: '))
    m = int(input('Introduzca un número entre 1 y 10: '))

    file = open(f'tabla-{n}.txt', 'r')
    print(file.read(m))
    return
lineaFichero()