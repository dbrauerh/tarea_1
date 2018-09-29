import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mp 
import math
"""computador con capacidad float64"""
h=np.logspace(-1,-6,6,10)
y1=[]
y2=[]
x=1.728
y=math.sin(1.728)
n=0
while n<len(h):
    delta=h[n]
    y1.append((-(math.cos(x+delta))+math.cos(x))/delta)
    y2.append((math.cos(x+2*delta)-8*math.cos(x+delta)+8*math.cos(x-delta)-math.cos(x-2*delta))/(12.0*delta))
    n+=1
n=0
plt.plot(h,y1,color='y')
plt.plot(h,y2,color='b')

"""cambiando la capacidad a float32"""
h2=np.logspace(-1,-6,6,10)
y12=[]
y22=[]
x2=np.float32(1.728)
y_1=np.float32(math.sin(1.728))
n=0
while n<len(h):
    delta=np.float32(h[n])
    y12.append(np.float32((-(np.float32(math.cos(x2+delta)))+
    np.float32(math.cos(x2)))/delta))

    y22.append(np.float32((np.float32(math.cos(x2+2*delta))-
    8*np.float32(math.cos(x2+delta))+8*np.float32(math.cos(x2-delta))
    -np.float32(math.cos(x2-2*delta)))/(12.0*delta)))
    n+=1
n=0
plt.plot(h2,y12,color='g')
plt.plot(h2,y22,color='k')
plt.show()   
