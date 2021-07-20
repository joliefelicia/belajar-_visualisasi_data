import matplotlib.pyplot as plt
import numpy as py
#ax.bar(x, height, width, bottom, align)
#numpy.arange([start, ]stop, [step, ], dtype=None) -> numpy.ndarray
fig1 = plt.figure()
ax = fig1.add_axes([0.1,0.2,0.7,0.7])
#add_axes[left, bottom, width, height]
langs = ['C', 'C++', 'Java', 'Python', 'PHP']
colors=['r','g','b','c','m']
students = [23,17,35,29,12]
ax.set_title('Jumlah murid pengguna bahasa tersebut')
p=ax.bar(langs,students,color=colors)
ax.bar_label(p)
plt.xlabel("program language")
plt.ylabel("students")
ax=plt.gca()
ax.spines['top'].set_color(('none'))
ax.spines['right'].set_color(('none'))


cm=1/2*54
#fig2 = plt.subplots(figsize =(2*cm, 2*cm))#figsize(width,height)
fig2=plt.figure()
ax = fig2.add_axes([0.1,0.2,0.7,0.7])
# set height of bar
IT = [12, 30, 1, 8, 22]
ECE = [28, 6, 16, 5, 10]
CSE = [29, 3, 24, 25, 17]

# Set position of bar on X axis
barwidth=0.25
br1 = py.arange(len(IT))
br2 = [x + barwidth for x in br1]
br3 = [x + barwidth for x in br2]

# Make the plot
pa=plt.bar(br1, IT, color ='r', width = barwidth,
		edgecolor ='grey', label ='IT')
pb=plt.bar(br2, ECE, color ='g', width = barwidth,
		edgecolor ='grey', label ='ECE')
pc=plt.bar(br3, CSE, color ='b', width = barwidth,
		edgecolor ='grey', label ='CSE')

# Adding Xticks
plt.xlabel('Branch', fontweight ='bold', fontsize = 15)
plt.ylabel('Students passed', fontweight ='bold', fontsize = 15)
plt.xticks([r + barwidth for r in range(len(IT))],
		['2015', '2016', '2017', '2018', '2019'])
plt.title('Jumlah mahasiswa tiap jurusan')
ax.bar_label(pa)
ax.bar_label(pb)
ax.bar_label(pc)
plt.legend()


ax=plt.gca()
ax.spines['top'].set_color(('none'))
ax.spines['right'].set_color(('none'))


menMeans = (20, 35, 30, 35, 27)
womenMeans = (25, 32, 34, 20, 25)
ind = py.arange(5) # the x locations for the groups
width = 0.35
fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.8,0.8])
p1=ax.bar(ind, menMeans, width, color='r')
p2=ax.bar(ind, womenMeans, width,bottom=menMeans, color='b')
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
labels=['G1', 'G2', 'G3', 'G4', 'G5']
ax.set_xticks(py.arange(len(labels)))
ax.set_xticklabels(labels)
ax.set_yticks(py.arange(0, 81, 10))
ax.legend(labels=['Men', 'Women'])

# label with label type
ax.bar_label(p1,label_type='center',color='w')
ax.bar_label(p2,label_type='center',color='w')
ax.bar_label(p2)
ax=plt.gca()
ax.spines['top'].set_color(('none'))
ax.spines['right'].set_color(('none'))
plt.show()




