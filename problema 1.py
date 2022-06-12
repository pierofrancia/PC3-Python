"""Implemente un programa que solicite al usuario una fracción, con
formato X/Y, donde cada uno de X e Y es un número entero, y luego
muestra, como un porcentaje redondeado al número entero más
cercano, donde se indicará la cantidad de combustible en el
tanque. Se debe tener en cuenta los siguientes casos:
- Colocar E en caso X/Y sea menor a 1% del total
- Colocar F en caso X/Y sea mayor a 99%.
- En otro caso, devolver el valor en porcentaje %
También debe tomar en cuenta los siguientes casos:
- X y Y deben ser números enteros
- X debe ser mayor o igual a Y, y Y != 0
De no cumplirse estos casos, se debe volver a preguntar al usuario. Asegúrese de detectar
cualquier excepción como ValueError o ZeroDivisionError.
Ejemplos:
- Input: 4/0 Acción: Volver a preguntar al usuario dada la excepción ZeroDivisionError
- Input 1.5/3 Acción: Error dado que solo se permiten números enteros ValueError
- Input 5/4 Acción: Volver a preguntar al usuario
- Input 3/4 Output: 75%
- Input 4/4: Output F
Nota: Le será de utilidad aplicar
try:
...
except ValueError:
...
except ZeroDivisionError:                """

def main():
    msg= str(input('Ingrese una fracción: '))
    x,y=msg.split('/')
    while x<=y :
        try:
            x=int(x)
            y=int(y)
            d=x/y
        except ValueError:
            print("Error dado que solo se permiten números enteros")
            return main()
        break
    while x>y:
        try:
            x=int(x)
            y=int(y)
            d=x/y
            return main()
        except ValueError:
            print("Error dado que solo se permiten números enteros")
            return main()
        except ZeroDivisionError:
            print('ZeroDivisionError')
            return main() 
        break
    d=x/y
    porcentaje=d*100
    porcentaje=int(porcentaje)
    if 1>=d>0.99:
       print('F')
    elif d<0.01:
       print('E')
    else:
        print(f'{porcentaje}%')    
    
main()


        