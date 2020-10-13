# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_libreria.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(264, 305)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.autor_lineEdit = QLineEdit(self.groupBox)
        self.autor_lineEdit.setObjectName(u"autor_lineEdit")

        self.gridLayout.addWidget(self.autor_lineEdit, 1, 1, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.editorial_lineEdit = QLineEdit(self.groupBox)
        self.editorial_lineEdit.setObjectName(u"editorial_lineEdit")

        self.gridLayout.addWidget(self.editorial_lineEdit, 3, 1, 1, 1)

        self.publicado_spinBox = QSpinBox(self.groupBox)
        self.publicado_spinBox.setObjectName(u"publicado_spinBox")
        self.publicado_spinBox.setMinimum(2000)
        self.publicado_spinBox.setMaximum(2020)
        self.publicado_spinBox.setValue(2020)

        self.gridLayout.addWidget(self.publicado_spinBox, 2, 1, 1, 1)

        self.titulo_lineEdit = QLineEdit(self.groupBox)
        self.titulo_lineEdit.setObjectName(u"titulo_lineEdit")

        self.gridLayout.addWidget(self.titulo_lineEdit, 0, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.agregar_pushButton = QPushButton(self.groupBox)
        self.agregar_pushButton.setObjectName(u"agregar_pushButton")

        self.gridLayout.addWidget(self.agregar_pushButton, 4, 0, 1, 2)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 264, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Mis Libros", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Libro", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Autor:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"T\u00edtulo:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Publicado:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Editorial", None))
        self.agregar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
    # retranslateUi

