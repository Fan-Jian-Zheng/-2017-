# -*- coding: utf-8 -*-

import ui.ui.ui_main
import sys, os, time
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
import configparser
import sub_main


StyleSheet = '''

QPushButton {
    /*border: none; 去掉边框*/
}

QPushButton#pushButton_save{
    background-color: #76EE00; /*背景颜色*/
    max-height: 48px;
    border-radius: 10px; /*圆角*/
}
QPushButton#pushButton_search{
    background-color: #76EE00; /*背景颜色*/
    max-height: 48px;
    border-radius: 10px; /*圆角*/
}
QPushButton#pushButton_modify{
    background-color: #76EE00; /*背景颜色*/
    max-height: 48px;
    border-radius: 10px; /*圆角*/
}
QPushButton#pushButton_modifypassword{
    background-color: #76EE00; /*背景颜色*/
    max-height: 48px;
    border-radius: 10px; /*圆角*/
}
QPushButton#pushButton_deleteAccount{
    background-color: #76EE00; /*背景颜色*/
    max-height: 48px;
    border-radius: 10px; /*圆角*/
}

QPushButton#pushButton_search0{
    background-color: #76EE00; /*背景颜色*/
    max-height: 48px;
    border-radius: 10px; /*圆角*/
}
QPushButton#pushButton_search1{
    background-color: #76EE00; /*背景颜色*/
    max-height: 48px;
    border-radius: 10px; /*圆角*/
}

QPushButton#pushButton_cancel0{
    background-color: #ff0000; /*背景颜色*/
    max-height: 48px;
    border-radius: 10px; /*圆角*/
}
QPushButton#pushButton_cancel1{
    background-color: #ff0000; /*背景颜色*/
    max-height: 48px;
    border-radius: 10px; /*圆角*/
}
QPushButton#pushButton_exit{
    background-color: #ff0000; /*背景颜色*/
    max-height: 48px;
    border-radius: 10px; /*圆角*/
}
QPushButton#pushButton_cancel{
    background-color: #ff0000; /*背景颜色*/
    max-height: 48px;
    border-radius: 10px; /*圆角*/
}

'''

path1 = r".\data\recorde.ini"

class MyForm(QMainWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = ui.ui.ui_main.Ui_MainWindow()
        self.ui.setupUi(self)
        self.move(500, 250)
        self.setWindowTitle("密码通v2.0.0")
        self.sBar = self.statusBar() 
        self.sBar.showMessage("欢迎使用密码通v2.0.0")
        self.ui.tabWidget.setCurrentIndex(0)         
# -------设置信号槽------
        self.ui.pushButton.clicked.connect(self.login)  # ---设置登录函数---
        self.ui.pushButton_2.clicked.connect(self.writein)# ---设置注册函数---
        self.ui.pushButton_3.clicked.connect(self.next) # ----设置自动注册函数---
# -------编辑输入框特性-----
        self.ui.input_5.setEchoMode(QLineEdit.Password) # ----设置密码模式---
        self.ui.input_4.setEchoMode(QLineEdit.Password) # ----设置密码模式---
        self.ui.input_2.setEchoMode(QLineEdit.Password) # ----设置密码模式---      

        palette1 = QPalette()
        palette1.setColor(self.backgroundRole(), QColor(192,253,123))   # 设置背景颜色
        # palette1.setBrush(self.backgroundRole(), QBrush(QPixmap(r'.\res\blue_start.jpg')))   # 设置背景图片
        self.setPalette(palette1)
        self.setAutoFillBackground(True)                  

    def next(self):
        self.ui.tabWidget.setCurrentIndex(1)   

    def login(self):
        self.name1 = self.ui.input_1.text() #--获取信息--
        self.password = self.ui.input_2.text() #---获取密码---
        config = configparser.ConfigParser()
        config.readfp(open(r'%s'%path1))
        try:
            a = config.get("information", str(self.name1)) # ---读取数据库信息---
        except:
            QMessageBox.information(None, "Information", "您未注册，请先进行注册后登陆")
            return None
        else:
            if str(self.password) == str(a):
                QMessageBox.information(None, "Information", "登陆成功，欢迎您！")
                self.get_thread1 = thread1() 
                self.get_thread1.sendData.connect(self.show_mainwindow) #---启动主程序界面----
                self.get_thread1.start()
                self.hide()   # ---隐藏登录界面--
            else:
                self.ui.input_2.clear()
                QMessageBox.information(None, "Information", "密码错误,请重新输入！")
                config = configparser.ConfigParser()
                config.read(r'%s'%path1)
                config.set("information", "totalSwitch", "0")
                config.write(open(r'%s'%path1, "w"))

    def show_mainwindow(self,status):
        if(status==1):
            mainCode = sub_main.MyForm(None,self.name1,self.password)  #-------启动主程序界面入口---
            mainCode.show()
            mainCode.exec_()          

    def writein(self):
        name2 = self.ui.input_3.text()# ----获取用户名----
        password1 = self.ui.input_4.text() # ----获取密码---
        password2 = self.ui.input_5.text() #-----获取密码a----

        if str(password1) == str(password2):
            config = configparser.ConfigParser()
            config.read(r'%s'%path1)
            config.set("information", str(name2), str(password1))
            config.write(open(r'%s'%path1, "w")) # ------写入数据库
            QMessageBox.information(None, "Information", "恭喜您，注册成功！")
            self.ui.tabWidget.setCurrentIndex(0) 
        else:
            self.ui.input_4.clear()
            self.ui.input_5.clear()
            QMessageBox.information(None, "Information", "两次密码输入不一致,无法注册")


class thread1(QThread):
    sendData = pyqtSignal(int)
    def __init__(self):
        QThread.__init__(self)
        self.flag_exit = 0

    def __del__(self):
        self.wait()

    def run(self):
        try:
            self.sendData.emit(1)
        except Exception as e:
            print("%s---%s" % (sys._getframe().f_lineno,e))


# -----------------------code input----------------------------------------
def mycodestart():
    app = QApplication(sys.argv)
    app.setStyleSheet(StyleSheet)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    mycodestart()
# --------------------------------------------------------------------------