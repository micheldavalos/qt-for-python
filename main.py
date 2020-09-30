from PySide2.QtWidgets import QApplication
# from mainwindow import MainWindow
from libreriawindow import LibreriaWindow
import sys

app = QApplication()
window = LibreriaWindow()
window.show()

sys.exit(app.exec_())