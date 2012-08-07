from PyQt4 import QtGui
import untitled

class Main(QtGui.QMainWindow, untitled.Ui_MainWindow):
    """ MainApp Class thats generated from the untitled.ui and converted to python """
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        
        self.setupUi(self)
        self.actionQuit.triggered.connect(QtGui.qApp.quit)
        self.actionYes.triggered.connect(self.say_fag)
        self.actionNo.triggered.connect(self.say_notfag)
        self.pushButtonHelloWorld.clicked.connect(self.say_hi)
        self.show()
        self.hihi = 'ooo harrow!'
        
		
    def say_hi(self):
		print self.hihi
		
    def say_fag(self):
		self.hihi = 'fag'
    def say_notfag(self):
		self.hihi = 'ooo harrow!'

		
       
		
if __name__ == '__main__':
    import sys
    
    app = QtGui.QApplication(sys.argv)
    MA = Main()
    
    app.exec_()