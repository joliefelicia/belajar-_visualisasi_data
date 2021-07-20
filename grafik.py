import matplotlib.pyplot as plt
import numpy as np



#membuat lingkaran
pi=np.pi
sudut=np.linspace(0,2*pi,100)
radius=5
#np.linspace(start, stop, num).astype(int)

x=radius*np.cos(sudut)
y=radius*np.sin(sudut)

#1 membuat data
#2. membuat plot
#3. menampilkan plot
#membuat plot banyak akan membuat banyak garis

#1. membuat data


#2. membuat plot
#plt.plot(x,y,y2)

#3. menampilkan plot
#plt.show()

#1 membuat data (sin(2wt + theta))
#camel case
def sinusgenerator(amplitudo,frekuensi,takhir,theta):
    t=np.arange(0,takhir,0.1)
    y=amplitudo*np.sin(2*frekuensi*t+np.deg2rad(theta))
    return t,y

#2. membuat plot
t1,y1=sinusgenerator(1,1,4,0)
plt.plot(t1,y1,'b-o')

t2,y2=sinusgenerator(1,1,4,30)
plt.plot(t2,y2,'r')#r artinya red untuk menambahkan warna garis, untuk garis putus2 jadi r--

t3,y3=sinusgenerator(1,1,4,60)
plt.plot(t3,y3,'g--')
#3. menampilkan plot
plt.show()