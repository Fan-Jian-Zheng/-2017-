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
        Dialog.resize(376, 223)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 341, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton_save = QtWidgets.QPushButton(Dialog)
        self.pushButton_save.setGeometry(QtCore.QRect(30, 80, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_save.setFont(font)
        self.pushButton_save.setObjectName("pushButton_save")
        self.pushButton_search = QtWidgets.QPushButton(Dialog)
        self.pushButton_search.setGeometry(QtCore.QRect(140, 80, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_search.setFont(font)
        self.pushButton_search.setObjectName("pushButton_search")
        self.pushButton_modify = QtWidgets.QPushButton(Dialog)
        self.pushButton_modify.setGeometry(QtCore.QRect(250, 80, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_modify.setFont(font)
        self.pushButton_modify.setObjectName("pushButton_modify")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 160, 101, 16))
        self.label_2.setObjectName("label_2")
        self.label_username = QtWidgets.QLabel(Dialog)
        self.label_username.setGeometry(QtCore.QRect(130, 160, 150, 16))
        self.label_username.setObjectName("label_username")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 180, 101, 16))
        self.label_4.setObjectName("label_4")
        self.label_password = QtWidgets.QLabel(Dialog)
        self.label_password.setGeometry(QtCore.QRect(130, 180, 150, 16))
        self.label_password.setObjectName("label_password")
        self.pushButton_modifypassword = QtWidgets.QPushButton(Dialog)
        self.pushButton_modifypassword.setGeometry(QtCore.QRect(30, 120, 131, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_modifypassword.setFont(font)
        self.pushButton_modifypassword.setObjectName("pushButton_modifypassword")
        self.pushButton_deleteAccount = QtWidgets.QPushButton(Dialog)
        self.pushButton_deleteAccount.setGeometry(QtCore.QRect(220, 120, 131, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_deleteAccount.setFont(font)
        self.pushButton_deleteAccount.setObjectName("pushButton_deleteAccount")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "密码通v1.0.0"))
        self.label.setText(_translate("Dialog", "密码通v1.0.0"))
        self.pushButton_save.setText(_translate("Dialog", "新增数据"))
        self.pushButton_search.setText(_translate("Dialog", "查询"))
        self.pushButton_modify.setText(_translate("Dialog", "修改"))
        self.label_2.setText(_translate("Dialog", "欢迎尊敬的用户："))
        self.label_username.setText(_translate("Dialog", "admin"))
        self.label_4.setText(_translate("Dialog", "您的登录密码是："))
        self.label_password.setText(_translate("Dialog", "admin"))
        self.pushButton_modifypassword.setText(_translate("Dialog", "修改登录密码"))
        self.pushButton_deleteAccount.setText(_translate("Dialog", "删除已有账户"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

