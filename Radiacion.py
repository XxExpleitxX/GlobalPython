from Mutador import Mutador
class Radiacion(Mutador):
    def __init__(self, base_nitrogenada, nombre_mutacion, nivel_mutacion, tipo_radiacion):
        super().__init__(base_nitrogenada, nombre_mutacion, nivel_mutacion)
        self.tipo_radiacion = tipo_radiacion

    def crear_mutante(self, matriz_adn, posicion_inicial, orientacion_de_la_mutacion):
        try:
            fila, columna = posicion_inicial
            if orientacion_de_la_mutacion == "H":
                for i in range(4):
                    matriz_adn[fila][columna + i] = self.base_nitrogenada
            elif orientacion_de_la_mutacion == "V":
                for i in range(4):
                    matriz_adn[fila + i][columna] = self.base_nitrogenada
            return matriz_adn
        except IndexError:
            print("Error: la posicion o direccion de la mutacion no es válida")
            return None