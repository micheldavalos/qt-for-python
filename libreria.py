from libro import Libro

class Libreria:
    def __init__(self):
        self.__libros = []
    
    def agregar_final(self, libro:Libro):
        self.__libros.append(libro)
    
    def agregar_inicio(self, libro:Libro):
        self.__libros.insert(0, libro)

    def mostrar(self):
        for libro in self.__libros:
            print(libro)

# libreria = Libreria()

# l1 = Libro(titulo='Programación', autor='Joyanes', publicado=2000, editorial='Pearson') 
# l2 = Libro(titulo='Programación en C++', autor='Deitel', publicado=2020, editorial='Mc Graw Hill') 
# l3 = Libro(titulo='Programación en Python', autor='Guido', publicado=2015, editorial='RA-MA') 

# libreria.agregar_inicio(l1)
# libreria.agregar_final(l2)
# libreria.agregar_inicio(l3)
# libreria.mostrar()