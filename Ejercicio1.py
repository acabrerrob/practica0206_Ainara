# Escribir una función que pida un número entero entre 1 y 10 y
# guarde en un fichero con el nombre tabla-n.txt la tabla de 
# multiplicar de ese número, donde n es el número introducido.
def newFicheroMult ():
    number = int(input('introduzca un numero'))
    file = open(f'tabla-{number}.txt','w')
    for n in range (0,11):
        value = n * number
        file.write(f'\n{n} * {number} = {value}')
    return 

newFicheroMult()
