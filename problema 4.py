"""Definir una clase llamada “RECTANGULO” que puede ser construida por los atributos largo y
ancho. La clase “RECTANGULO” debe tener un método que puede calcular el área utilizando los
atributos de la clase."""
class rectangulo:
    # atributos por defecto

    # atributos de inicializacion
    def __init__(self, alto, ancho):
        self.alto=alto
        self.ancho=ancho
    pass
    # metodos

    def area(self):
        a=self.alto*self.ancho
        print(f'El area es:{a}')
    pass
rect1 = rectangulo(3,4)
rect1.area()