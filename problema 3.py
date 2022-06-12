"""Definir una clase llamada “CIRCULO” la cual contenga un atributo inicializador radio. La clase
“CIRCULO” debe tener un método que puede calcular el área en utilizando el atributo radio."""

import math

class Circulo:
    # atributos por defecto
    pi=math.pi

    # atributos de inicializacion
    def __init__(self, radio) :
        self.radio=radio
    pass

    # metodos

    def calcula_area(self):
        a=math.pi*self.radio*self.radio
        print(f'El area es:{a}')
    pass


c1 = Circulo(3)
c1.calcula_area()


