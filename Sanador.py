import random

from Detector import Detector

class Sanador():
    # Constructor que inicializa el nombre del sanador y su experiencia aleatoria.
    def __init__(self, nombre):
        self.nombre = nombre
        self.experiencia = random.randint(20, 100)
    
    # Método principal para sanar mutantes en la matriz de ADN.
    def sanar_mutantes(self, matriz):
        detector = Detector("Sanador detector")
        matriz_sana = []
        # Si hay mutantes detectados, genera una matriz sana.
        if detector.detectar_mutantes(matriz):
            print("Mutacion detectada, sanando... ")
            matriz_sana = self._generar_adn_sano(len(matriz), len(matriz[0]))
            return matriz_sana
        print("No se detectaron mutaciones.")
        return matriz
    
    # Método privado que genera una nueva matriz de ADN sin mutantes.
    def _generar_adn_sano(self, filas, columnas):
        bases = ["A", "T", "C", "G"]
        nvo_adn = [[random.choice(bases) for _ in range(columnas)] for _ in range(filas)]
        detector_a = Detector("sanador detector")
        if detector_a.detectar_mutantes(nvo_adn):
            return self._generar_adn_sano(filas,columnas)
        else:
            return nvo_adn