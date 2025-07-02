import os
os.system("cls")

turistas = {
    "001": ["John Doe", "Estados Unidos", "12-01-2024"],
    "002": ["Emily Smith", "Estados Unidos", "23-03-2024"],
    "012": ["Julian Martinez", "Argentina", "19-09-2023"],
    "014": ["Agustin Morales", "Argentina", "28-03-2024"],
    "005": ["Carlos Garcia", "Mexico", "10-05-2024"],
    "006": ["Maria Lopez", "Mexico", "08-12-2023"],
    "007": ["Joao Silva", "Brasil", "20-06-2024"],
    "003": ["Michael Brown", "Estados Unidos", "05-07-2023"],
    "004": ["Jessica Davis", "Estados Unidos", "15-11-2024"],
    "008": ["Ana Santos", "Brasil", "03-10-2023"],
    "010": ["Martin Fernandez", "Argentina", "13-02-2023"],
    "011": ["Sofia Gomez", "Argentina", "07-04-2024"]
}


def turistas_por_pais(turistas):
    if not turistas:
        print("lo siento pero no tenemos turistas")
    else:
        busqueda_pais = input("ingrese el pais: ").strip().title()
        encontrados = []

        for codigo, datos in turistas.items():
            nombre, pais, fecha = datos
            if pais == busqueda_pais:
                encontrados.append((codigo, nombre, fecha))
        
        if encontrados:
            print(f"Turistas de {busqueda_pais}: ")
            for codigo, nombre, fecha in encontrados:
                print(f"ID: {codigo}, Nombre: {nombre}, Fecha: {fecha}")
        else:
            print("Informacion no encontrada.")


def turistas_por_mes(turistas):
    if not turistas:
        print("lo siento pero no tenemos turistas")
    else:
        try:

            busqueda_pais = int(input("ingrese el mes: "))

            if 1 <= busqueda_pais <= 12:
                encontrados_mes = []

                for codigo, datos in turistas.items():
                    nombre, nombre, fecha = datos
                    
                    mes = int(fecha.split("-")[1])

                    if mes == busqueda_pais:
                        encontrados_mes.append((codigo, nombre, fecha))
                
                if encontrados_mes:
                    print(f"Turistas de {busqueda_pais}: ")
                    for codigo, nombre, fecha in encontrados_mes:
                        print(f"ID: {codigo}, Nombre: {nombre}, Fecha: {fecha}")
                else:
                    print("Informacion no encontrada.")
            else:
                print("ingrese un mes correcto (1 - 12)")

        except ValueError:
            print("Error.")


def eliminar_turista(turistas):
    if not turistas:
        print("No hay turistas registrados.")
    
    else:
        try:
            codigo = input("ingrese el codigo (ID) del turista a eliminar: ")
            if codigo in turistas:
                del turistas[codigo]
                print("turista eliminado con exito")
                print("el diccionario de turistas: ", turistas)
            else:
                print("codigo no encontrado")
        except ValueError:
            print("Error, ingrese un numero valido")
    
    return turistas


def menu():

    turistas = {
        "001": ["John Doe", "Estados Unidos", "12-01-2024"],
        "002": ["Emily Smith", "Estados Unidos", "23-03-2024"],
        "012": ["Julian Martinez", "Argentina", "19-09-2023"],
        "014": ["Agustin Morales", "Argentina", "28-03-2024"],
        "005": ["Carlos Garcia", "Mexico", "10-05-2024"],
        "006": ["Maria Lopez", "Mexico", "08-12-2023"],
        "007": ["Joao Silva", "Brasil", "20-06-2024"],
        "003": ["Michael Brown", "Estados Unidos", "05-07-2023"],
        "004": ["Jessica Davis", "Estados Unidos", "15-11-2024"],
        "008": ["Ana Santos", "Brasil", "03-10-2023"],
        "010": ["Martin Fernandez", "Argentina", "13-02-2023"],
        "011": ["Sofia Gomez", "Argentina", "07-04-2024"]
    }
    while True:

        print("------------------------------")
        print("------- MENU PRINCIPAL -------")
        print("---- 1-Turistas por pais -----")
        print("----- 2-Turista por mes ------")
        print("----- 3-Eliminar turista -----")
        print("----------- 4-Salir ----------")
        print("------------------------------")
        
        try:
            opc = int(input("ingrese una opcion: "))

            if opc == 1:
                print("opcion 1 Turistas por pais")
                turistas_por_pais(turistas)

            
            elif opc == 2:
                print("opcion 2 Turistas por mes")
                turistas_por_mes(turistas)

            elif opc == 3:
                print("opcion 3 Eliminar turistas")
                eliminar_turista(turistas)

            elif opc == 4:
                print("Adios :D")
                break

            else:
                print("ingrese una de las opciones en pantalla")
        except ValueError:
            print("Error, no puede ingresar letras o sinbolos")

menu()