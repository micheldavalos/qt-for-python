from .libro import Libro
import json
from pprint import PrettyPrinter

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

    def __str__(self):
        return "".join(
            str(libro) + "\n" for libro in self.__libros
        )

    def __len__(self):
        return len(self.__libros)
        
    def __iter__(self):
        self.cont = 0

        return self

    def __next__(self):
        if self.cont < len(self.__libros):
            libro = self.__libros[self.cont]
            self.cont += 1
            return libro
        else:
            raise StopIteration

    
    def guardar(self, ubicacion):
            try:
                with open(ubicacion, 'w') as archivo:
                    # prueba = {
                    #     'key1': 'string',
                    #     'key2': 10,
                    #     56: 10.5
                    # }
                    # pruebas = [prueba, prueba, prueba]
                    libros_dict = [libro.to_dict() for libro in self.__libros]
                    json.dump(libros_dict, archivo, indent=5)
                    return 1
            except:
                return 0

    def recuperar(self, ubicación):
        try:
            with open(ubicación, 'r') as archivo:
                libros_dict = json.load(archivo)
                PrettyPrinter().pprint(libros_dict)
                self.__libros = [Libro(**libro) for libro in libros_dict]
                # **libro = (convertir dict en parametros para una funcion)
                return 1
        except:
            return 0
            


l01 = Libro(titulo="Programación", autor="Deitel", publicado=2020, editorial="Pearson")
l02 = Libro("Python", "Guido", "2010", "Planeta")
libreria = Libreria()
# libreria.agregar_final(l01)
# libreria.agregar_inicio(l02)
# libreria.agregar_inicio(l01)
# libreria.mostrar()