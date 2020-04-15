import numpy as np
import matplotlib.pyplot as matplot

nroTiradas = int(input("Ingrese la cantidad de veces a iterar el experimento:\n"))
nroSeguido = int(input("Ingrese el numero a seguir:\n"))

print("Relizando experimento...\n")

valores = np.arange(0, 37)
    
frecRelEsperado = round(1/len(valores),4)             # Relative Frecuency Expected (1/37)
promEsperado = round(np.mean(valores), 4)         # Average (Mean) Expected (666/37)
varianEsperada = round(np.var(valores), 4)     # Variance Expected (114)
desvEsperado = round(np.std(valores), 4)    # Deviation Expected (Square Root of 114)

nroDeRepeticiones = 5

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


matplot.figure()
graf1=matplot.subplot(221,aspect='auto',anchor='C')
graf1.plot(frecRelativa[0],'tab:red')
graf1.axhline(frecRelEsperado,color='blue')

graf2=matplot.subplot(222,anchor='C')
graf2.plot(promedios[0], 'tab:purple')

graf3=matplot.subplot(223,anchor='C')
graf3.plot(desvioEstandar[0],'tab:blue')

graf4=matplot.subplot(224,anchor='C')
graf4.plot(variancia[0],'tab:orange')
matplot.show()
