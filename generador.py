"""
Un generador de senal es el responsable de generar una senal portadora.

"""
import numpy as np
from matplotlib import pyplot as plt
class Generador(object):


    def __init__(self, amplitud, fase, frecuencia):
        self.amplitud = amplitud
        self.fase = fase
        self.frecuencia = frecuencia

        #  muestras por segundo
        self.frecuencia_muestreo = frecuencia*3


    def generar(self, tiempo_inicial, tiempo_final):

        import math
        # self.noise_level
        cantidad_muestras = (tiempo_final - tiempo_inicial).seconds/\
        self.frecuencia_muestreo

        muestras = range(int(cantidad_muestras))

        #Agrego un ruido blanco aleatorio a la senal

        ret = [((np.random.random())*0.01) + self.amplitud*math.sin(2*(1/self.frecuencia)*i+self.fase) \
        for i in muestras]

        plt.plot(ret)
        plt.show()

        return ret
