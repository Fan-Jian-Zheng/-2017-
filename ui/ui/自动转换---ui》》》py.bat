::使用说明：
::    这个批处理文件是用来自动将.ui文件转换成.py文件
::    使用要求：必须将.ui文件的名称输入进去，按回车键后会自动生成同名的.py文件
::作者：Jimmy.wei

@echo off
cd /d %~dp0
::set/p name=请输入生成Python文件名称: 
pyuic5 -x ui_main.ui -o ui_main.py
::pause
