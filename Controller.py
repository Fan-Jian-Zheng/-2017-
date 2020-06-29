# -*- coding: utf-8 -*-
import sqlite3
import sys, os, time

dbPath = r".\data\data.db"

class CDialogController(object):
    """docstring for ClassName"""
    def __init__(self, arg="none"):
        self.arg = arg

    def addItem(self,website="",webusername="",webpassword="",username="",uerpassword="",webpasswordKind="",passwordCode=""):
        conn = sqlite3.connect(dbPath)
        c = conn.cursor()
        c.execute("INSERT INTO webInfoTotal (website, webusername, webpassword, username, uerpassword ,webpasswordKind ,passwordCode) VALUES \
                   ( '%s', '%s', '%s', '%s', '%s', %d, '%s')" %(website,webusername,webpassword,username,uerpassword,webpasswordKind,passwordCode))
        conn.commit()
        conn.close()        

    def searchItem(self):
        conn = sqlite3.connect(dbPath)
        c = conn.cursor()

        c.execute('SELECT * FROM webInfoTotal')
        totalData = c.fetchall()
        print(totalData)

        conn.commit()
        conn.close()       

    def deleteItem(self,username=""):
        conn = sqlite3.connect(dbPath)
        c = conn.cursor()            
        c.execute("DELETE FROM webInfoTotal WHERE username = '%s'"%username)
        conn.commit()
        conn.close() 

    def searchItemByWebsite(self,website="",username=""):
        conn = sqlite3.connect(dbPath)
        c = conn.cursor()
        sql_cmd = "SELECT webusername,webpassword FROM webInfoTotal WHERE website like '%"+website+"%' AND username = '"+username+"'"
        print(sql_cmd)
        c.execute(sql_cmd)
        totalData = c.fetchall()
        conn.commit()
        conn.close()     
        return totalData    

    def searchItemByWebsiteUsername(self,website="",webusername="",username=""):
        conn = sqlite3.connect(dbPath)
        c = conn.cursor()
        c.execute("SELECT webusername,webpassword FROM webInfoTotal WHERE website = '%s' AND webusername='%s' AND username = '%s'"%(website,webusername,username))
        totalData = c.fetchall()
        conn.commit()
        conn.close()     
        return totalData  


    def changeLoginPassword(self,username="adimin",newpassword="adimin"):        
        conn = sqlite3.connect(dbPath)
        c = conn.cursor()            
        c.execute("UPDATE webInfoTotal SET uerpassword = '%s' WHERE username = '%s'"%(newpassword,username))
        conn.commit()
        conn.close()        

    def changeWebPassword(self,username="adimin",webpath="",webusername="",oldwebpassword="",newpassword=""): 
        conn = sqlite3.connect(dbPath)
        c = conn.cursor()                    
        c.execute("SELECT webpassword FROM webInfoTotal WHERE username = '%s' AND website = '%s'"%(username,webpath))
        oldwebpassworddb = c.fetchall()
        conn.commit()
        conn.close()     
        if len(oldwebpassworddb) == 0:
            return "数据库中不存在该网址信息！"
        elif oldwebpassworddb[0][0] != oldwebpassword:
            return "您输入的原密码不正确！"
        else:
            conn = sqlite3.connect(dbPath)
            c = conn.cursor()            
            c.execute("UPDATE webInfoTotal SET webpassword = '%s' WHERE username = '%s' AND website = '%s'"%(newpassword,username,webpath))
            conn.commit()
            conn.close()    
            return "恭喜您密码修改完成！"

# ------------------------code part:----------------------------------
if __name__ == "__main__":
    myapp = CDialogController()
    #myapp.addItem()
    # myapp.changeLoginPassword("1","789")
    # username = '1'
    # webpath = 'www.baidu.com'
    # webusername = 'xiaoming'
    # oldwebpassword = '123456'
    # newpassword = '789'
    # feedback = myapp.changeWebPassword(username,webpath,webusername,oldwebpassword,newpassword)
    # print(feedback)
    # myapp.searchItemByWebsite()
    # aa = myapp.searchItemByWebsiteUsername("www.baidu.com","xiaoming")
    # print(aa)
    myapp.deleteItem("1")