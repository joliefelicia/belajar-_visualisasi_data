import numpy as np
import pandas as pd


"""#mengenal tipe data series
label=['a','b','c']
data=[10,20,30]
array=np.array(data)
k={'a':10,'b':20,'c':30}

#pd.Series(data=data)
#print(pd.Series(data=data, index=label));pd.Series(data,label)
#print(pd.Series(k))
series1=pd.Series([1,2,3,4,5],['Yogyakarta','Bantul','Kulonprogo','Gunung Kidul','Sleman'])
series2=pd.Series([1,2,3,4,5],['Yogyakarta','Bantul','Kulonprogo','Gunung Kidul','Sleman'])
print(series2)

#memanggil no indeks
print(series2['Yogyakarta'])

#menjumlahkan no indeks dari 2 series, jika gaad ahasil maka di output nan
print (series1+series2)"""


#mengenal tipe data dataframe
from numpy.random import randn
df=pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])#pd.DataFrame(randn(baris,kolom),nama baris bentuk list,nama kolom bentuk list)

#memanggil kolom untuk mengecek tipe ketik type
#print(df['W'])

# untuk mengakses beberapa kolom dibuat 2 list
#print(df[['W','X']])

#menambahkan kolom baru isinya adalah pertambahan nilai kolom w dan z
df['baru']=df['W']+df['Z']

#menghapus kolom menggunakan drop, untuk menghapus kolom perlu ditulis axis=1, ini hilang sementara
#df.drop('baru',axis=1)

#menghapus premanen
df.drop('baru',axis=1, inplace=True)

#melihat baris dan kolom
#print(df.shape)

#melihat baris tertentu
#print(df.loc['A'])

#melihat baris tertentu menggunakan indeks
#print(df.iloc[0])

print('baris a kolom y',df.loc['A','Y'])
print(' ')
print('baris a baris b kolom x kolom y');print(df.loc[['A','B'],['X','Y']])
print(' ')
print('baris 2 kolom 4',df.iloc[1,3])
print(' ')
print('mengambil matriks dari 2 baris awal dan 2 kolom awal');print(df.iloc[:2,:2])
print(' ')
print('mengambil matriks dari 2 baris awal dan 2 kolom yaitu '
'kolom ke-1 dan kolom ke-3 ');print(df.iloc[:2,[1,3]])

#conditional selection
print(df>0)#menambilkan boolean
print(' ')
boolean =df>0
print('yang false diganti nan atau bisa print(df[df>0])');print(df[boolean])#yang false diganti nan atau bisa print(df[df>0])
print(' ')
print('akan menampilkan baris di kolom w yang kondisinya memenuhi yaitu diatas 0');print(df[df['W']>0])#akan menampilkan baris di kolom w yang kondisinya memenuhi yaitu diatas 0
print(' ')
print(df[df['W']>0]['X'])#jika ingin menampilkan di kolom tertentu
print(' ')
print(df[df['W']>0][['X','Z']])
print(' ')
print(df[(df['X']<0) & (df['W']>0)]) #membuat 2 kondisi pada 2 kolom
print(' ')
new_data ='ai ue eo ab cd'.split()
df['new']=new_data
print(df)
print(df.set_index('new'))
print(' ')

#multilevel index
ind1=['A1','A1','A1','A2','A2','A2']
ind2=[1,2,3,1,2,3]
index=list(zip(ind1,ind2))#menggabungkan antar list
print(index)
print(' ')
index=pd.MultiIndex.from_tuples(index)#perbedaan dalam output menjadi kebawah
print(index)
df=pd.DataFrame(randn(6,2),index, ['A','B'])
print('Menampilkan baris A1 bagian no 1');print(df.loc['A1'].loc[1])
print(' ')
print('Menampilkan baris A2 bagian no 1 kolom B');print(df.loc['A1'].loc[1]['B'])
print(' ')
df.index.names=['Kelompok','Nomor']
print(df)
print(' ')
print(df.xs(2,level='Nomor'))#df.xs(key,axis=0,level=,drp_level=,bool)
print(' ')
#Missing Data
d={'A':[1,2,np.nan],'B':[6,np.nan,np.nan],'C':[1,2,5]}
df=pd.DataFrame(d)
print(df)
print(' ')
print('menampilkan isi tabel yang gaada na');print(df.dropna())#jika ingin kolom, tambahkan axis=1 didalam kurung dropna
print(' ')
print('Mengisi nilai na dengan angka 1');print(df.fillna(value=1))
print(' ')
print('Menggantikan nan dengan angka rata2 dari nilai yang bukan nan dikolom A');print(df['A'].fillna(value=df['A'].mean()))
print(' ')
#df=pd.read_csv('example')
  