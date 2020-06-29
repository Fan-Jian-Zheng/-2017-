# -*- coding: utf-8 -*-
import sys, os, time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import ui.sub_ui_modify.ui_main_1
import Controller

def resource_path(relative):
    return os.path.join(
        os.environ.get(
            "_MEIPASS2",
            os.path.abspath(".")
        ),
        relative
    )

path1 = str(resource_path("logo.jpg"))
path1           = path1.replace("\\", "/")

class MyForm(QDialog):
    def __init__(self, parent=None,username="admin",password="admin"):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = ui.sub_ui_modify.ui_main_1.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton_modify.clicked.connect(self.funcMain)
        self.ui.pushButton_cancel.clicked.connect(self.funcExit)

        self.username = username
        self.password = password
        palette1 = QPalette()
        # palette1.setColor(self.backgroundRole(), QColor(192,253,123))   # 设置背景颜色
        palette1.setBrush(self.backgroundRole(), QBrush(QPixmap(r'.\res\blue_start.jpg')))   # 设置背景图片
        self.setPalette(palette1)
        self.setAutoFillBackground(True)                   

    def funcExit(self):
        self.ui.lineEdit_webpath.clear()
        self.ui.lineEdit_webusername.clear()
        self.ui.lineEdit_oldwebpassword.clear()
        self.ui.lineEdit_newpassword.clear()
        self.ui.lineEdit_newpassword2.clear()

    def funcMain(self):
        webpath = self.ui.lineEdit_webpath.text()
        webusername = self.ui.lineEdit_webusername.text()
        oldwebpassword = self.ui.lineEdit_oldwebpassword.text()
        newpassword = self.ui.lineEdit_newpassword.text()
        newpassword2 = self.ui.lineEdit_newpassword2.text()
        if (len(webpath)!=0) and  (len(webusername)!=0) and  (len(oldwebpassword)!=0) and  (len(newpassword)!=0) and  (len(newpassword2)!=0):
            if newpassword == newpassword2:
                controller = Controller.CDialogController()
                feedback = controller.changeWebPassword(self.username,webpath,webusername,oldwebpassword,newpassword)
                QMessageBox.information(None, "Information", "%s"%feedback)
            else:
                QMessageBox.critical(None, "Critical", "两次输入的新密码不一致，请重新操作。")
        else:
            QMessageBox.critical(None, "Critical", "信息不完整，请重新操作。")
  
# ------------------------code part:----------------------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())

