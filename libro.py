class Libro:
    def __init__(self, titulo="", autor="", publicado=0, editorial=""):
        self.__titulo = titulo
        self.__autor = autor
        self.__publicado = publicado
        self.__editorial = editorial

    def __str__(self):
        return(
            'Titulo: ' + self.__titulo + '\n' +
            'Autor: ' + self.__autor + '\n' +
            'Publicado: ' + str(self.__publicado) + '\n' +
            'Editorial: ' + self.__editorial + '\n'
        )