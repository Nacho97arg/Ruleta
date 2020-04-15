import numpy as np
import matplotlib.pyplot as mp

class Ruleta:

	def __init__(self, nroTiradas, nroElegido):
		self.tiradas = []
		self.frecAbsolutas = []
		self.frecRelativas = []
		self.nroTiradas = nroTiradas
		self.nroElegido = nroElegido
		for x in range(0,37):
			self.frecAbsolutas.append(0)
			self.frecRelativas.append(0)
		self.ejeX = []
		for x in range(0, nroTiradas):
			self.ejeX.append(x)
		self.promedios = []
		self.desvios = []
		self.varianzas = []

	def realizarTiradas(self):
		for i in range(0, self.nroTiradas):
			nro = np.random.randint(0, 37)
			self.tiradas.append(nro)
			self.promedios.append(np.average(self.tiradas))
			self.desvios.append(np.std(self.tiradas))
			self.varianzas.append(np.var(self.tiradas))


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
		self.calcularFrecRelativa()
		frecRel = mp.subplot()
		frecRel.bar(self.ejeX, self.frecRelativas)
		frecRel.set_title('Frecuencias Relativas')
		mp.show()

	def graficaPromedio(self):
		mp.plot(self.promedios)
		mp.show()

	def graficaDesvio(self):
		mp.plot(self.desvios)
		mp.show()

	def graficaVarianza(self):
		mp.plot(self.varianzas)
		mp.show()

nTiradas = int(input("Ingrese la cantidad de tiradas a realizar\n"))
nElegido = int(input("Ingrese el nro a seguir (de 0 a 36)\n"))
rul = Ruleta(nTiradas, nElegido)
rul.realizarTiradas()
rul.calcularFrecAbsoluta()
rul.graficaFrecAbsoluta()


