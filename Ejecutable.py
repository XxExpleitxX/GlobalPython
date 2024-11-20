from Detector import Detector
from Radiacion import Radiacion
from Sanador import Sanador
from Virus import Virus

def mostrar_matriz(matriz):
    for fila in matriz:
        print(" ".join(fila))

def ejecutar():
    matriz_adn = ["AGATCA", "GATTCA", "CAACAT", "GAGCTA", "ATTGCG", "CTGTTC"]
    print("Matriz de ADN actual:")
    mostrar_matriz(matriz_adn)

    opcion = input("¿Qué desea hacer? (1: Detectar mutaciones, 2: Mutar, 3: Sanar): ")

    if opcion == "1":
        detector = Detector("Detector principal", 95)
        if detector.detectar_mutantes(matriz_adn):
            print("Mutación detectada en la matriz de ADN.")
        else:
            print("No se detectaron mutaciones.")
    elif opcion == "2":
        tipo_mutacion = input("Tipo de mutación (Radiacion o Virus): ")
        base = input("Ingrese la base nitrogenada para mutar (A, T, C, G): ")
        fila = int(input("Fila inicial para la mutación (0-5): "))
        col = int(input("Columna inicial para la mutación (0-5): "))

        if tipo_mutacion.lower() == "radiacion":
            orientacion = input("Orientación de la mutación (H para horizontal, V para vertical): ")
            radiacion = Radiacion(base, "Mutación Horizontal/Vertical", 80, "horizontal" if orientacion == "H" else "vertical")
            matriz_adn = radiacion.crear_mutante(matriz_adn, (fila, col), orientacion)
        elif tipo_mutacion.lower() == "virus":
            virus = Virus("A", "Mutación Diagonal", 50, "Tipo de Virus")
            matriz_adn = virus.crear_mutante(matriz_adn, (fila, col))
        print("Matriz de ADN mutada:")
        mostrar_matriz(matriz_adn)
    elif opcion == "3":
        sanador = Sanador(100, 10)
        matriz_adn = sanador.sanar_mutantes(matriz_adn)
        print("Matriz de ADN luego de sanar:")
        mostrar_matriz(matriz_adn)
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    ejecutar()