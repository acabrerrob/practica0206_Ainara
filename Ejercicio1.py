def newFicheroMult (number):
    """Función que pide un número entero entre 1 y 10 y guarde 
    en un fichero con el nombre tabla-n.txt la tabla de
    multiplicar de ese número, donde n es el número introducido.
    
    Parámetro: 
            - number: Número entero entre 1 y 10.
    
    
    Salida: 
            - Crea un ficheron con el nombre tabla-n.txt la 
            tabla de emultiplicar de ese número, donde n es el
            número introducido.
    
    """
    if number in range(1,11):
    
        file = open(f'tabla-{number}.txt','w')

        for n in range (0,11):
                value = n * number
                file.write(f'\n{n} * {number} = {value}')
        return 
    
    else:
         print('Su número entero no se encuentra entre 1 y 10')