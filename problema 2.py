"""Cree un programa que solicite al usuario una lista de calificaciones separadas por comas. Divida
la cadena en calificaciones individuales y almacénelas en una lista para luego convertir cada
calificación en un entero. Deberá utilizar una sentencia try/except para informar al usuario
cuando los valores introducidos no puedan ser convertidos debido a un error de tipeo o
formato. (Los métodos de cadena le serán de utilidad)"""

lista=[]
def main():
    r=str(input('Desea ingresar una nota:'))
    while r=='si':
        n=(input('Ingrese una nota: '))
        try:
            n=int(n) 
            lista.append(n)
            return main()  
        except:
            print("Los valores introducidos no puedan ser convertidos debido a un error de tipeo o formato")
            return main()  
        break
    while r=='no':
        print(lista)
        break

main()
