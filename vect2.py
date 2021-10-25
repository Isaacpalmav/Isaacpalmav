import random

contador=0

lista=[0,0,0,0,0,0,0,0,0,0] 

lista[0] = random.randint(1,10)
lista[1] = random.randint(1,10)
lista[2] = random.randint(1,10)
lista[3] = random.randint(1,10)
lista[4] = random.randint(1,10)
lista[5] = random.randint(1,10)
lista[6] = random.randint(1,10)
lista[7] = random.randint(1,10)
lista[8] = random.randint(1,10)
lista[9] = random.randint(1,10)

for i in lista:
    if(i%2==0):
        contador=contador+1
   
print(lista)

print("Los números pares que hay en la lista son: ", contador)
