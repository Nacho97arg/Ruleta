import Ruleta as r

print('Ingrese el numero de tiradas')
numeroTiradas = int(input())

ruleta = r.Ruleta(numeroTiradas)

ruleta.realizarTiradas()

input()

ruleta.graficaPromedio()

input()

ruleta.graficaDesvio()

input()

ruleta.graficaVarianza()