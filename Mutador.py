class Mutador:
    # Constructor que inicializa la base nitrogenada, la matriz de ADN y define el nombre de la mutación.
    def __init__(self, base_nitrogenada, matriz_adn):
        self.base_nitrogenada = base_nitrogenada
        self.nombre_mutacion = f'Mutación clase {self.base_nitrogenada}'
        self.matriz_adn = matriz_adn

    # Método genérico para crear mutantes, a ser implementado por las subclases.
    def crear_mutante(self):
        pass
