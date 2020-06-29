# -*- coding: utf-8 -*-
import sys, os, time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import ui.sub_ui_search.ui_main_1
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
        self.ui = ui.sub_ui_search.ui_main_1.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton_search0.clicked.connect(self.funcMain)
        self.ui.pushButton_cancel0.clicked.connect(self.funcExit)
        self.ui.pushButton_search1.clicked.connect(self.funcMain1)
        self.ui.pushButton_cancel1.clicked.connect(self.funcExit1)
        self.username = username
        self.password = password        

        palette1 = QPalette()
        # palette1.setColor(self.backgroundRole(), QColor(192,253,123))   # 设置背景颜色
        palette1.setBrush(self.backgroundRole(), QBrush(QPixmap(r'.\res\blue_start.jpg')))   # 设置背景图片
        self.setPalette(palette1)
        self.setAutoFillBackground(True)           
  
    def funcMain(self):
        website = self.ui.lineEdit_website0.text()
        if len(website) != 0:
            controller = Controller.CDialogController()
            feedback = controller.searchItemByWebsite(website,self.username)
            if len(feedback) != 0:
                resutl = "搜索结果：\n   用户名：   密码： \n"
                for item in feedback:
                    resutl = resutl + str(item) + "\n"
                QMessageBox.information(None, "Search Result", "%s"%resutl)

            else:
                QMessageBox.critical(None, "Critical", "数据库中无此项数据。")

    def funcExit(self):
        self.ui.lineEdit_website0.clear()

    def funcMain1(self):
        website = self.ui.lineEdit_website1.text()
        webusername = self.ui.lineEdit_username.text()
        if len(website) != 0:
            controller = Controller.CDialogController()
            feedback = controller.searchItemByWebsiteUsername(website,webusername,self.username)
            if len(feedback) != 0:
                resutl = "搜索结果：\n   用户名：   密码： \n"
                for item in feedback:
                    resutl = resutl + str(item) + "\n"
                QMessageBox.information(None, "Search Result", "%s"%resutl)

            else:
                QMessageBox.critical(None, "Critical", "数据库中无此项数据。")
        
    def funcExit1(self):
        self.ui.lineEdit_website1.clear()
        self.ui.lineEdit_username.clear()

# ------------------------code part:----------------------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())

