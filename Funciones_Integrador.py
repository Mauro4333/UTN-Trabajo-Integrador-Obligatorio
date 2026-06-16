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
                archivo.write("Argentina,46735004,2780400,america\n")
                archivo.write("Brasil,213421037,8515767,america\n")
                archivo.write("Mexico,130861007,1964375,america\n")
                archivo.write("Estados Unidos,340110988,9833517,america\n")
                archivo.write("España,48300000,505990,europa\n")
                archivo.write("Francia,68300000,551695,europa\n")
                archivo.write("Alemania,83500000,357588,europa\n")
                archivo.write("Italia,58900000,301340,europa\n")
                archivo.write("China,1408975000,9562910,asia\n")
                archivo.write("India,1450935791,3287263,asia\n")
                archivo.write("Japon,123975371,377975,asia\n")
                archivo.write("Arabia Saudita,34000000,2149690,asia\n")
                archivo.write("Nigeria,232679478,923768,africa\n")
                archivo.write("Egipto,116538258,1002450,africa\n")
                archivo.write("Sudafrica,63000000,1221037,africa\n")
                archivo.write("Argelia,47000000,2381741,africa\n")
                archivo.write("Australia,27000000,7692024,oceania\n")
                archivo.write("Nueva Zelanda,5300000,268838,oceania\n")
                archivo.write("Papua Nueva Guinea,11000000,462840,oceania\n")
                archivo.write("Fiyi,930000,18274,oceania\n")
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
        pais = input("Ingrese el nombre del pais a agregar: ").strip().title()
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
                buscador = input("Ingrese el pais a buscar ").strip().title()
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


def mostrar_menu_filtrar():
    print("""
        1-Filtrar paises por continente
        2-Filtrar paises por poblacion
        3-Filtrar paises por superficie
          """)
    
def poblacion_superficie():
    print("""
        1-Poblacion
        2-Superficie
          """)

def filtrar_paises(lista):
    if len(lista) <= 0:
        print("Debe ingresar un pais primero")
    else:
        mostrar_menu_filtrar()
        opcion = input("Ingrese una opcion ")
        match opcion:
            case "1":
                mostrar_menu_continentes()
                opcion_cont = input("Ingrese el continente ")
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
                        print("Opcion invalida")
                        return
                encontrado = False
                for pais in lista:
                    if pais["continente"] == continente:
                        print(pais)
                        encontrado = True
                if not encontrado:
                    print("No hay paises en ese continente")
            case "2":
                try:
                    minimo = int(input("Ingrese la poblacion minima "))
                    maximo = int(input("Ingrese la poblacion maxima "))
                    if minimo > maximo:
                        print("La poblacion minima no puede ser mayor que la maxima")
                        return
                    if minimo <= 0 or maximo <= 0:
                        print("Debe ingresar numeros mayores a 0")
                        return
                    encontrado = False
                    for pais in lista:
                        if minimo <= pais["poblacion"] <= maximo:
                            print(f"Pais: {pais["nombre"]}"
                            f"Poblacion: {pais["poblacion"]}"
                            f"Superficie: {pais["superficie"]}|"
                            f"Continente: {pais["continente"]}")
                            encontrado = True
                    if not encontrado:
                        print("No se encontraron paises en ese rango")
                except ValueError:
                    print("Debe ingresar numeros enteros")
            case "3":
                try:
                    minimo = int(input("Ingrese la superficie minima "))
                    maximo = int(input("Ingrese la superficie maxima "))
                    if minimo > maximo:
                        print("La superficie minima no puede ser mayor que la maxima")
                        return
                    if minimo <= 0 or maximo <= 0:
                        print("Debe ingresar numeros mayores a 0")
                        return
                    encontrado = False
                    for pais in lista:
                        if minimo <= pais["superficie"] <= maximo:
                            print(f"Pais: {pais["nombre"]}"
                            f"Poblacion: {pais["poblacion"]}"
                            f"Superficie: {pais["superficie"]} "
                            f"Continente: {pais["continente"]}")
                            encontrado = True
                    if not encontrado:
                        print("No se encontraron paises en ese rango")
                except ValueError:
                    print("Debe ingresar numeros enteros")
            case _:
                print("Debe ingresar una opcion valida")