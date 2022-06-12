"""
Crea una clase llamada Punto con sus dos coordenadas X e Y.
Añade un método constructor para crear puntos fácilmente. Si no se reciben una coordenada, su valor será cero.
Sobreescribe el método string, para que al imprimir por pantalla un punto aparezca en formato (X,Y)
Añade un método llamado cuadrante que indique a qué cuadrante pertenece el punto, teniendo en cuenta que si X == 0 e Y != 0 se sitúa sobre el eje Y, si X != 0 e Y == 0 se sitúa sobre el eje X y si X == 0 e Y == 0 está sobre el origen.
Añade un método llamado vector, que tome otro punto y calcule el vector resultante entre los dos puntos.
(Optativo) Añade un método llamado distancia, que tome otro punto y calcule la distancia entre los dos puntos y la muestre por pantalla. La fórmula es la siguiente:

Crea una clase llamada Rectangulo con dos puntos (inicial y final) que formarán la diagonal del rectángulo.
Añade un método constructor para crear ambos puntos fácilmente, si no se envían se crearán dos puntos en el origen por defecto.
Añade al rectángulo un método llamado base que muestre la base.
Añade al rectángulo un método llamado altura que muestre la altura.
Añade al rectángulo un método llamado area que muestre el area.
"""
#--------------1---------------------------
import math
class Punto:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
        
 #El método constructor es el que llama automáticamente a crear un objeto __init__   
    
    #metodo string
    def __str__(self):
        print(f'({self.x},{self.y})')
    def cuadrante(self):
        if self.x>0 and self.y>0:
            print('Pertenece al PRIMER CUADRANTE')
        elif self.x<0 and self.y>0:
            print('Pertenece al SEGUNDO CUADRANTE')
        elif self.x<0 and self.y<0:
            print('Pertenece al TERCER CUADRANTE')
        elif self.x>0 and self.y<0:
            print('Pertenece al CUARTO CUADRANTE')
        elif self.x!=0 and self.y==0:
            print('Pertenece al eje X')
        elif self.x==0 and self.y!=0:
            print('Pertenece al eje Y')
        else:
            print('Se encuentra en el origen de cordenadas')
    def vector(self,p):
        print(f'EL vector es ({p.x-self.x},{p.y-self.y})')

    def distancia(self,p):
        d=math.sqrt((p.x-self.x)**2+(p.y-self.y)**2)
        print(f'La distancia es {d}')



class Rectangulo:
    def __init__(self, a=Punto(), b=Punto()):
        self.a=a
        self.b=b    
    def base(self):
        self.base = abs(self.b.x - self.a.x)
        print(f"La base del rectángulo es {self.base}") 
    def altura(self):
        self.altura = abs(self.b.y - self.a.y)
        print(f"La altura del rectángulo es {self.altura}" )
    def area(self):
        self.base = abs(self.b.x - self.a.x)
        self.altura = abs(self.b.y - self.a.y)
        self.area = self.base * self.altura
        print("El área del rectángulo es {}".format( self.area ) )





A = Punto(2,3)
B = Punto(5,5)

A.__str__()
A.cuadrante()
A.vector(B)
A.distancia(B)

R= Rectangulo(A,B)

R.base()
R.altura()
R.area()





