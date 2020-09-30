class Libro:
    def __init__(self, titulo="", autor="", publicado="", editorial=""):
        self.__titulo = titulo
        self.__autor = autor
        self.__publicado = publicado
        self.__editorial = editorial

    def __str__(self):
        return(
"""Titulo: {0}
Autor: {1}
Publicado: {2}
Editorial: {3}""".format(
    self.__titulo,
    self.__autor, 
    self.__publicado, 
    self.__editorial)
        )