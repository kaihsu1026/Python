from PyQt5.QtGui import QIcon, QGuiApplication
from PyQt5.QtWidgets import QApplication, QMainWindow,  QWidget ,  QTextEdit, QVBoxLayout, QPushButton
import sys  
import pyotp

class TextEditDemo(QWidget):
	def __init__(self, parent=None):
		super(TextEditDemo, self).__init__(parent)
		
		self.setWindowTitle("OPT")
		self.resize(250, 100)    

		self.textEdit = QTextEdit()      
		self.btnPress1 = QPushButton("CU")  
		self.btnPress2 = QPushButton("AMG")  

		layout = QVBoxLayout()
		layout.addWidget(self.textEdit)
		layout.addWidget(self.btnPress1)   
		layout.addWidget(self.btnPress2)   		
		self.setLayout(layout)

		self.btnPress1.clicked.connect(self.btnPress1_Clicked)
		self.btnPress2.clicked.connect(self.btnPress2_Clicked)

		self.totp1 = pyotp.TOTP('C762DBMMURUHERSV')
		self.totp2 = pyotp.TOTP('VTIYUASYIJ2R4JWM')
    	
		self.clipboard = QApplication.clipboard()  #複製剪貼簿

	def btnPress1_Clicked(self):
		self.textEdit.setText(f"<font color='green' size='10' face='DFKai-sb'> <b>{self.totp1.now()} </b></font>")
		self.clipboard.setText(self.totp1.now())      #複製文字
		
	def btnPress2_Clicked(self):
		self.textEdit.setText(f"<font color='green' size='10' face='DFKai-sb'><b>{self.totp2.now()}</b></font>")
		self.clipboard.setText(self.totp2.now())


if __name__ == "__main__":       
	app = QApplication(sys.argv)
	app.setWindowIcon(QIcon("./001.ico"))
	win = TextEditDemo()	
	win.show()	
	sys.exit(app.exec_())
