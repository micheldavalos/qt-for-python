from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox
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

        self.ui.actionAbrir.triggered.connect(self.action_abrir_archivo)
        self.ui.actionGuadar.triggered.connect(self.action_guardar_archivo)


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
        self.ui.salida_plainTextEdit.clear()
        self.ui.salida_plainTextEdit.insertPlainText(str(libreria))

    @Slot()
    def action_abrir_archivo(self):
        ubicacion = QFileDialog.getOpenFileName(
            self,
            'Abrir Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        if self.libreria.recuperar(ubicacion):
            QMessageBox.information(
                self,
                'Éxito',
                'Se abrió correctamente el archivo ' + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                'Error',
                'No fue posible abrir el archivo ' +  ubicacion
            )


    @Slot()
    def action_guardar_archivo(self):
        ubicacion = QFileDialog.getSaveFileName(
            self,
            'Guardar Archivo',
            ".",
            "JSON (*.json)"
        )[0]
        # print(ubicacion)
        if self.libreria.guardar(ubicacion):
            QMessageBox.information(
                self,
                'Éxito',
                'Se guardó el archivo en ' + ubicacion                
            )
        else:
            QMessageBox.critical(
                self,
                'Error',
                'No se pudo crear el archivo ' + ubicacion
            )
    