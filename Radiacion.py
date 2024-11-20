from Mutador import Mutador
class Radiacion(Mutador):
    def __init__(self, base_nitrogenada, matriz_adn):
        super().__init__(base_nitrogenada.upper(), matriz_adn)

    def crear_mutante(self, posicion_inicial, orientacion_de_la_mutacion):
        try:
            fila, columna = posicion_inicial
            fila = int(fila)
            columna = int(columna)
            if orientacion_de_la_mutacion == "H":
                for i in range(4):
                    self.matriz_adn[fila][columna + i] = self.base_nitrogenada
            elif orientacion_de_la_mutacion == "V":
                for i in range(4):
                    self.matriz_adn[fila + i][columna] = self.base_nitrogenada
            return self.matriz_adn
        except IndexError:
            print("Error: La posicion o direccion de la mutacion no es válida. ADN NO MUTADO.")
            return self.matriz_adn