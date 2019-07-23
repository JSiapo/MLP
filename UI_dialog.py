# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt
import resources_rc


class Ui_Dialog(object):
    S1 = 0
    S2 = 0
    S3 = 0
    S4 = 0
    S5 = 0
    theta = 0

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setStyleSheet("image: url(:/img/img/car.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 5, 1)
        self.chbox_S5 = QtWidgets.QCheckBox(Dialog)
        self.chbox_S5.setObjectName("chbox_S5")
        self.gridLayout.addWidget(self.chbox_S5, 0, 1, 1, 1)
        self.chbox_S4 = QtWidgets.QCheckBox(Dialog)
        self.chbox_S4.setObjectName("chbox_S4")
        self.gridLayout.addWidget(self.chbox_S4, 1, 1, 1, 1)
        self.chbox_S3 = QtWidgets.QCheckBox(Dialog)
        self.chbox_S3.setObjectName("chbox_S3")
        self.gridLayout.addWidget(self.chbox_S3, 2, 1, 1, 1)
        self.chbox_S2 = QtWidgets.QCheckBox(Dialog)
        self.chbox_S2.setObjectName("chbox_S2")
        self.gridLayout.addWidget(self.chbox_S2, 3, 1, 1, 1)
        self.chbox_S1 = QtWidgets.QCheckBox(Dialog)
        self.chbox_S1.setObjectName("chbox_S1")
        self.gridLayout.addWidget(self.chbox_S1, 4, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.txt_destino = QtWidgets.QLineEdit(Dialog)
        self.txt_destino.setObjectName("txt_destino")
        self.horizontalLayout.addWidget(self.txt_destino)
        self.gridLayout.addLayout(self.horizontalLayout, 5, 0, 1, 2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.btn_calcular = QtWidgets.QPushButton(Dialog)
        self.btn_calcular.setObjectName("btn_calcular")
        self.horizontalLayout_2.addWidget(self.btn_calcular)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_2, 6, 0, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.btn_calcular.clicked.connect(self.mensaje)
        self.chbox_S5.stateChanged.connect(self.check_S5)
        self.chbox_S4.stateChanged.connect(self.check_S4)
        self.chbox_S3.stateChanged.connect(self.check_S3)
        self.chbox_S2.stateChanged.connect(self.check_S2)
        self.chbox_S1.stateChanged.connect(self.check_S1)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.chbox_S5.setText(_translate("Dialog", "S5"))
        self.chbox_S4.setText(_translate("Dialog", "S4"))
        self.chbox_S3.setText(_translate("Dialog", "S3"))
        self.chbox_S2.setText(_translate("Dialog", "S2"))
        self.chbox_S1.setText(_translate("Dialog", "S1"))
        self.label_2.setText(_translate("Dialog", "DESTINO (-1, 0 1):"))
        self.btn_calcular.setText(_translate("Dialog", "Calcular"))

    def check_S5(self, state):
        if state == Qt.Checked:
            self.S5 = 1
        else:
            self.S5 = 0

    def check_S4(self, state):
        if state == Qt.Checked:
            self.S4 = 1
        else:
            self.S4 = 0

    def check_S3(self, state):
        if state == Qt.Checked:
            self.S3 = 1
        else:
            self.S3 = 0

    def check_S2(self, state):
        if state == Qt.Checked:
            self.S2 = 1
        else:
            self.S2 = 0

    def check_S1(self, state):
        if state == Qt.Checked:
            self.S1 = 1
        else:
            self.S1 = 0

    def calcular(self):
        from run import get_action
        entrada_i = [self.S5, self.S4, self.S3, self.S2, self.S1, self.theta]
        # entrada_i = [self.S1, self.S2, self.S3, self.S4, self.S5, self.theta]
        # print(get_action(entrada_i))
        print(entrada_i)
        return get_action(entrada_i)

    def mensaje(self, event):
        theta = self.txt_destino.text()

        print(self.theta)
        if theta is not "":
            self.theta = int(theta)
            QMessageBox.information(None, "Acción",
                                    "{}".format(self.calcular()))
            print("Respuesta", self.calcular())
        else:
            QMessageBox.critical(None, "Error",
                                 "Faltan datos")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
