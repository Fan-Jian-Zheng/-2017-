::ʹ��˵����
::    ����������ļ��������Զ���.ui�ļ�ת����.py�ļ�
::    ʹ��Ҫ�󣺱��뽫.ui�ļ������������ȥ�����س�������Զ�����ͬ����.py�ļ�
::���ߣ�Jimmy.wei

@echo off
cd /d %~dp0
::set/p name=����������Python�ļ�����: 
pyuic5 -x ui_main.ui -o ui_main.py
::pause
