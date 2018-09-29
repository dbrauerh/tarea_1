#descargando la librerias necesarias
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mp 
import math
from astropy import constants as cte
archivo=open("columnas.txt","r")#abriendo el archivo que contiene datos de FIRAS 
columna1=[]#guardara las frecuencias
columna2=[]#guardara los espectros
columna4=[]#guardara errores
a=archivo.readlines()# contiene en una matriz todas las lienas de "archivo"
vluz=3e8
for linea in a:
    columna1.append(100*vluz*float(linea[1:5]))#linea[1:5] contiene frecuencia
    columna4.append(float(linea[27:30]))#linea[27:30]contiene error de la frecuencia
    columna2.append(float(linea[9:15]))#linea[9:15] contiene espectro de la frecuencia
#ploteando todo como es debido...
fig, ax=plt.subplots()
ax.errorbar(columna1,columna2,yerr=columna4, label='Frecuencia [Hz]')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Espectro [MJy/sr]')
plt.title('Grafico Frecuencia versus espectro con \n los errores rescpectivos de  FIRAS')
plt.legend()
plt.show()
archivo.close()
print(columna4)