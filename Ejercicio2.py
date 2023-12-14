def ficheroPrinter (number):
    """Función que pide un número entero entre 1 y 10 y lea 
        el fichero con el nombre tabla-n.txt con la tabla de
        multiplicar de ese número, donde n es el número 
        introducido, y la muestre por pantalla.
    
    Parámetro: 
            - number: Número entero entre 1 y 10.

    Salida: 
            - Lee el fichero con nombre tabla-n.txt con la 
            tabla de multiplicar de ese número, donde n es 
            el número introducido, y la muestre por pantalla.
    
    """

    import os   #Importo la libreria.
    if number in range (1,11):
        if os.path.exists(f'tabla-{number}.txt'):  
        #Le pregunto a la libreria si existe el archivo.

            file = open(f'tabla-{number}.txt', 'r')

            print(file.read())

            return file.read()
    
        else:
            print('El fichero no existe.')
    else:
        print('Su número entero no se encuentra entre 1 y 10')