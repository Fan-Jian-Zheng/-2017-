# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main_1.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(466, 356)
        self.lineEdit_oldwebpassword = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_oldwebpassword.setGeometry(QtCore.QRect(120, 147, 331, 31))
        self.lineEdit_oldwebpassword.setObjectName("lineEdit_oldwebpassword")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 150, 100, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 75, 100, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.lineEdit_webpath = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_webpath.setGeometry(QtCore.QRect(120, 72, 331, 31))
        self.lineEdit_webpath.setObjectName("lineEdit_webpath")
        self.pushButton_modify = QtWidgets.QPushButton(Dialog)
        self.pushButton_modify.setGeometry(QtCore.QRect(150, 300, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_modify.setFont(font)
        self.pushButton_modify.setObjectName("pushButton_modify")
        self.pushButton_cancel = QtWidgets.QPushButton(Dialog)
        self.pushButton_cancel.setGeometry(QtCore.QRect(260, 300, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_cancel.setFont(font)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.lineEdit_webusername = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_webusername.setGeometry(QtCore.QRect(120, 109, 331, 31))
        self.lineEdit_webusername.setObjectName("lineEdit_webusername")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 112, 100, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 421, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.lineEdit_newpassword = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_newpassword.setGeometry(QtCore.QRect(120, 187, 331, 31))
        self.lineEdit_newpassword.setObjectName("lineEdit_newpassword")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 190, 100, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.lineEdit_newpassword2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_newpassword2.setGeometry(QtCore.QRect(120, 227, 331, 31))
        self.lineEdit_newpassword2.setObjectName("lineEdit_newpassword2")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(20, 230, 100, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.lineEdit_webpath, self.lineEdit_webusername)
        Dialog.setTabOrder(self.lineEdit_webusername, self.lineEdit_oldwebpassword)
        Dialog.setTabOrder(self.lineEdit_oldwebpassword, self.lineEdit_newpassword)
        Dialog.setTabOrder(self.lineEdit_newpassword, self.lineEdit_newpassword2)
        Dialog.setTabOrder(self.lineEdit_newpassword2, self.pushButton_modify)
        Dialog.setTabOrder(self.pushButton_modify, self.pushButton_cancel)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "密码通v1.0.0  修改服务"))
        self.label_2.setText(_translate("Dialog", "原密码："))
        self.label_3.setText(_translate("Dialog", "网址："))
        self.pushButton_modify.setText(_translate("Dialog", "修改"))
        self.pushButton_cancel.setText(_translate("Dialog", "取消"))
        self.label_5.setText(_translate("Dialog", "账号："))
        self.label_6.setText(_translate("Dialog", "修改系统"))
        self.label_4.setText(_translate("Dialog", "新密码："))
        self.label_7.setText(_translate("Dialog", "确认新密码："))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
