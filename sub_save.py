# -*- coding: utf-8 -*-
import sys, os, time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import ui.sub_ui_save.ui_main_1
import Controller
import base64
import Encryption


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
        self.ui = ui.sub_ui_save.ui_main_1.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton_save.clicked.connect(self.funcMain)
        self.ui.pushButton_exit.clicked.connect(self.funcExit)
        self.username = username
        self.password = password        
        self.passwordCode = "None"
        self.ui.comboBox.addItem("二进制编码加密")
        self.ui.comboBox.addItem("base64编码加密")
        self.ui.comboBox.addItem("ascii编码加密")
        self.ui.comboBox.addItem("自定义密码加密")
        self.ui.comboBox.setCurrentIndex(-1)
        self.ui.comboBox.currentIndexChanged.connect(self.comboxRespone)  

        palette1 = QPalette()
        # palette1.setColor(self.backgroundRole(), QColor(192,253,123))   # 设置背景颜色
        palette1.setBrush(self.backgroundRole(), QBrush(QPixmap(r'.\res\blue_start.jpg')))   # 设置背景图片
        self.setPalette(palette1)
        self.setAutoFillBackground(True)   
        self.webpassword = ""

    def comboxRespone(self):
        self.webpassword = self.ui.lineEdit_password.text()    
        index = self.ui.comboBox.currentIndex()
        if index == 0:
            #二进制编码加密：
            self.ui.lineEdit_password.setText(encode(self.webpassword))
        elif index == 1:
            #base64编码加密：base64.b64encode(bytes("hello",encoding='utf-8')) 
            self.ui.lineEdit_password.setText(str(base64.b64encode(bytes(self.webpassword,encoding='utf-8'))))
        elif index == 2:
            #ascii编码加密：list(map(ord, name))
            self.ui.lineEdit_password.setText(str(list(map(ord, self.webpassword))))
        elif index == 3:
            text, ok = QInputDialog.getText(None, '自定义加密方式：', '请输入您的加密吗？')
            if ok and (len(text)!=0):
                self.passwordCode = text
                ps = Encryption.ENCRYTION(str(self.webpassword).encode(), str(self.passwordCode).encode())
                content = ps.Encode()
                self.ui.lineEdit_password.setText(str(content))
    
    def funcMain(self):
        webpath = self.ui.lineEdit_web.text()        
        webusername = self.ui.lineEdit_username.text()
        if len(self.webpassword) ==0:
            self.webpassword = self.ui.lineEdit_password.text()            
        passwordkind = self.ui.comboBox.currentIndex()

        if len(webpath) != 0 and  len(webusername) != 0 and len(self.webpassword) != 0:                
            controller = Controller.CDialogController()
            controller.addItem(webpath,webusername,self.webpassword,self.username,self.password,passwordkind,self.passwordCode)  
            QMessageBox.information(None, "Information", "恭喜您，信息录入成功！")      
        
    def funcExit(self):
        pass

def encode(s):
    return ' '.join([bin(ord(c)).replace('0b', '') for c in s])
 
def decode(s):
    return ''.join([chr(i) for i in [int(b, 2) for b in s.split(' ')]])
  
# ------------------------code part:----------------------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())

