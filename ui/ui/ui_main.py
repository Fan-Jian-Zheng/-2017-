# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(381, 367)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 40, 341, 281))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(30, 20, 261, 191))
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(17, 70, 51, 41))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 24, 51, 41))
        self.label.setObjectName("label")
        self.input_1 = QtWidgets.QLineEdit(self.groupBox)
        self.input_1.setGeometry(QtCore.QRect(80, 30, 151, 31))
        self.input_1.setObjectName("input_1")
        self.input_2 = QtWidgets.QLineEdit(self.groupBox)
        self.input_2.setGeometry(QtCore.QRect(80, 72, 151, 31))
        self.input_2.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.input_2.setObjectName("input_2")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(30, 120, 91, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(130, 120, 91, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_3.setGeometry(QtCore.QRect(30, 20, 241, 221))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(39, 67, 51, 41))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(26, 25, 51, 41))
        self.label_6.setObjectName("label_6")
        self.input_4 = QtWidgets.QLineEdit(self.groupBox_3)
        self.input_4.setGeometry(QtCore.QRect(80, 72, 151, 31))
        self.input_4.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_4.setObjectName("input_4")
        self.input_3 = QtWidgets.QLineEdit(self.groupBox_3)
        self.input_3.setGeometry(QtCore.QRect(80, 30, 151, 31))
        self.input_3.setObjectName("input_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 160, 91, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.input_5 = QtWidgets.QLineEdit(self.groupBox_3)
        self.input_5.setGeometry(QtCore.QRect(81, 117, 151, 31))
        self.input_5.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.input_5.setObjectName("input_5")
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setGeometry(QtCore.QRect(19, 111, 51, 41))
        self.label_7.setObjectName("label_7")
        self.tabWidget.addTab(self.tab_2, "")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 8, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 381, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "登录系统："))
        self.label_2.setText(_translate("MainWindow", "密码："))
        self.label.setText(_translate("MainWindow", "用户名："))
        self.pushButton.setText(_translate("MainWindow", "登录"))
        self.pushButton_3.setText(_translate("MainWindow", "注册"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "登录界面"))
        self.groupBox_3.setTitle(_translate("MainWindow", "注册系统："))
        self.label_5.setText(_translate("MainWindow", "密码："))
        self.label_6.setText(_translate("MainWindow", "用户名："))
        self.pushButton_2.setText(_translate("MainWindow", "注册"))
        self.label_7.setText(_translate("MainWindow", "确认密码："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "注册界面"))
        self.label_3.setText(_translate("MainWindow", "密码通用户登录"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

