from Mutador import Mutador
class Virus(Mutador):
    def __init__(self, base_nitrogenada, nombre_mutacion, nivel_mutacion, tipo_virus):
        super().__init__(base_nitrogenada, nombre_mutacion, nivel_mutacion)
        self.tipo_virus = tipo_virus

    def crear_mutante(self, matriz_adn, posicion_inicial):
        try:
            fila, columna = posicion_inicial
            for i in range(4):
                matriz_adn[fila + i][columna + i] = self.base_nitrogenada
            return matriz_adn
        except IndexError:
            print("Error: la posicion de la mutacion no es válida")
            return None