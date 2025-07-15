#DATOS
productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
             '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
             'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
             'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
             'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
             '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
             '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
             'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']}

stock = {'8475HD': [387990,10],
         '2175HD': [327990,4], 
         'JjfFHD': [424990,1],
         'fgdxFHD': [664990,21], 
         '123FHD': [290890,32], 
         '342FHD': [444990,7],
         'GF75HD': [749990,2], 
         'UWU131HD': [349990,1], 
         'FS1230HD': [249990,0]}

#FUNCIONES

def stock_marca(marca:str):
    lista_codigo = []
    for codigo in productos:
        if productos[codigo][0].lower() == marca.lower():
            lista_codigo.append(codigo.lower())

    stock_total = 0
    for id_marca in lista_codigo:
        for notebooks in stock:
            if id_marca.lower() == notebooks.lower():
                stock_total += stock[notebooks][1]
    print(f"El stock es: {stock_total}")

#stock_marca("DEll")
    
def búsqueda_precio(p_min:int, p_max:int):
    lista_precios = []
    for codigo in stock:
        if stock[codigo][0] >= p_min and stock[codigo][0] <= p_max:
            for id_codigo in productos:
                if codigo == id_codigo:
                    lista_precios.append(codigo)
    
    #lista_precios[0] = "Dell--" + lista_precios[0]
    iterador = 0
    for codigo in lista_precios:
        for id_codigo in productos:
            if codigo == id_codigo:
                lista_precios[iterador] = productos[id_codigo][0] + "--" + codigo
                iterador += 1
                
    if lista_precios == []:
        print("No hay notebooks en ese rango de precios.")
        return

    lista_precios.sort()
    print(f"Los notebooks entre los precios conlutas son: {lista_precios}")

#búsqueda_precio(0,80000000)

def actualizar_precio(modelo:str, p:int):
    iteracion = False
    for nombre in stock:
        if modelo.lower() == nombre.lower():
            stock[nombre][0] = p
            iteracion = True
            print("Precio actualizado!!")
    if iteracion == False:
        print("El modelo no existe!!")

#actualizar_precio("8475sdfsfHD",23424)

def validar_nombre(mensaje:str):
    nombre = input(mensaje)
    nombre = nombre.lower().strip()
    return nombre

def validar_numero (numero:int):
        if numero < 0:
            print("Debe ingresar valores enteros!!\n")
        else:
            return numero
        

def menu():
    while True:
        print("""\n*** MENU PRINCIPAL ***
    1. Stock marca.
    2. Búsqueda por precio.
    3. Actualizar precio.
    4. Salir.
    """)
        try:
            opcion = int(input("Ingrese opción: "))


            if opcion == 1:
                marca = validar_nombre("Ingrese marca a consultar: ")
                stock_marca(marca)
                continue

            if opcion == 2:
                precio_min = int(input("Ingrese precio mínimo: "))
                precio_min = validar_numero(precio_min)

                precio_max = int(input("Ingrese precio máximo: "))
                precio_max = validar_numero(precio_max)
                búsqueda_precio(precio_min, precio_max) 
                continue   

            if opcion == 3:
                while True:
                    codigo = validar_nombre("Ingrese modelo a actualizar: ")
                    precio = int(input("Ingrese precio nuevo: "))
                    precio= validar_numero(precio)
                    3
                    actualizar_precio(codigo, precio)

                    opcion = validar_nombre("Desea actualizar otro precio (si/no)?: ")

                    if opcion == "no" or opcion == "nó":
                        break
                continue

            if opcion == 4:
                print("Programa finalizado.")
                break
                
            else:
                print("Debe selecionar una opción válida!!")
        except ValueError:
            print("Debe seleccionar una opción válida!!")
menu()
            
