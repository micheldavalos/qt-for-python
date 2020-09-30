from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Slot
from ui_libreriawindow import Ui_MainWindow


class LibreriaWindow(QMainWindow):
    def __init__(self):
        super(LibreriaWindow, self).__init__()
        ui = Ui_MainWindow()
        ui.setupUi(self)
        ui.agregar_button.clicked.connect(self.click_agregar_buton)

    # TODO:
    # Slot del boton
    # # obtener cada lineEdit e imprimir
    @Slot()
    def click_agregar_buton(self):
        print("click")
