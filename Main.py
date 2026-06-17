from Funciones_Integrador import *

crear_archivo()
paises = cargar_paises()

while True:
    mostrar_menu()
    opcion = input("Ingrese una opcion: ")
    match opcion:
        case "1":
            agregar_pais(paises)
        case "2":
            actualizar_pais(paises)
        case "3":
            buscar_pais(paises)
        case "4":
            filtrar_paises(paises)
        case "5":
            ordenar_paises(paises)
        case "6":
            mostrar_estadisticas(paises)
        case "7":
            print("Usted esta saliendo del programa")
            break
        case _:
            print("Ingrese una opcion valida")