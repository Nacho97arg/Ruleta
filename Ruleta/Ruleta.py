import numpy as np
import matplotlib.pyplot as mp

print('Ingrese el numero de tiradas')
numeroTiradas = int(input())

tiradas = np.random.randint(0,37,size = numeroTiradas)
print(tiradas)

frecAbsolutas = []
frecRelativas = []

for x in range(0,37):
    frecAbsolutas.append(0)
    frecRelativas.append(0)

for tirada in tiradas:
    frecAbsolutas[tirada] = frecAbsolutas[tirada]+1
print(frecAbsolutas)

for x in range(0,37):
    frecRelativas[x]= frecAbsolutas[x]/numeroTiradas

frecAbs = mp.subplot()
frecRel = mp.subplot()

ejeX = []
for x in range(0,37):
    ejeX.append(x)

frecAbs.bar(ejeX,frecAbsolutas)
frecAbs.set_title('Frecuencias Absolutas')
frecRel.bar(ejeX,frecRelativas)
frecRel.set_title('Frecuencias Relativas')

mp.show()


