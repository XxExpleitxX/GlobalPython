import random
from Detector import Detector
from Radiacion import Radiacion
from Sanador import Sanador
from Virus import Virus
    #Función para mostrar la matriz de adn

def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)
    
    #Función para validar cada opcion que ingresa el usuario
    
def validar(mensaje, incluido):
    while(True):
        opcion_us = input(mensaje)
        if opcion_us in incluido:
            return opcion_us
        else:
            print("\nOpción incorrecta, ingrese nuevamente.")

def ejecutar():

    while(True):
        # Menú principal del programa
        option_a = input(
            'MENÚ PRINCIPAL\n\n'
            '1: Generar matriz de ADN manualmente\n'
            '2: Generar matriz de ADN aleatorio\n'
            '3: Usar una matriz de prueba mutante\n'
            '4: Usar una matriz de prueba humana\n'
            '5: Salir del programa\n'
            )
        dna = []

        if option_a == '1': #Genera matriz manual
            while (len(dna)!=6):
                row = input("Fila: ").strip().upper()
                if len(row) != 6 or any(letter not in "ATCG" for letter in row):
                    print("Las filas deben tener exactamente 6 letras de A, T, C, o G.")
                    continue
                dna.append(row)
        elif option_a == "2": #Genera matriz aleatoria
            bases = ["A", "T", "C", "G"]
            dna = [[random.choice(bases) for _ in range(6)] for _ in range(6)]
        elif option_a == '3': #Caso mutante
            dna = ['ACGTTG','TTCCGG','AGTCCG','ACTGCG','AAAAAA','TTCCTT'] 
        elif option_a == '4': #Caso no mutante
            dna = ["AGATCA", "GATTCA", "CAACAT", "GAGCTA", "ATTGCG", "CTGTTC"]
        elif option_a == '5': #Salida del programa
            print("La matriz resultante de este programa fue: ")
            mostrar_matriz(dna)
            print("\nGracias por usar nuestro detector de mutantes.")
            break
        else: #Opción incorrecta
            print('\nOpción incorrecta, ingrese nuevamente.')
            continue

        print("\nMatriz de ADN actual:")
        mostrar_matriz(dna)
        
        # Menú secundario para acciones sobre la matriz
        
        while(True):

            opcion = input(
                            "\n¿Qué desea hacer a continuación?\n\n"
                            "1: Detectar mutaciones\n"
                            "2: Mutar\n"
                            "3: Sanar\n"
                            "4: Salir y volver al menú principal\n"
                        )

            if opcion == "1":  #Detectar mutaciones en la matriz
                
                detector = Detector("Detector principal", dna)
                print(f'\n{detector.nombre} trabajando...')
                if detector.detectar_mutantes():
                    print("\nMutación detectada en la matriz de ADN.")
                else:
                    print("\nNo se detectaron mutaciones.")

            elif opcion == "2": #Mutar

                tipo_mutacion = validar("\nTipo de mutación\n\nIngrese una opción:\nR: Radiacion\nV: Virus\n","rvRV")
                base = validar("\nIngrese la base nitrogenada para mutar (A, T, C, G)\n","ATCGatcg")
                fila = validar("\nFila inicial para la mutación (0-5)\n","012345")
                col = validar("\nColumna inicial para la mutación (0-5)\n","012345")

                if tipo_mutacion.lower() == "r": #Radiacion
                    orientacion = validar("\nOrientación de la mutación\nH para horizontal\nV para vertical\n", "HVhv")
                    radiacion = Radiacion(base, dna)
                    print(f'\nGenerando {radiacion.nombre_mutacion}')
                    dna = radiacion.crear_mutante((fila, col), orientacion.upper())
                elif tipo_mutacion.lower() == "v": #Virus
                    virus = Virus(base, dna)
                    print(f'\nGenerando {virus.nombre_mutacion}')
                    dna = virus.crear_mutante((fila, col))

                print("\nMatriz de ADN devuelta:")
                mostrar_matriz(dna)

            elif opcion == "3": #Sanar

                sanador = Sanador("Dr. Strange")
                print(f'\nSanador {sanador.nombre}, con {sanador.experiencia} puntos de experiencia curando mutante...')
                dna = sanador.sanar_mutantes(dna)
                print("\nMatriz de ADN luego de sanar:")
                mostrar_matriz(dna)
            
            elif opcion == "4": #Salir
                break

            else: #Opción incorrecta
                print("\nOpción no válida, Ingrese nuevamente.")

if __name__ == "__main__":
    ejecutar()