import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mp 
import math
archivo=open("columnas.txt","r")#abriendo el archivo que contiene datos de FIRAS 
columna1=[]#guardara las frecuencias
columna2=[]#guardara los espectros
columna4=[]#guardara errores
h=6.62607004e-34
ksubB=1.38064852e-2
c=299792458.0
def Bplanck(T,v):
    y=((2*h*(v**3))/(c**2))/(np.exp((h*v)/(ksubB*T))-1)
    return y
a=archivo.readlines()# contiene en una matriz todas las lienas de "archivo"
espectro_T_cal=[]
espectro_T_dad=[]
T_cal=2685
T_obt=2725
for linea in a:
    v=300*float(linea[1:5])/1.25664e-22
    v2=300*float(linea[1:5])
    columna1.append(v2)#linea[1:5] contiene frecuencia
    columna4.append(float(linea[27:30]))#linea[27:30]contiene error de la frecuencia
    columna2.append(float(linea[9:15]))#linea[9:15] contiene espectro de la frecuencia
    espectro_T_cal.append(Bplanck(T_cal,v))
    espectro_T_dad.append(Bplanck(T_obt,v))
    
#ploteando todo como es debido...
fig, ax=plt.subplots()
ax.errorbar(columna1,columna2, xerr=columna4, label='Espectro obtenido por FIRAS')
plt.plot(columna1,espectro_T_cal,color='g',label='Espectro ecuacion de Planck  con temperatura obtenida')
plt.plot(columna1,espectro_T_dad,color='b',label='Espectro ecuacion de Planck  con temperatura=2.725')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Espectro [MJy/sr]')
plt.title('Grafico Frecuencia versus espectro con \n los errores rescpectivos de  FIRAS')
plt.legend()
plt.show()
archivo.close()
print(columna4)