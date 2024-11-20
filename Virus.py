from Mutador import Mutador
class Virus(Mutador):
    def __init__(self, base_nitrogenada, matriz_adn):
        super().__init__(base_nitrogenada.upper(), matriz_adn)

    def crear_mutante(self, posicion_inicial):
        nva_matriz = self.matriz_adn
        try:
            fila, columna = posicion_inicial
            fila = int(fila)
            columna = int(columna)
            for i in range(4):
                nva_matriz[fila + i][columna + i] = self.base_nitrogenada
            return nva_matriz
        except IndexError:
            print("Error: La posición inicial de la mutación no es válida. ADN NO MUTADO.")
            return nva_matriz