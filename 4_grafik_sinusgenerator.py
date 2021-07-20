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

fig, axs = plt.subplots(2,2,constrained_layout=True)
fig.suptitle('Grafik Sinus generator')

def sinusGenerator(amplitudo,frekuensi,tAkhir,theta):
	t = np.arange(0,tAkhir,0.1)
	y = amplitudo * np.sin(2*frekuensi*t + np.deg2rad(theta))
	return t,y


t1,y1 = sinusGenerator(1,1,4,0)
axs[0,0].plot(t1,y1,'r')
axs[0,0].set_title("sin 0")


t2,y2 = sinusGenerator(1,1,4,30)
axs[0,1].plot(t2,y2,'b')
axs[0,1].set_title("sin 30")

t3,y3 = sinusGenerator(1,1,4,60)
axs[1,0].plot(t3,y3,'g')
axs[1,0].set_title("sin 60")

t4,y4 = sinusGenerator(1,1,4,90)
axs[1,1].plot(t4,y4,'k')
axs[1,1].set_title("sin 90")

for ax in axs.flat:
    ax.set(xlabel='waktu(detik)', ylabel='magnitudo(cm)')

# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax in axs.flat:
    ax.label_outer()


plt.show()
