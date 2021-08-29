import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QGridLayout, QPushButton, QTextEdit, QLineEdit, QLabel, QFontDialog, QColorDialog, QGroupBox, QMainWindow, QApplication, QRadioButton, QStackedLayout, QStyle, QToolBar, QToolButton, QVBoxLayout, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import  Qt



class Window(QMainWindow):            #繼承QMainWindow 執行後生成了一個"視窗" 有選單欄、狀態列、工具欄、停靠視窗、中心視窗
    def __init__(self):               #宣告時會自動執行的函式
        super().__init__()            #繼承子類別

        self.setWindowTitle("Tool")   #設置標題
        self.resize(480, 360)         #設置視窗大小
        self.initUI()                 #屬性介面

    def initUI(self):
        toolBar = QToolBar(self)      #添加工具欄模組
        self.addToolBar(Qt.LeftToolBarArea, toolBar)   #設定工具欄為左側LeftToolBarArea

        btnColor = self.createButton('顏色對話框')
        btnColor.clicked.connect(lambda: self.onButtonClicked(0))
        toolBar.addWidget(btnColor)                      #addWidget 添加一個頁面,並返回頁面索引
        btnFont = self.createButton('字體對話框')
        btnFont.clicked.connect(lambda: self.onButtonClicked(1))
        toolBar.addWidget(btnFont)                       #addWidget 添加一個頁面,並返回頁面索引
        btnUser = self.createButton('分組物件')
        btnUser.clicked.connect(lambda: self.onButtonClicked(2))
        toolBar.addWidget(btnUser)                       #addWidget 添加一個頁面,並返回頁面索引


        mainWidget = QWidget(self)  #QWidget 基礎窗口執行後就只有一個"頁面" 沒有選單欄、狀態列、工具欄、停靠視窗、中心視窗
        self.mainLayout = QStackedLayout(mainWidget)   #QStackedLayout堆線布局

        self.mainLayout.addWidget(QColorDialog(self))
        self.mainLayout.addWidget(QFontDialog(self))
        self.mainLayout.addWidget(self.rdlog)
        self.rdlog = QWidget()
        self.createExclusiveGroup()

        mainWidget.setLayout(self.mainLayout)

        self.setCentralWidget(mainWidget)
    

        

    def createButton(self, text):
        icon = QApplication.style().standardIcon(QStyle.SP_FileDialogListView)  #PyQt5內建的QStyle裡面自帶的Icon
        # https://clay-atlas.com/blog/2019/11/17/python-chinese-tutorial-pyqt5-qstyle-icon/ 可參考

        btn = QToolButton(self)
        btn.setText(text)
        btn.setIcon(icon)
        btn.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        return btn
    
    def onButtonClicked(self, index):
        if index < self.mainLayout.count():      #self.mainLayout.count() 獲取頁面數量,這邊是3個
            self.mainLayout.setCurrentIndex(index)   #setCurrentIndex(index) 設置索引index所在頁面為當前頁面
           

            


    def createExclusiveGroup(self):
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

        self.rdlog.setLayout(mainLayout)

        







if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling) #PyQt5 設置支持高分辨率屏幕自適應的方法
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./001.ico"))  #設置視窗圖案
    win = Window()
    win.show()
    sys.exit(app.exec_())
