import numpy as np
import matplotlib.pyplot as plt


major=['IT','Manajemen','Accounting','psychology','Art']
values =[12,55,4,32,14]
colors=['r','g','b','c','m']
explode=[0,0,0,0,0]
labels=list(major)
plt.pie(values,colors=colors,labels=labels,explode=explode,autopct='%1.1f%%',startangle=90)
#plt.pie(sizes, explode=None, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)   #line 240
#plt.pie(sizes, labels, colors)
plt.axis('equal')#equal aspect ratio ensures that pie is drawn as a circle
plt.title("student major")
plt.show()