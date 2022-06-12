def suma(a,b):
  try:
    print("La suma es: " + float(a + b))
  except TypeError:
    print("Tipo de dato no válido")

def resta(a,b):
  try:
    print("La resta es: " + float(a - b))
  except TypeError:
    print("Tipo de dato no válido")

def multiplicacion(a,b):
  try:
    print("La multiplicación es: " + float(a * b))
  except TypeError:
    print("Tipo de dato no válido")

def division(a,b):
  try:
    print("La división es: " + float(a / b))
  except TypeError:
    print("Tipo de dato no válido")
  except ZeroDivisionError:
    print("No es posible dividir entre cero")