import random
from Detector import Detector
from Radiacion import Radiacion
from Sanador import Sanador
from Virus import Virus

def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)

def validar(mensaje, incluido):
    while(True):
        opcion_us = input(mensaje)
        if opcion_us in incluido:
            return opcion_us
        else:
            print("\nOpción incorrecta, ingrese nuevamente.")

def ejecutar():

    while(True):

        option_a = input('MENÚ PRINCIPAL\n\n1: Generar matriz de ADN manualmente\n2: Generar matriz de ADN aleatorio\n3: Usar una matriz de prueba mutante\n4: Usar una matriz de prueba humana\n5: Salir del programa\n')
        dna = []

        if option_a == '1':
            while (len(dna)!=6):
                row = input("Fila: ").strip().upper()
                if len(row) != 6 or any(letter not in "ATCG" for letter in row):
                    print("Las filas deben tener exactamente 6 letras de A, T, C, o G.")
                    continue
                dna.append(row)
        elif option_a == "2":
            bases = ["A", "T", "C", "G"]
            dna = [[random.choice(bases) for _ in range(6)] for _ in range(6)]
        elif option_a == '3':
            dna = ['ACGTTG','TTCCGG','AGTCCG','ACTGCG','AAAAAA','TTCCTT'] #Caso mutante
        elif option_a == '4':
            dna = ["AGATCA", "GATTCA", "CAACAT", "GAGCTA", "ATTGCG", "CTGTTC"] #Caso no mutante
        elif option_a == '5':
            print("\nGracias por usar nuestro detector de mutantes.")
            break
        else:
            print('\nOpción incorrecta, ingrese nuevamente.')
            continue

        print("\nMatriz de ADN actual:")
        mostrar_matriz(dna)

        while(True):

            opcion = input("\n¿Qué desea hacer a continuación?\n\n1: Detectar mutaciones\n2: Mutar\n3: Sanar\n4: Salir y volver al menú principal\n")

            if opcion == "1":

                detector = Detector("Detector principal", dna)
                print(f'\n{detector.nombre} trabajando...')
                if detector.detectar_mutantes():
                    print("\nMutación detectada en la matriz de ADN.")
                else:
                    print("\nNo se detectaron mutaciones.")

            elif opcion == "2":

                tipo_mutacion = validar("\nTipo de mutación\n\nIngrese una opción:\nR: Radiacion\nV: Virus\n","rvRV")
                base = validar("\nIngrese la base nitrogenada para mutar (A, T, C, G)\n","ATCGatcg")
                fila = validar("\nFila inicial para la mutación (0-5)\n","012345")
                col = validar("\nColumna inicial para la mutación (0-5)\n","012345")

                if tipo_mutacion.lower() == "r":
                    orientacion = validar("\nOrientación de la mutación\nH para horizontal\nV para vertical\n", "HVhv")
                    radiacion = Radiacion(base, dna)
                    print(f'\nGenerando {radiacion.nombre_mutacion}')
                    dna = radiacion.crear_mutante((fila, col), orientacion.upper())
                elif tipo_mutacion.lower() == "v":
                    virus = Virus(base, dna)
                    print(f'\nGenerando {virus.nombre_mutacion}')
                    dna = virus.crear_mutante((fila, col))

                print("\nMatriz de ADN devuelta:")
                mostrar_matriz(dna)

            elif opcion == "3":

                sanador = Sanador("Dr. Strange")
                print(f'\nSanador {sanador.nombre}, con {sanador.experiencia} puntos de experiencia curando mutante...')
                dna = sanador.sanar_mutantes(dna)
                print("\nMatriz de ADN luego de sanar:")
                mostrar_matriz(dna)
            
            elif opcion == "4":
                break

            else:
                print("\nOpción no válida, Ingrese nuevamente.")

if __name__ == "__main__":
    ejecutar()