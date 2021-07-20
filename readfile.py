import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

cm=1/2*54
fig=plt.figure(figsize =(2*cm, 2*cm))
#add_axes[left, bottom, width, height]
ax=fig.add_axes([0.1,0.2,0.8,0.7])
table=pd.read_csv("https://storage.googleapis.com/dqlab-dataset/penduduk_gender_head.csv")
table.head()
x_label = table['NAMA KELURAHAN']
p=plt.bar(x=np.arange(len(x_label)),height=table['LAKI-LAKI WNI'])
plt.title('Jumlah penduduk laki - laki  wni di berbagai kelurahan')
plt.xticks(np.arange(len(x_label)),x_label,rotation=90)
plt.bar_label(p,padding=5,rotation=90)
ax=plt.gca()
ax.spines['top'].set_color(('none'))
ax.spines['right'].set_color(('none'))


cm=1/2*54
fig2=plt.figure(figsize =(2*cm, 2*cm))
#add_axes[left, bottom, width, height]
ax=fig2.add_axes([0.2,0.05,0.7,0.9])
table=pd.read_csv("https://storage.googleapis.com/dqlab-dataset/penduduk_gender_head.csv")
table.head()
plt.title('Jumlah penduduk laki -laki dan perempuan wni di berbagai kelurahan')
x_label = table['NAMA KELURAHAN']
p1=plt.barh(y=np.arange(len(x_label)),width=table['LAKI-LAKI WNI'])
p2=plt.barh(y=np.arange(len(x_label)),width=table['PEREMPUAN WNI'],left=table['LAKI-LAKI WNI'])
plt.yticks(np.arange(len(x_label)),x_label)
ax.bar_label(p1,label_type='center')
ax.bar_label(p2,label_type='center')
ax.bar_label(p2)
ax.legend(labels=['Men', 'Women'],loc="lower right")
plt.show()
