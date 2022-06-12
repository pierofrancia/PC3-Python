import random

def lista_random():
  numeros=[]
  print("Lista de números random:")
  for i in range(20):
    numeros.append(random.randint(0,100))
    print(numeros[i], end=" ")
  print("Lista de números random ordenada:")
  numeros.sort()
  for i in range(20):
    print(numeros[i], end=" ")