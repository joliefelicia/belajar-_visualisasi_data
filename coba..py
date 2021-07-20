def kali( number1,  number2):
    hasil=int(number1)*int(number2)
    print("hasil:  %f" %hasil)

nama=input("What is your name:")
print(nama)

num=int(input("How old are you:"))
print(num)

if (num<21):
    print("You are under 21")
else:
    print("You are older than me")

mathema = []
jumlah=int(input("How many your favourite mathematic topic? "))

for i in range (jumlah):
    print("What is your favourite mathematic topic:")
    nama=input(str)
    mathema.insert(i,nama)

for i in mathema:
    print(i)

def tambah( number1,  number2):
    hasil=int(number1)+int(number2)
    print("hasil:  %f" %hasil)

def bagi( number1,  number2):
    hasil=int(number1)/int(number2)
    print("hasil:  %f" %hasil)

def kurang( number1,  number2):
    hasil=int(number1)-int(number2)
    print("hasil:  %f" %hasil)

print("calculating two number, please type method")
met=input(str)
metode=met.lower()

if metode=='kali':
        number1=input("angka 1: ")
        number2=input("angka 2: ")
        kali(number1,number2)

elif metode=='bagi':
        number1=input("angka 1: ")
        number2=input("angka 2: ")
        bagi(number1,number2)

elif metode=='tambah':
        number1=input("angka 1: ")
        number2=input("angka 2: ")
        tambah(number1,number2)    

elif metode=='kurang':
        number1=input("angka 1: ")
        number2=input("angka 2: ")
        kurang(number1,number2)

else:
        print("method tidak ada")
"""
"""j=0
for i in range (0,5):
    for j in range (0,i+1):
        print("* ",end=' ')
    print(' ')

for i in range (0,5):
    j=0
    while j<=i:
        print("* ",end=' ')
        j+=1    
    print('\n')    

  







