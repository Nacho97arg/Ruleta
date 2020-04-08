import Ruleta as r

print('Ingrese el numero de tiradas')
numeroTiradas = int(input())

ruleta = r.Ruleta(numeroTiradas)

ruleta.realizarTiradas()
#ruleta.calcularFrecAbsoluta()
#ruleta.calcularFrecRelativa(numeroTiradas)


print(ruleta.tiradas)
print(ruleta.nroTiradas)

input()

ruleta.graficaFrecAbsoluta()

input()

ruleta.graficaFrecRelativa()

input()