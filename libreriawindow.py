from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Slot
from ui_libreriawindow import Ui_MainWindow

from libreria_20B.libreria import Libreria, libreria
from libreria_20B.libro import Libro


class LibreriaWindow(QMainWindow):
    
    def __init__(self):
        super(LibreriaWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.libreria = Libreria()
        self.libreria = libreria

        self.ui.agregar_final_pushButton.clicked.connect(self.click_agregar_final)
        self.ui.agregar_inicio_pushButton.clicked.connect(self.click_agregar_inicio)
        self.ui.mostrar_pushButton.clicked.connect(self.click_mostrar_libros)

    @Slot()
    def click_agregar_final(self):
        titulo = self.ui.titulo_lineEdit.text()
        autor = self.ui.autor_lineEdit.text()
        publicado = self.ui.publicado_spinBox.value()
        editorial = self.ui.editorial_lineEdit.text()

        libro = Libro(titulo, autor, publicado, editorial)

        self.libreria.agregar_final(libro)
    
    @Slot()
    def click_agregar_inicio(self):
        titulo = self.ui.titulo_lineEdit.text()
        autor = self.ui.autor_lineEdit.text()
        publicado = self.ui.publicado_spinBox.value()
        editorial = self.ui.editorial_lineEdit.text()

        libro = Libro(titulo, autor, publicado, editorial)

        self.libreria.agregar_inicio(libro)

    @Slot()
    def click_mostrar_libros(self):
        self.libreria.mostrar()
