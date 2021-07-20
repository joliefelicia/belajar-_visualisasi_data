from matplotlib.transforms import Bbox
import numpy as np
import matplotlib.pyplot as plt
"""
	1. Membuat data
	2. Membuat plot
	3. Menampilkan plot
"""
#legend berfungsi memberitahu garis grafik apa
# 1. Membuat data (sin(2wt + theta))
# camel case
def sinusGenerator(amplitudo,frekuensi,tAkhir,theta):
	t = np.arange(0,tAkhir,0.1)
	y = amplitudo * np.sin(2*frekuensi*t + np.deg2rad(theta))
	return t,y

# 2. Membuat plot
#legend tipe pertama

t1,y1 = sinusGenerator(1,1,4,0)
dataplot1=plt.plot(t1,y1, label="sin(0)")
plt.text(2,0.5,'sin(0)')#plt.text(posisi x, posisi y, text)
plt.legend()


t2,y2 = sinusGenerator(1,1,4,30)
dataplot2=plt.plot(t2,y2,label="sin(30)")
plt.legend()

t3,y3 = sinusGenerator(1,1,4,60)
dataplot3=plt.plot(t3,y3,label="sin(60)")
plt.legend()

t4,y4 = sinusGenerator(1,1,4,90)
dataplot4=plt.plot(t4,y4,label="sin(90)")
plt.legend()

#4. menyimpan grafk dalam png
#plt.savefig(trmpat penyimpanan, format)
plt.savefig('F:\python\grafik_sinus_generator.png')


#legend tipe kedua
"""t1,y1 = sinusGenerator(1,1,4,0)
dataplot1=plt.plot(t1,y1, label="sin(0)")
plt.legend(loc="upper right")"""

#legend tipe ketiga
"""t1,y1 = sinusGenerator(1,1,4,0)
dataplot1=plt.plot(t1,y1, label="sin(0)")
plt.legend(loc="upper center",bbox_to_anchor=(0.5,-0.05))"""
#bbox_to_achor=(posisi x,posisi y)

#legend tipe keempat
"""plt.figure(1)
ax=plt.subplot(111) #subplot merupakan gambar grafik
t1,y1 = sinusGenerator(1,1,4,0)
dataplot1=plt.plot(t1,y1, label="sin(0)")
box=ax.get_position()
ax.set_position([box.x0,box.y0,box.width*0.7,box.height])
plt.legend(loc="upper center",bbox_to_anchor=(1.2,1))"""

#settings axis minimum dan maximum
#plt.axis([xmin,xmas,ymin,ymax])
plt.axis([0,4,-2,2])


#membuat judul
judul="Grafik Sinusoidal\n"
rumus=r'$ \mathcal{y} = A.sin(2 \omega t + \theta) $' +'\n'
amplitudo='$ A= $'+str(1)+'cm, '
frekuensi=r'$ \omega= $'+str(1)+r'$ \mathit{Hz}$'+', '
theta=r'$ \theta = $'+str(0)+r'$^{0}$'
plt.title(judul+rumus+amplitudo+frekuensi+theta)

#membuat label
plt.xlabel("waktu(detik)")
plt.ylabel("magnitudo(cm)")

#settings properties
plt.setp(dataplot1,color='g',linestyle='-',linewidth=1)
plt.setp(dataplot2,color='r',linestyle='--',linewidth=0.75)
plt.setp(dataplot3,color='b',linestyle='-',linewidth=1)
plt.setp(dataplot4,color='c',linestyle='--',linewidth=0.75)

#4. menyimpan grafk dalam png
#plt.savefig(trmpat penyimpanan, format)
plt.savefig('F:\python\grafik_sinus_generator.png')
# 3. Menampilkan plot
plt.show()



# "."	point
# ","	pixel
# "o"	circle
# "v"	triangle_down
# "^"	triangle_up
# "<"	triangle_left
# ">"	triangle_right
# "1"	tri_down
# "2"	tri_up
# "3"	tri_left
# "4"	tri_right
# "8"	octagon
# "s"	square
# "p"	pentagon
# "P"	plus (filled)
# "*"	star
# "h"	hexagon1
# "H"	hexagon2
# "+"	plus
# "x"	x
# "X"	x (filled)
# "D"	diamond
# "d"	thin_diamond
# "|"	vline
# "_"	hline