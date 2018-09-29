import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mp 
import math
archivo=open("columnas.txt","r")
columna1=[]
columna2=[]
columna4=[]
a=archivo.readlines()
for linea in a:
    columna1.append((300e8)*float(linea[1:5]))
    columna4.append(float(linea[27:30]))
    columna2.append(float(linea[9:15]))

fig, ax=plt.subplots()
ax.errorbar(columna1,columna2,yerr=columna4)
plt.show()
archivo.close()
print(columna4)