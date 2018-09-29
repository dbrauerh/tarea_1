import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mp 
import math
from astropy import constants as cte
archivo=open("columnas.txt","r")
columna1=[]
columna2=[]
a=archivo.readlines()
for linea in a:
    columna1.append(300*float(linea[1:5]))
    columna2.append(float(linea[9:15]))

area=0
n=0
while n < (len(columna2)-1):
    delta=columna1[n+1]-columna1[n]
    area+=delta*(columna2[n]+columna2[n+1])/2.0
    n+=1

print(area)
archivo.close()