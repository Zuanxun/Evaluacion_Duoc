#VARIABLES
id_clientes = [
    {
        "nombre":"Cris",
        "entrada":"G",  #G(general) o V(vip)
        "codigo":"C19382" #6 caracteres, 1Mayus, no espacio
    }
]

continuar = True

#DEFINICIONES
def menu():
    print("""\n----MENU PRINCIPAL----
          
[1] Comprar entrada
[2] Consultar comprador
[3] Cancelar compra
[4] Salir
""")
    
def registrar_comprador():
    contador_letras = 0
    contador_numeros = 0
    print("\n----Datos de comprador----")
    nombre = input("Ingrese nombre de comprador: ")
    entrada = input("Ingrese tipo de entraa (G/V): ").upper()
    if entrada != "G" and entrada != "V":
        print("Tipo de entrada no válida")
        return
    
    codigo = input("Ingrese código de confirmación: ")
    if len(codigo) != 6:
        print("Código no válido. Intente otra vez.")
        return
    for letra in codigo:
        if letra == " ":
            print("Código no válido. Intente otra vez.")
            return
     
    for letra in codigo:
        if letra == "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            contador_letras += 1
    if contador_letras != 0:
        print("Código no válido. Intente otra vez.")
        return
     
    for letra in codigo:
        if letra == "1234567890":
            contador_numeros += 1

    if contador_numeros != 0:
        print("Código no válido. Intente otra vez.")
        return
   
    usuario = {
        "nombre": nombre,
        "entrada": entrada,  #G(general) o V(vip)
        "codigo": codigo #6 caracteres, 1Mayus, no espacio
    }

    id_clientes.append(usuario)
    print("Código validado. ¡Entrada registrada con éxito!")
    return

def ver_diccionario():
    print("\n----Consultas compradores----")
    consulta = input("Ingrese nombre de comprador: ")
    for id in id_clientes:
        if id["nombre"] == consulta:
            print(f"Tipo de entrada: {id["entrada"]}, Código: {id["codigo"]}\n")  
            return     
    print("El usuario no se encuentra")
    return

def eliminar_comprador():
    print("\n----Eliminación de usuario----")
    eliminar = input("Ingrese nombre de comprador a cancelar: ")
    for id in id_clientes:
        if id["nombre"] == eliminar:
            id_clientes.remove(id)
            print("¡Compra cancelada!")
            return     
        
    print("El comprador no se encuentra")
    return
 
 
#SALIDA
while continuar:
    menu()
    try:
        opcion = int(input("Seleccione una opción (1-4): "))
    except ValueError:
        print("Error, ingrese un número\n")
        continue

    if opcion == 1:
        registrar_comprador()
        continue

    elif opcion == 2:
        ver_diccionario()
        continue

    elif opcion == 3:
        eliminar_comprador()
        continue

    elif opcion == 4:
        print("Programa terminado...")
        continuar = False

    else:
        print("Ingrese una opción válida.")