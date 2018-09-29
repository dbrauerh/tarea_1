#importando todas las librearias necesarias
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mp 
import math
from astropy import constants as cte
N=10#numero de divisiones que se hara inicialmente
errores=[]#matriz donde se guardaran los errores
Enes=[]#matriz donde se guardara las diviciones que se hizo en cada ciclo
error=10# estableciendo un error inicial para poder entrar en el while
while(error>(10e-6)):
    N1=N
    epsilon=1/N*10
    amasb_n1=np.linspace(epsilon,(np.pi/2.0)-epsilon,2*N+1)#creando divisiones entre 0 y pi/2 sin tocar los puntos extremos
    amasb_n2=np.linspace((np.pi/2.0)-epsilon,np.pi/2.0,2*N1+1)#creando divisiones entre pi/2 - epsilon y pi/2
    amasb_n3=np.linspace(0,epsilon,2*N1+1)#creando divisiones entre 0 y epsilon

    delta1=(amasb_n1[1]-amasb_n1[0])#calculando el delta que existe en la primera division
    delta2=(amasb_n2[1]-amasb_n2[0])#calculando el delta que existe en la segunda division
    delta3=(amasb_n3[1]-amasb_n3[0])#calculando el delta que existe en la tercera division
    #ahora escribiendo la integral normalizada la cual se calculara entre 0 y pi/2
    def I_planck(x):
        y=((np.tan(x)**3)*(1/(np.cos(x)**2)))/(np.exp(np.tan(x))-1)
        return y
    

    sumatoria1=0#almacenara sumatoria de los puntos impares de "amasb_n1"
    sumatoria2=0#alamcenara sumatoria de los puntos pares de "amasb_n1"
    sumatoria3=0#almacenara sumatoria para calcular la integral entre  pi/2 - epsilon y pi/2
    sumatoria4=0#alnacenara sumatoria para calcular la integral entre 0 y pi/2
    n=0
    k1=0
    while n<N:
        sumatoria1+=I_planck(amasb_n1[2*n+1])
        n+=1
        k1+=1
    n=1
    k2=0
    while n<N:
        sumatoria2+=I_planck(amasb_n1[2*n])
        n+=1
        k2+=1
    n=0
    k3=0
    while n<N1:
        sumatoria3+=2*delta2*I_planck(amasb_n2[2*n+1])# metodo simple de rectangulos tomando ptos medios entre extremos de intervalos
        n+=1
        k3+=1
    n=1
    k4=0
    while n<N1:
        sumatoria4+=2*delta3*I_planck(amasb_n3[2*n+1])#metodos simples de rectangulos tomando ptos medios entre extremos de intervalo
        n+=1
        k4+=1

    integral1=(delta1/3.0)*(I_planck(amasb_n1[0])+I_planck(amasb_n1[2*N])+4*sumatoria1+2*sumatoria2)#Metodo de SIMPSON
    integral2=sumatoria3
    integral3=sumatoria4
    integral_tot=(integral1+integral2+integral3)#calculando integral total entre 0 y pi/2
    error=np.fabs(integral_tot-((np.pi**4)/15.0))#calculnado el error de la integral
    Enes.append(N)#guardando el numero de divisiones usadas
    N+=1
    #print(error)
    errores.append(error)
T=2725
P=(2*cte.h/(cte.c**2))*((cte.k_B*T/cte.h)**4)*integral_tot#calculando la potencia final
print('valor: '+str(P))
#print(integral_tot)
#print(error)
#Graficando como es debido...
plt.plot(Enes,errores)
plt.xlabel('Numero de divisiones realizadas')
plt.ylabel('Error')
plt.title('Error de integral de frecuencia usando metodo de Simpson \n mas metodo de rectangulos en los bordes')
plt.yscale('log')
plt.show()
#calculando la T con el resultado que nos da en la parte 3, obtenemos:
T=np.sqrt(np.sqrt(938989.8*(cte.c**2)/(2*cte.h*integral_tot)))*(cte.h/cte.k_B)
print('Temperatura obtenida: '+str(T))