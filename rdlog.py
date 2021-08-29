import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QTextEdit, QApplication, QDialog, QGridLayout, QLabel, QLineEdit, QMainWindow, QPushButton, QTableWidget, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QEventLoop, QTimer, QThread, pyqtSignal
import paramiko
import datetime


class MainWindow(QWidget):
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
       

        self.textEdit = QTextEdit()
        self.textEdit.setReadOnly(True)   #設定唯讀,介面是無法輸入的

        self.btnOk = QPushButton("下載")
        self.btnCancel = QPushButton("清除帳密")
        self.Clr = QPushButton("清除內容")
        
        

        

        #設置位置
        mainLayout = QGridLayout(self)
        mainLayout.addWidget(self.nameLb1, 0,0)
        mainLayout.addWidget(self.nameEd1, 0,1,1,2)
        mainLayout.addWidget(self.nameLb2, 1,0)
        mainLayout.addWidget(self.nameEd2, 1,1,1,2)
        mainLayout.addWidget(self.btnOk, 2,1)
        mainLayout.addWidget(self.btnCancel, 2,2)
        mainLayout.addWidget(self.Clr, 2,0)
        mainLayout.addWidget(self.textEdit, 3,0,1,0)

        #按鈕動作
        self.btnCancel.clicked.connect(self.nameEd1.clear)
        self.btnCancel.clicked.connect(self.nameEd2.clear)
        self.btnOk.clicked.connect(self.rdlog)
        self.Clr.clicked.connect(self.Cler)


    def Cler(self):
        self.textEdit.clear()

    def rdlog(self):
        username = self.nameEd1.text()
        password = self.nameEd2.text()
        now = datetime.datetime.now().strftime("%Y%m%d")    #設定當下時間(年月日)
        local_path = ( './rdlog.log' 
                + '-' 
                +  now
                +  '_' )#本地位置
        remote_path = '/var/log/nginx/rdlog.log-' + now + '.gz'    #遠端linux主機  
        

        self.btnOk.setText('下載中')
        try:
            for i in range(191, 199):
                
                transport = paramiko.Transport(('10.11.2.' + str(i), 22))
                transport.connect(username=username, password=password)   #使用者登入帳密
                sftp = paramiko.SFTPClient.from_transport(transport)
                sftp.get(remote_path, local_path  + str(i) + '.gz')  # 將遠端檔案下載到本地並重新命名
                
                self.textEdit.append(f"<font color='blue' size='6' face='Arial'> {str(i)}正在下載 </font>")
                loop = QEventLoop()
                QTimer.singleShot(2000, loop.quit)
                loop.exec_() 
                self.textEdit.append(f"<font color='blue' size='6' face='Arial'> {str(i)}下載完畢 </font>")
                self.textEdit.append(f"<font color='green' size='6' face='Arial'> ------------------ </font>")
                transport.close()

            self.btnOk.setText('下載')    

            
        except Exception:
                self.textEdit.append(f"<font color='red' size='6' face='Arial'> LOG尚未更新 </font>")
                loop = QEventLoop()
                QTimer.singleShot(2000, loop.quit)
                loop.exec_()
    


          

if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling) #PyQt5 設置支持高分辨率屏幕自適應的方法
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./001.ico"))
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())