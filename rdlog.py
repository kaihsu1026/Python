import sys
import time
from PyQt5 import QtCore
from PyQt5.QtWidgets import QListWidget, QTextEdit, QApplication, QDialog, QGridLayout, QLabel, QLineEdit, QMainWindow, QPushButton, QTableWidget, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QEventLoop, QTimer, QThread, pyqtSignal, Qt
import paramiko
import datetime

now = datetime.datetime.now().strftime("%Y%m%d")    #設定當下時間(年月日)
local_path = ( './rdlog.log' 
                + '-' 
                +  now
                +  '_' )#本地位置

remote_path = '/var/log/nginx/rdlog.log-' + now + '.gz'    #遠端linux主機  

    

        
class App(QWidget):


        def __init__(self):
                super().__init__()
                self.initUI()
                

        def initUI(self):
                self.setWindowTitle('EQ_RDlog下載')
                self.nameLb1 = QLabel("<font color='blue' size='4' face='Arial'>輸入使用者帳號 : </font>", self)
                self.nameEd1 = QLineEdit(self)
                self.nameLb2 = QLabel("<font color='blue' size='4' face='Arial'>輸入使用者密碼 : </font>", self)
                self.nameEd2 = QLineEdit(self)
                self.nameEd2.setEchoMode(QLineEdit.Password)  #設定密文
                #self.log_thread = AppThread()  #類的實例化,也可以在此處實例化,但如過在此處實例化的話,就不會獲得控鍵的值了,傳遞至run()線程中,因此在start()中實例化。
                self.textEdit = QTextEdit()
                self.textEdit.setReadOnly(True)   #設定唯讀,介面是無法輸入的
                self.btnOk = QPushButton("下載")
                self.btnCancel = QPushButton("清除帳密")
                self.Clr = QPushButton("清除內容")

        #設置位置
                mainLayout = QGridLayout(self)
                mainLayout.addWidget(self.nameLb1, 0,0)
                mainLayout.addWidget(self.nameEd1, 0,1)
                mainLayout.addWidget(self.nameLb2, 1,0)
                mainLayout.addWidget(self.nameEd2, 1,1)
                mainLayout.addWidget(self.btnOk, 1,2)
                mainLayout.addWidget(self.btnCancel, 0,2)
                mainLayout.addWidget(self.Clr, 3,2)
                mainLayout.addWidget(self.textEdit, 2,0,1,0)
        # self.setLayout(mainLayout)  主要布局(格子)
        #按鈕動作
                self.btnCancel.clicked.connect(self.nameEd1.clear)
                self.btnCancel.clicked.connect(self.nameEd2.clear)
                self.btnOk.clicked.connect(self.start)  #按下載中連置start() 
                self.Clr.clicked.connect(self.textEdit.clear)

        

        def start(self):
                username = self.nameEd1.text() #獲得帳號
                password = self.nameEd2.text() #獲得密碼
                self.log_thread = AppThread(username,password) #在此實例化是為了讓run()線程中得到參數
                self.log_thread.start()  #開始線程
                self.log_thread.update.connect(self.log)  #信號連接槽函數
                self.log_thread.error.connect(self.error) #信號連接槽函數

        def log(self, i):
                self.textEdit.append(f"<font color='blue' size='6' face='DFKai-sb'> {i} </font>")
                #self.log_thread.update.connect(self.log) 信號連接槽,傳入數值(i)這可以隨意設變數,主要是發射那邊參數是甚麼
                #也能在裡面新增其他self.textEdit.append,照著下面發射的for迴圈逐一顯示

        def error(self, e):
                self.textEdit.append(f"<font color='red' size='6' face='DFKai-sb'> {e} </font>")





class AppThread(QThread):   

        update  = pyqtSignal(str)  #定義str信號槽
        error = pyqtSignal(str)    #定義str信號槽     
        global local_path     #變成全域變數
        global remote_path    #變成全域變數  
        def __init__(self, username, password):  #初始化
            super().__init__()
            self.username = username    #屬性
            self.password = password    #屬性

        #def __del__(self):
                #self.wait()
       
        def run(self):
                #print(self.username)
                #print(self.password)
                for i in range(191,199):
                        log  = "下載完成"    #定義信號內容,也可空值
                        err = "LOG尚未更新"  #定義信號內容
                        
                        try:
                                self.update.emit(f"<font color='green' size='6' face='Arial'>================= </font>")
                                self.update.emit(f"{i}正在下載")
                                transport = paramiko.Transport(('10.11.2.' + str(i), 22))
                                transport.connect(username=self.username, password='peng1026')   #使用者登入帳密
                                sftp = paramiko.SFTPClient.from_transport(transport)
                                sftp.get(remote_path, local_path  + str(i) + '.gz')  # 將遠端檔案下載到本地並重新命名 
                                transport.close()
                                self.update.emit(str(i) + log)  #emit 發射信號
                        except Exception as e:
                                self.error.emit(err)
                                print(e)
                                time.sleep(1)
                self.showdialog()
        
        def showdialog(self):
                dialog = QDialog()
                QLabel("下載完成", dialog)
        
                dialog.setWindowTitle("Dialog")
                # 設置對話框的模態屬性為應用程式級別的模態
                dialog.setWindowModality(Qt.ApplicationModal)
                dialog.exec_()      

if __name__ == "__main__":
        app = QApplication(sys.argv)  
        #QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling) #PyQt5 設置支持高分辨率屏幕自適應的方法
        win = App()
        app.setWindowIcon(QIcon("./002.ico"))
        win.show()
        sys.exit(app.exec_())
