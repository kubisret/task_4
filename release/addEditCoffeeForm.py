# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(370, 322)
        self.lineEdit_sort = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_sort.setGeometry(QtCore.QRect(10, 30, 351, 21))
        self.lineEdit_sort.setObjectName("lineEdit_sort")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 101, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 111, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_stepen = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_stepen.setGeometry(QtCore.QRect(10, 80, 351, 21))
        self.lineEdit_stepen.setObjectName("lineEdit_stepen")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 110, 121, 16))
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(10, 130, 351, 26))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 160, 111, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit_text = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_text.setGeometry(QtCore.QRect(10, 180, 351, 21))
        self.lineEdit_text.setObjectName("lineEdit_text")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 210, 111, 16))
        self.label_5.setObjectName("label_5")
        self.lineEdit_cene = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_cene.setGeometry(QtCore.QRect(10, 230, 351, 21))
        self.lineEdit_cene.setObjectName("lineEdit_cene")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(10, 260, 111, 16))
        self.label_6.setObjectName("label_6")
        self.lineEdit_v = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_v.setGeometry(QtCore.QRect(60, 260, 301, 21))
        self.lineEdit_v.setObjectName("lineEdit_v")
        self.pushButton_ok = QtWidgets.QPushButton(Dialog)
        self.pushButton_ok.setGeometry(QtCore.QRect(10, 290, 351, 32))
        self.pushButton_ok.setObjectName("pushButton_ok")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Название сорта"))
        self.label_2.setText(_translate("Dialog", "Степень обжарки"))
        self.label_3.setText(_translate("Dialog", "Молотый/в зернах"))
        self.comboBox.setItemText(0, _translate("Dialog", "молотый"))
        self.comboBox.setItemText(1, _translate("Dialog", "в зернах"))
        self.label_4.setText(_translate("Dialog", "Описание вкуса"))
        self.label_5.setText(_translate("Dialog", "Цена"))
        self.label_6.setText(_translate("Dialog", "Объем"))
        self.pushButton_ok.setText(_translate("Dialog", "Сохранить"))