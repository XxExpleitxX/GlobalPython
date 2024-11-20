import random

from Detector import Detector

class Sanador():
    def __init__(self, nombre):
        self.nombre = nombre
        self.experiencia = random.randint(20, 100)
    
    def sanar_mutantes(self, matriz):
        detector = Detector("Sanador detector", matriz)
        matriz_sana = []
        if detector.detectar_mutantes():
            print("Mutacion detectada, sanando... ")
            matriz_sana = self._generar_adn_sano(len(matriz), len(matriz[0]))
            print(f'matriz sana {matriz_sana}')
            return matriz_sana
        print("No se detectaron mutaciones.")
        return matriz
    
    def _generar_adn_sano(self, filas, columnas):
        bases = ["A", "T", "C", "G"]
        nvo_adn = [[random.choice(bases) for _ in range(columnas)] for _ in range(filas)]
        print(f'nuevo adn {nvo_adn}')
        detector_a = Detector("sanador detector", nvo_adn)
        if detector_a.detectar_mutantes():
            return self._generar_adn_sano(filas,columnas)
        else:
            return nvo_adn