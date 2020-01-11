from PySide2.QtWidgets import QMainWindow, QFileDialog
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
import json

class MainWindow(QMainWindow):
    libros = []
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.agregar)
        self.ui.pushButton_2.clicked.connect(self.mostrar)

        self.ui.actionGuardar.triggered.connect(self.guardar)
        self.ui.actionAbrir.triggered.connect(self.abrir)

    @Slot()
    def agregar(self):
        titulo = self.ui.titulo.text()
        autor = self.ui.autor.text()
        year = self.ui.spinBox.value()
        editorial = self.ui.editorial.text()

        print(titulo, autor, year, editorial)

        libro = {'titulo': titulo,
                 'autor': autor,
                 'year': year,
                 'editorial': editorial}
        print(libro)

        self.libros.append(libro)

        self.ui.titulo.clear()
        self.ui.autor.clear()
        self.ui.editorial.clear()

    @Slot()
    def mostrar(self):
        print(self.libros)

    @Slot()
    def guardar(self):
        ubicacion = QFileDialog.getSaveFileName(self, 'Guardar libros', '.', 'JSON (*.json)')
        print(ubicacion)

        with open(ubicacion[0], 'w') as archivo:
            json.dump(self.libros, archivo, indent=5)

    @Slot()
    def abrir(self):
        ubicacion = QFileDialog.getOpenFileName(self, 'Abrir archivo', '.', 'JSON (*.json)')

        with open(ubicacion[0], 'r') as archivo:
            self.libros = json.load(archivo)