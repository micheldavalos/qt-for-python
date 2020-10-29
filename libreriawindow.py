from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem
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


        self.ui.mostrar_tabla_pushButton.clicked.connect(self.mostrar_tabla)
        self.ui.buscar_pushButton.clicked.connect(self.buscar_libro_titulo)   


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
    
    @Slot()
    def mostrar_tabla(self):
        self.ui.tabla.setColumnCount(4)
        headers = ['Título', 'Autor', 'Publicado', 'Editorial']
        self.ui.tabla.setHorizontalHeaderLabels(headers)

        self.ui.tabla.setRowCount(len(self.libreria))

        row = 0
        for libro in self.libreria:
            titulo_widget = QTableWidgetItem(libro.titulo)
            autor_widget = QTableWidgetItem(libro.autor)
            publicado_widget = QTableWidgetItem(str(libro.publicado))
            editorial_widget = QTableWidgetItem(libro.editorial)

            # titulo_widget = QTableWidgetItem(libro['titulo'])
            # autor_widget = QTableWidgetItem(libro['autor'])
            # publicado_widget = QTableWidgetItem(str(libro['publicado']))
            # editorial_widget = QTableWidgetItem(libro['editorial'])

            self.ui.tabla.setItem(row, 0, titulo_widget)
            self.ui.tabla.setItem(row, 1, autor_widget)
            self.ui.tabla.setItem(row, 2, publicado_widget)
            self.ui.tabla.setItem(row, 3, editorial_widget)

            row += 1
    
    @Slot()
    def buscar_libro_titulo(self):
        titulo = self.ui.buscar_lineEdit.text()
        encontrado = False

        for libro in self.libreria:
            if titulo == libro.titulo:
                self.ui.tabla.clear()
                self.ui.tabla.setRowCount(1)

                titulo_widget = QTableWidgetItem(libro.titulo)
                autor_widget = QTableWidgetItem(libro.autor)
                publicado_widget = QTableWidgetItem(str(libro.publicado))
                editorial_widget = QTableWidgetItem(libro.editorial)

                self.ui.tabla.setItem(0, 0, titulo_widget)
                self.ui.tabla.setItem(0, 1, autor_widget)
                self.ui.tabla.setItem(0, 2, publicado_widget)
                self.ui.tabla.setItem(0, 3, editorial_widget)

                encontrado = True
        
        if not encontrado:
            QMessageBox.warning(
                self,
                "Atención",
                f'El libro con el título "{titulo}" no fue encontrado'
            )

        