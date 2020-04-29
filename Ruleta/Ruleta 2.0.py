import numpy as np
import matplotlib.pyplot as matplot

def plotGraficos(arregloFrecRel, arregloProm, arregloDesvEst, arregloVar, unico):
    matplot.figure(figsize=(7,7))
    if unico:
        matplot.suptitle("Resultados de una iteracion")
    if not(unico):
        matplot.suptitle("Resultados Promedio de las iteraciones")

    graf1=matplot.subplot(221,aspect='auto',anchor='N')
    graf1.plot(frecRelativa[0],'tab:red')
    graf1.axhline(frecRelEsperado,color='blue')
    graf1.set_title("Frecuencia Relativa")

    graf2=matplot.subplot(222,anchor='N')
    graf2.plot(promedios[0], 'tab:purple')
    graf2.axhline(promEsperado,color='blue')
    graf2.set_title("Promedio")

    graf3=matplot.subplot(223,anchor='S')
    graf3.plot(desvioEstandar[0],'tab:blue')
    graf3.axhline(desvEsperado,color='blue')
    graf3.set_title("Desviacion Estandar")

    graf4=matplot.subplot(224,anchor='S')
    graf4.plot(variancia[0],'tab:orange')
    graf4.axhline(varianEsperada,color='blue')
    graf4.set_title("Variancia")
    matplot.show()


nroTiradas = int(input("Ingrese la cantidad de veces a iterar el experimento:\n"))


nroSeguido = int(input("Ingrese el numero a seguir:\n"))
if (nroSeguido>36 or nroSeguido<0):
    print("El numero a seguir debe estar entre 0 y 36")
while (nroSeguido<0 or nroSeguido>36):
    nroSeguido = int(input("Numero ingresado invalido, ingrese un numero valido:\n"))

print("Relizando experimento...\n")

valoresRuleta = np.arange(0, 37)
    
frecRelEsperado = round(1/len(valoresRuleta),4)
promEsperado = round(np.mean(valoresRuleta), 4)
varianEsperada = round(np.var(valoresRuleta), 4)
desvEsperado = round(np.std(valoresRuleta), 4)

nroDeRepeticiones = 6

frecRelativa=np.zeros((nroDeRepeticiones,nroTiradas+1))
frecAbsoluta=np.zeros((nroDeRepeticiones,nroTiradas+1))
promedios=np.zeros((nroDeRepeticiones,nroTiradas+1))
desvioEstandar=np.zeros((nroDeRepeticiones,nroTiradas+1))
variancia=np.zeros((nroDeRepeticiones,nroTiradas+1))

for n in range(nroDeRepeticiones):
    for i in range(1,nroTiradas+1):
        valores = np.random.randint(0,37,i)
        debug = (valores == nroSeguido)
        nroAciertos = np.count_nonzero(valores == nroSeguido)
        frecRelativa[n][i] = nroAciertos/i
        frecAbsoluta[n][i] = nroAciertos
        promedios[n][i]=np.mean(valores)
        desvioEstandar[n][i]=np.std(valores)
        variancia[n][i]=np.var(valores)

plotGraficos(frecRelativa[0], promedios[0],desvioEstandar[0], variancia[0], 1)

frecRelProm = (frecRelativa[0] + frecRelativa[1] + frecRelativa[2] + frecRelativa[3] + frecRelativa[4] + frecRelativa[5]) / nroDeRepeticiones
promedioProm = (promedios[0] + promedios[1] + promedios[2] + promedios[3] + promedios[4] + promedios[5]) / nroDeRepeticiones
varianciaProm = (variancia[0] + variancia[1] + variancia[2] + variancia[3] + variancia[4] + variancia[5]) / nroDeRepeticiones
desvioProm = (desvioEstandar[0] + desvioEstandar[1] + desvioEstandar[2] + desvioEstandar[3] + desvioEstandar[4] + desvioEstandar[5]) / nroDeRepeticiones

plotGraficos(frecRelProm,promedioProm,desvioProm,varianciaProm, 0)


