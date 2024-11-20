class Detector:
    def __init__(self, nombre, matriz_adn):
        self.nombre = nombre
        self.matriz_adn = matriz_adn

    def detectar_mutantes(self):
        return(
            self._detectar_horizontal() or
            self._detectar_vertical() or
            self._detectar_diagonal()
        )
    
    def _detectar_horizontal(self):
        for fila in self.matriz_adn:
            for i in range(len(fila) - 3):
                if fila[i] == fila[i + 1] == fila[i + 2] == fila[i + 3]:
                    return True
        return False
    
    def _detectar_vertical(self):
        for col in range(len(self.matriz_adn[0])):
            for fila in range(len(self.matriz_adn) - 3):
                if (self.matriz_adn[fila][col] == self.matriz_adn[fila + 1][col] == self.matriz_adn[fila + 2][col] == self.matriz_adn[fila + 3][col]):
                    return True
        return False
    
    def _detectar_diagonal(self):
        for fila in range(len(self.matriz_adn) - 3):
            for col in range(len(self.matriz_adn[0]) - 3):
                if (self.matriz_adn[fila][col] == self.matriz_adn[fila + 1][col + 1] == self.matriz_adn[fila + 2][col + 2] == self.matriz_adn[fila + 3][col + 3]):
                    return True
        return False