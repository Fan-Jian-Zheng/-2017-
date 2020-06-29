# -*- coding: utf-8 -*-
import sys, os, time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import ui.sub_ui_main.ui_main_1
import configparser
import sub_search
import sub_modify
import sub_save
import Controller

path1 = r".\data\recorde.ini"



class MyForm(QDialog):
    def __init__(self, parent=None,username="admin",password="admin"):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = ui.sub_ui_main.ui_main_1.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton_save.clicked.connect(self.funcSave)
        self.ui.pushButton_search.clicked.connect(self.funcSearch)
        self.ui.pushButton_modify.clicked.connect(self.funcModify)

        self.ui.pushButton_modifypassword.clicked.connect(self.modifypassword)
        self.username = username
        self.password = password
        self.updateUserInfo()

        self.ui.pushButton_deleteAccount.clicked.connect(self.delCount)
        if self.username == "admin":
            self.ui.pushButton_deleteAccount.setVisible(1)
        else:
            self.ui.pushButton_deleteAccount.setVisible(0)

        palette1 = QPalette()
        # palette1.setColor(self.backgroundRole(), QColor(192,253,123))   # 设置背景颜色
        palette1.setBrush(self.backgroundRole(), QBrush(QPixmap(r'.\res\blue_start.jpg')))   # 设置背景图片
        self.setPalette(palette1)
        self.setAutoFillBackground(True)               


    def updateUserInfo(self):
        self.ui.label_username.setText("%s"%self.username)       
        self.ui.label_password.setText("%s"%self.password)           

    def modifypassword(self):
        resetFlag = 0
        text, ok = QInputDialog.getText(None, '重置登录密码', '请输入您的新密码？')
        if ok and (len(text)!=0):
            text1, ok1 = QInputDialog.getText(None, '重置登录密码', '请再次输入您的新密码？')
            if ok1 and (len(text1)!=0):   
                if text == text1:
                    QMessageBox.information(None, "Information", "恭喜您，密码重置成功！")
                    self.password = text
                    self.updateUserInfo()
                    resetFlag = 1
                else:
                    QMessageBox.critical(None, "Critical", "两次输入的密码不一致，请重新操作。")
        if resetFlag == 1:
            config = configparser.ConfigParser()
            config.read(r'%s'%path1)
            config.set("information", str(self.username), str(self.password))
            config.write(open(r'%s'%path1, "w"))

            controller = Controller.CDialogController()
            controller.changeLoginPassword(self.username,self.password)

    def delCount(self):
        fp = open(r"%s"%path1)
        lines = []
        for line in fp: 
            if line.find("=") != -1:
                lines.append(line[0:line.find("=")-1])
        fp.close()
        showstr= "已存在的账户：\n"
        for item in lines:
            #if item != "totalswitch" and item != self.username:
            if item != "totalswitch" :
                showstr = showstr + "    " + str(item) + "\n"
        showstr = showstr + "\n" + "请输入您要删除的账户："
        text, ok = QInputDialog.getText(None, '重置登录密码', '%s'%showstr)
        if ok and (len(text)!=0):
            if text in lines:
                config = configparser.ConfigParser()
                config.read(r'%s'%path1)
                config.remove_option('information',text)
                config.write(open(r'%s'%path1, "w"))
                
                controller = Controller.CDialogController()
                controller.deleteItem(text)                

                QMessageBox.information(None, "Information", "恭喜您，账户删除成功！")
            else:
                QMessageBox.critical(None, "Critical", "您输入的账户信息不存在！")            

    def funcSave(self):
        mainCode = sub_save.MyForm(None,self.username,self.password)  #-------启动主程序界面入口---
        mainCode.show()
        mainCode.exec_()   
 
    def funcSearch(self):
        mainCode = sub_search.MyForm(None,self.username,self.password)  #-------启动主程序界面入口---
        mainCode.show()
        mainCode.exec_()    

    def funcModify(self):
        mainCode = sub_modify.MyForm(None,self.username,self.password)  #-------启动主程序界面入口---
        mainCode.show()
        mainCode.exec_()            
# ------------------------code part:----------------------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)    
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())

