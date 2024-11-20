import random


class Detector:
    def __init__(self, nombre):
        self.nombre = nombre
        self.potencia_deteccion = random.randint(50,100)

    def detectar_mutantes(self, matriz_adn):
        return(
            self._detectar_horizontal(matriz_adn) or
            self._detectar_vertical(matriz_adn) or
            self._detectar_diagonal(matriz_adn)
        )
    
    def _detectar_horizontal(self, matriz_adn):
        for fila in matriz_adn:
            for i in range(len(fila) - 3):
                if fila[i] == fila[i + 1] == fila[i + 2] == fila[i + 3]:
                    return True
        return False
    
    # Busca 4 bases iguales seguidas en cada columna.
    def _detectar_vertical(self, matriz_adn):
        for col in range(len(matriz_adn[0])):
            for fila in range(len(matriz_adn) - 3):
                if (matriz_adn[fila][col] == matriz_adn[fila + 1][col] == matriz_adn[fila + 2][col] == matriz_adn[fila + 3][col]):
                    return True
        return False
    
    # Busca 4 bases iguales seguidas en diagonales
    def _detectar_diagonal(self, matriz_adn):
        for fila in range(len(matriz_adn) - 3):
            for col in range(len(matriz_adn[0]) - 3):
                if (matriz_adn[fila][col] == matriz_adn[fila + 1][col + 1] == matriz_adn[fila + 2][col + 2] == matriz_adn[fila + 3][col + 3]):
                    return True
        return False