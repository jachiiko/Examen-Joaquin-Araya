#Examen Joaquin Araya M. 
import random
import csv
import math

trabajadores = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]

sueldos = {}

def asignar_sueldos():
    global sueldos
    sueldos = {trabajador: random.randint(300000, 2500000) for trabajador in trabajadores}
    print("Sueldos asignados aleatoriamente.\n")

def clasificar_sueldos():
    clasificacion = {"menores": {}, "medios": {}, "altos": {}}
    for trabajador, sueldo in sueldos.items():
        if sueldo < 800000:
            clasificacion["menores"][trabajador] = sueldo
        elif 800000 <= sueldo <= 2000000:
            clasificacion["medios"][trabajador] = sueldo
        else:
            clasificacion["altos"][trabajador] = sueldo

    print("Clasificación de sueldos:")
    for clave, valor in clasificacion.items():
        print(f"\nSueldos {clave}: TOTAL: {len(valor)}")
        for trabajador, sueldo in valor.items():
            print(f"{trabajador} ${sueldo}")
    print(f"\nTOTAL SUELDOS: ${sum(sueldos.values())}\n")

def ver_estadisticas():
    sueldos_lista = list(sueldos.values())
    sueldo_mas_alto = max(sueldos_lista)
    sueldo_mas_bajo = min(sueldos_lista)
    promedio_sueldos = sum(sueldos_lista) / len(sueldos_lista)
    media_geometrica = math.exp(sum(math.log(x) for x in sueldos_lista) / len(sueldos_lista))
    
    print("Estadísticas de sueldos:")
    print(f"Sueldo más alto: ${sueldo_mas_alto}")
    print(f"Sueldo más bajo: ${sueldo_mas_bajo}")
    print(f"Promedio de sueldos: ${promedio_sueldos}")
    print(f"Media geométrica: ${media_geometrica}\n")

def reporte_sueldos():
    with open('reporte_sueldos.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre empleado", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Líquido"])
        for trabajador, sueldo in sueldos.items():
            descuento_salud = sueldo * 0.07
            descuento_afp = sueldo * 0.12
            sueldo_liquido = sueldo - descuento_salud - descuento_afp
            writer.writerow([trabajador, sueldo, descuento_salud, descuento_afp, sueldo_liquido])
    print("Reporte de sueldos generado en 'reporte_sueldos.csv'.\n")

def mostrar_menu():
    while True:
        print("Menú de opciones:")
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas")
        print("4. Reporte de sueldos")
        print("5. Salir del programa")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            asignar_sueldos()
        elif opcion == "2":
            clasificar_sueldos()
        elif opcion == "3":
            ver_estadisticas()
        elif opcion == "4":
            reporte_sueldos()
        elif opcion == "5":
            print("Desarrollado por Joaquin Araya RUT 20.287.239-5")
            break
        else:
            print("Opción no válida, por favor intente nuevamente.\n")

if __name__ == "__main__":
    mostrar_menu()