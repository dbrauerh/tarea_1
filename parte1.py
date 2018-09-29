import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mp 
import math
"""computador con capacidad float64"""
h=np.logspace(-1,-6,6,10)#creando un vector que tendra distintos delta
#para evaluar en los dos metodos
y1=[]#matriz que almacenara los resultados del primer metodo
y2=[]#matriz que almacenara los resultados del segundo metodo
x=1.728
y=math.sin(1.728)
error1m=[]#matriz que almacenara los errores del primer metodo
error2m=[]#matriz que almacenara los errores del segundo metodo
n=0
while n<len(h):#evaluendo h en cada metodo y reemplazando los resultados en y1 e y2
    delta=h[n]
    y1.append((-(math.cos(x+delta))+math.cos(x))/delta)#primer metodo, mas simple con orden O(h)
    y2.append((math.cos(x+2*delta)-8*math.cos(x+delta)+8*math.cos(x-delta)-math.cos(x-2*delta))/(12.0*delta))
    #segundo metodo, mas complicado entregado en el enunciado con errores de orden O(h^4)
    error1m.append(np.fabs(y1[n]-y))#obteniendo los errores
    error2m.append(np.fabs(y2[n]-y))#obteniendo los errores
    n+=1
n=0
error1=y1[len(y1)-1]-y
error2=y2[len(y2)-1]-y
#ploteando los errores
plt.subplot(1,2,1)
plt.ylabel('error')
plt.xlabel('delta')
plt.title('Errores usando metodo con \n error orden O(delta) y O(delta^4) con float 64:')
plt.plot(h,error1m,color='y',label='Metodo error orden O(delta)')
plt.plot(h,error2m,color='b',label='Metodo error orden O(delta^4)')
plt.legend()
plt.xscale('log')
plt.yscale('log')

"""cambiando la capacidad a float32"""
# en esta parte se hara lo mismo que en el paso anterior pero con float 32
h2=np.logspace(-1,-6,6,10)
y12=[]
y22=[]
x2=np.float32(1.728)
y_1=np.float32(math.sin(1.728))
error12m=[]
error22m=[]
n=0
while n<len(h):
    delta=np.float32(h[n])
    y12.append(np.float32((-(np.float32(math.cos(x2+delta)))+
    np.float32(math.cos(x2)))/delta))

    y22.append(np.float32((np.float32(math.cos(x2+2*delta))-
    8*np.float32(math.cos(x2+delta))+8*np.float32(math.cos(x2-delta))
    -np.float32(math.cos(x2-2*delta)))/(12.0*delta)))

    error12m.append(np.float32(np.fabs(y12[n]-np.float32(y))))
    error22m.append(np.float32(np.fabs(y22[n]-np.float32(y))))
    n+=1
n=0
error12=y12[len(y12)-1]-y
error22=y22[len(y22)-1]-y
plt.subplot(1,2,2)
plt.ylabel('error')
plt.xlabel('delta')
plt.title('Errores usando metodo con \n error orden O(delta) y O(delta^4) con float 32:')
plt.plot(h2,error12m,color='g',label='Metodo error orden O(delta)')
plt.plot(h2,error22m,color='k',label='Metodo error orden O(delta^4)')
plt.legend()
plt.xscale('log')
plt.yscale('log')
plt.show() 
print('Error usando metode orden O(h^1) y float 64: '+str(error1))
print('Error usando metode orden O(h^4) y float 64: '+str(error2))
print('Error usando metode orden O(h^1) y float 32: '+str(error12))
print('Error usando metode orden O(h^4) y float 32: '+str(error22))
