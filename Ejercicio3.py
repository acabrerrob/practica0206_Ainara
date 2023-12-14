def lineaFichero (n,m):
    """Función que pide un dos números n y m entre 1 y 10,
        lea el fichero con el nombre tabla-n.txt 
        con la tabla de multiplicar de ese número, y 
        muestre por pantalla la línea m del fichero. 
        Si el fichero no existe debe mostrar un mensaje
        por pantalla informando de ello. 
        
    
    Parámetro: 
            - n: Número entero entre 1 y 10. Siendo n 
            el númerop de la tabla de multiplicar.   

            - m: Número entero entre 1 y 10. Siendo m
            la línea del fichero n a mostrar.
    
    
    Salida: 
    
    """
    import os   #Importo la libreria.

    if n and m in range (1,11) :
        if os.path.exists(f'tabla-{n}.txt'):  
        #Le pregunto a la libreria si existe el archivo.

            file = open(f'tabla-{n}.txt', 'r')

        print(file.readlines(m))
        return