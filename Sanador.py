import random

from Detector import Detector

class Sanador:
    def __init__(self, nombre, potencia_sanacion):
        self.nombre = nombre
        self.potencia_sanacion = potencia_sanacion
    
    def sanar_mutantes(self, matriz_adn):
        Detector = Detector("Sanador detector", 100)
        if Detector.detector_mutantes(matriz_adn):
            print("Mutacion detectada, sanando... ")
            return self._generar_adn_sano(len(matriz_adn), len(matriz_adn[0]))
        print("No se detectaron mutaciones.")
        return matriz_adn
    
    def _generar_adn_sano(self, filas, columnas):
        bases = ["A", "T", "C", "G"]
        return [[random.choice(bases) for _ in range(columnas)] for _ in range(filas)]