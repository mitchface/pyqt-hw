from PyQt4 import QtGui
import untitled
class Main(QtGui.QMainWindow, untitled.Ui_MainWindow):
    """ MainApp Class thats generated from the untitled.ui and converted to python """
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)
        self.actionQuit.triggered.connect(QtGui.qApp.quit)
        self.pushButtonHelloWorld.clicked.connect(self.say_hi)
        self.show()

    def say_hi(self):
        print "Hi World"

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    MA = Main()
    
    app.exec_()