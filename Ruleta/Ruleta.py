import numpy as np
import matplotlib.pyplot as mp

class Ruleta:

    def __init__(self, nroTiradas):
    	self.tiradas = []
    	self.frecAbsolutas = []
    	self.frecRelativas = []
    	self.nroTiradas = nroTiradas
    	for x in range(0,37):
    		self.frecAbsolutas.append(0)
    		self.frecRelativas.append(0)
    	self.ejeX = []
    	for x in range(0,37):
    		self.ejeX.append(x)

    def realizarTiradas(self):
    	self.tiradas = np.random.randint(0,37,size = self.nroTiradas)

    def calcularFrecAbsoluta(self):
    	for tirada in self.tiradas:
    		self.frecAbsolutas[tirada] = self.frecAbsolutas[tirada]+1

    def calcularFrecRelativa(self):
    	for x in range(0,37):
    		self.frecRelativas[x]= self.frecAbsolutas[x]/self.nroTiradas

    def graficaFrecAbsoluta(self):
    	self.calcularFrecAbsoluta()
    	frecAbs = mp.subplot()
    	frecAbs.bar(self.ejeX, self.frecAbsolutas)
    	frecAbs.set_title('Frecuencias Absolutas')
    	mp.show()

    def graficaFrecRelativa(self):
    	self.calcularFrecRelativa(self.nroTiradas)
    	frecRel = mp.subplot()
    	frecRel.bar(self.ejeX, self.frecRelativas)
    	frecRel.set_title('Frecuencias Relativas')
    	mp.show()

