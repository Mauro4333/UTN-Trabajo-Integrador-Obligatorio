import os

def mostrar_menu():
    print("""
          1-Agregar un país
          2-Actualizar Población y Superficie
          3-Buscar un país por nombre
          4-Filtrar países
          5-Ordenar países
          6-Mostrar estadísticas
          7-Salir
          """)
    
def crear_archivo():
    try:
        if not os.path.exists("paises.csv"):
            with open("paises.csv", "w", newline="", encoding="utf-8") as archivo:
                archivo.write("nombre,poblacion,superficie,continente\n")
    except PermissionError:
        print ("No tiene los permisos necesarios")

def cargar_paises():
    lista = []

    try:
        with open("paises.csv","r",encoding="utf-8") as archivo:
            next(archivo)
            for linea in archivo:
                datos = linea.strip().split(",")
                pais = {"nombre": datos[0],
                        "poblacion": int(datos[1]),
                        "superficie":int(datos[2]),
                        "continente":datos[3]}
                lista.append(pais)
    except FileNotFoundError:
        print("No existe el archivo")
    return lista

def guardar_paises(lista):
    with open("paises.csv", "w", encoding="utf-8") as archivo:
        archivo.write("nombre,poblacion,superficie,continente\n")
        for pais in lista:
            archivo.write(
                f"{pais['nombre']},{pais['poblacion']},{pais['superficie']},{pais['continente']}\n"
            )

def mostrar_menu_continentes():
    print("""
        1-Asia
        2-America
        3-Africa
        4-Europa
        5-Oceania
          """)

def agregar_pais(lista):
    try:
        pais = input("Ingrese el nombre del pais a agregar: ").capitalize()
        if pais.strip() == "":
            print("Ingrese un nombre valido")
        elif not pais.replace(" ", "").isalpha():
            print("El nombre del pais no es valido")
        else:
            repetido = False
            for item in lista:
                if item["nombre"] == pais:
                    repetido = True
                    break
            if repetido:
                print("Ese pais ya existe")
                return
            poblacion = int(input("Ingrese cuanta poblacion tiene su pais: "))
            if poblacion <= 0:
                print("Debe ingresar un numero mayor a 0")
            else:
                superficie = int(input("Ingrese la superficie de su pais: "))
                if superficie <= 0:
                    print("Ingrese un numero mayor a 0")
                else:
                    mostrar_menu_continentes()
                    opcion_cont = input("Ingrese el continente al que pertenece ")
                    match opcion_cont:
                        case "1":
                            continente = "asia"
                        case "2":
                            continente = "america"
                        case "3":
                            continente = "africa"
                        case "4":
                            continente = "europa"
                        case "5":
                            continente = "oceania"
                        case _:
                            print("Debe ingresar un numero del 1 al 5")
                            return
                    pais_datos = {
                        "nombre": pais,
                        "poblacion": poblacion,
                        "superficie": superficie,
                        "continente": continente
                    }
                    lista.append(pais_datos)
                    guardar_paises(lista)
                    print("Pais Agregado correctamente")
    except ValueError:
        print("Debe ingresar un numero entero mayor a 0")

def mostrar_menu_busqueda():
    print("""
        1-Busqueda exacta
        2-Busqueda Parcial
          """)
    

def buscar_pais(lista):
    if (len(lista)) <= 0:
        print("Debe ingresar un pais primero")
    else:
        mostrar_menu_busqueda()
        opcion = input("Ingrese una opcion ")
        match opcion:
            case "1":
                encontrado = False
                buscador = input("Ingrese el pais a buscar ").capitalize()
                for pais in lista:
                    if pais["nombre"] == buscador:
                        print(f"Pais: {pais["nombre"]} Poblacion: {pais["poblacion"]} superficie: {pais["superficie"]} continente: {pais["continente"]} ")
                        encontrado = True
                        break
                if not encontrado:
                    print("No se encontro el pais")
            case "2":
                encontrado = False
                buscador = input("Ingrese la parte a buscar del pais ").strip().lower()
                if buscador == "":
                    print("Debe ingresar un texto para buscar")
                    return
                for pais in lista:
                    if buscador in pais["nombre"].lower():
                        print(f"Pais: {pais["nombre"]} "
                        f"Poblacion: {pais["poblacion"]} "
                        f"Superficie: {pais["superficie"]} "
                        f"Continente: {pais["continente"]}")
                        encontrado = True
                if not encontrado:
                    print("No se encontro coincidencias")
            case _:
                print("Debe ingresar un numero valido")