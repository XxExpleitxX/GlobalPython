from Mutador import Mutador
class Virus(Mutador):
    # Constructor que inicializa un virus con la base nitrogenada en mayúsculas y la matriz de ADN.
    def __init__(self, base_nitrogenada, matriz_adn):
        super().__init__(base_nitrogenada.upper(), matriz_adn)

    # Método para aplicar una mutación diagonal en la matriz de ADN.
    def crear_mutante(self, posicion_inicial):
        nva_matriz = self.matriz_adn
        try:
            fila, columna = posicion_inicial
            fila = int(fila)
            columna = int(columna)
            # Aplica la mutación diagonal sobre 4 posiciones consecutivas.
            for i in range(4):
                nva_matriz[fila + i][columna + i] = self.base_nitrogenada
            return nva_matriz
        except IndexError:
            # Maneja errores si la posición inicial excede los límites de la matriz.
            print("Error: La posición inicial de la mutación no es válida. ADN NO MUTADO.")
            return nva_matriz