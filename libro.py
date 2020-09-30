class Libro:
    def __init__(self, titulo="", autor="", publicado="", editorial=""):
        self.__titulo = titulo
        self.__autor = autor
        self.__publicado = publicado
        self.__editorial = editorial

    def __str__(self):
        return(
            'Titulo: ' + self.__titulo + '\n' +
            'Autor: ' + self.__titulo + '\n' +
            'Publicado: ' + self.__publicado + '\n' +
            'Editorial: ' + self.__editorial
        )