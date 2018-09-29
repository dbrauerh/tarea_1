import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mp 
import math
from astropy import constants as cte
N=10
errores=[]
Enes=[]
error=10
while(error>(10e-6)):
    N1=N
    epsilon=1/N*10
    amasb_n1=np.linspace(epsilon,(np.pi/2.0)-epsilon,2*N+1)
    amasb_n2=np.linspace((np.pi/2.0)-epsilon,np.pi/2.0,2*N1+1)
    amasb_n3=np.linspace(0,epsilon,2*N1+1)

    delta1=(amasb_n1[1]-amasb_n1[0])
    delta2=(amasb_n2[1]-amasb_n2[0])
    delta3=(amasb_n3[1]-amasb_n3[0])

    def I_planck(x):
        y=((np.tan(x)**3)*(1/(np.cos(x)**2)))/(np.exp(np.tan(x))-1)
        return y


    sumatoria1=0
    sumatoria2=0
    sumatoria3=0
    sumatoria4=0
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
        sumatoria3+=2*delta2*I_planck(amasb_n2[2*n+1])
        n+=1
        k3+=1
    n=1
    k4=0
    while n<N1:
        sumatoria4+=2*delta3*I_planck(amasb_n3[2*n+1])
        n+=1
        k4+=1

    integral1=(delta1/3.0)*(I_planck(amasb_n1[0])+I_planck(amasb_n1[2*N])+4*sumatoria1+2*sumatoria2)
    integral2=sumatoria3
    integral3=sumatoria4
    integral_tot=(integral1+integral2+integral3)
    error=np.fabs(integral_tot-((np.pi**4)/15.0))
    Enes.append(n)
    N+=1
    #print(error)
    errores.append(error)
T=2725
P=(2*cte.h/(cte.c**2))*((cte.k_B*T/cte.h)**4)*integral_tot
print('valor: '+str(P))
#print(integral_tot)
#print(error)
plt.plot(Enes,errores)
plt.yscale('log')
plt.show()