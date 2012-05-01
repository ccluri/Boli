import sys
import subprocess
from PyQt4 import Qt,QtGui,QtCore
from boliLayout import *

class DesignerMainWindow(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(DesignerMainWindow, self).__init__(parent)
        self.setupUi(self) 
        self.connectActions()
        self.translate()
        self.retranslateUi(self)

    def connectActions(self):
        self.connect(self.hotPushButton,QtCore.SIGNAL('toggled()'),self.hotOutputTextEdit)
        self.connect(self.kaPushButton,QtCore.SIGNAL('released()'),self.kaOutputTextEdit)
        self.connect(self.coldPushButton,QtCore.SIGNAL('released()'),self.coldOutputTextEdit)
        self.connect(self.yesPushButton,QtCore.SIGNAL('released()'),self.yesOutputTextEdit)
        self.connect(self.waterPushButton,QtCore.SIGNAL('released()'),self.waterOutputTextEdit)
        self.connect(self.foodPushButton,QtCore.SIGNAL('released()'),self.foodOutputTextEdit)
        self.connect(self.happyPushButton,QtCore.SIGNAL('released()'),self.happyOutputTextEdit)
        self.connect(self.noPushButton,QtCore.SIGNAL('released()'),self.noOutputTextEdit)
        self.connect(self.helloPushButton,QtCore.SIGNAL('released()'),self.helloOutputTextEdit)
        self.connect(self.sayPushButton,QtCore.SIGNAL('released()'),self.sayItLoud)

    def sayItLoud(self):
        p1 = subprocess.Popen(["echo", str(self.outputTextEdit.toPlainText())], stdout=subprocess.PIPE)
        p2 = subprocess.Popen(["festival", "--tts"], stdin=p1.stdout, stdout=subprocess.PIPE)

    def hotOutputTextEdit(self):
        self.outputTextEdit.setText(self.hotPushButton.text())

    def kaOutputTextEdit(self):
        self.outputTextEdit.setText(self.kaPushButton.text())

    def coldOutputTextEdit(self):
        self.outputTextEdit.setText(self.coldPushButton.text())

    def yesOutputTextEdit(self):
        self.outputTextEdit.setText(self.yesPushButton.text())

    def waterOutputTextEdit(self):
        self.outputTextEdit.setText(self.waterPushButton.text())

    def foodOutputTextEdit(self):
        self.outputTextEdit.setText(self.foodPushButton.text())

    def happyOutputTextEdit(self):
        self.outputTextEdit.setText(self.happyPushButton.text())

    def noOutputTextEdit(self):
        self.outputTextEdit.setText(self.noPushButton.text())

    def helloOutputTextEdit(self):
        self.outputTextEdit.setText(self.helloPushButton.text())

    def doQuit(self):
        QtGui.qApp.closeAllWindows()

    def translate(self):
        translate1 = QtCore.QTranslator()
        translate1.load("t1_hi",".")
        app.installTranslator(translate1)
        
app = QtGui.QApplication(sys.argv)
dmw = DesignerMainWindow()
dmw.show()
sys.exit(app.exec_())
                     
