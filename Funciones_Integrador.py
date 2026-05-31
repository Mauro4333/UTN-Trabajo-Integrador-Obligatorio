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
        pais = input("Ingrese el nombre del pais a agregar: ").lower().capitalize()
        if pais.strip() == "":
            print("Ingrese un nombre valido")
        elif not pais.replace(" ","").isalpha():
            print("El nombre del pais no es valido")
        else:
            poblacion = int(input("Ingrese cuanta poblacion tiene su pais: "))
            if poblacion <=0:
                print("Debe ingresar un numero mayor a 0")
            else:
                superficie = int(input("Ingrese la superficie de su pais: "))
                if superficie <=0:
                    print("Ingrese un numero mayor a 0")
                else:
                    mostrar_menu_continentes()
                    opcion_cont = input("Ingrese")
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
                    pais_datos = {"nombre":pais,
                            "poblacion":poblacion,
                            "superficie":superficie,
                            "continente":continente
                                      }
                    lista.append(pais_datos)
                    guardar_paises(lista)
                    print("Pais Agregado correctamente")
    except ValueError:
        print("Debe ingresar un numero entero mayor a 0")