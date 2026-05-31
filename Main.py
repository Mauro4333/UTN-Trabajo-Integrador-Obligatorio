from Funciones_Integrador import *

paises = []

crear_archivo()

while True:
    mostrar_menu()
    opcion = input("Ingrese una opcion: ")
    match opcion:
        case "1":
            agregar_pais(paises)
        case "2":
            pass
        case "3":
            pass
        case "4":
            pass
        case "5":
            pass
        case "6":
            pass
        case "7":
            print("Usted esta saliendo del programa")
            break
        case _:
            print("Ingrese una opcion valida")