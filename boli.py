#Author:Chaitanya CH
#FileName: boli.py

#This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 3, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.

import sys
import subprocess
import time
from PyQt4 import Qt,QtGui,QtCore
from boliLayout import *


class DesignerMainWindow(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(DesignerMainWindow, self).__init__(parent)
        self.setupUi(self) 
        self.connectActions()
        #self.translate()
        #self.retranslateUi(self)
        self.defaultTimePause = 0.5 #seconds

    def eventFilter(self, source, event): #hover functionality - gets called multiple times though!
        if event.type() == QtCore.QEvent.MouseMove:
            if event.buttons() == QtCore.Qt.NoButton:
#                pos = event.pos()
#                print pos.x(),pos.y()
                if self.cancelPushButton.underMouse():
                    self.clearText()
                    time.sleep(self.defaultTimePause)
                    #             _________
                    #page Deadend | 0 | 1 | Deadend
                    #page Deadend | 2 | 3 | Deadend
                    #             ---------  
                elif self.leftPagePushButton.underMouse():
                    thisPage = self.stackedWidget.currentIndex()
                    if thisPage == 1:
                        thisPage = self.stackedWidget.setCurrentIndex(0)
                        time.sleep(self.defaultTimePause)
                    elif thisPage ==3:
                        thisPage = self.stackedWidget.setCurrentIndex(2)
                        time.sleep(self.defaultTimePause)

                elif self.rightPagePushButton.underMouse():
                    thisPage = self.stackedWidget.currentIndex()
                    if thisPage == 0:
                        thisPage = self.stackedWidget.setCurrentIndex(1)
                        time.sleep(self.defaultTimePause)
                    elif thisPage ==2:
                        thisPage = self.stackedWidget.setCurrentIndex(3)
                        time.sleep(self.defaultTimePause)

                elif self.topPagePushButton.underMouse():
                    thisPage = self.stackedWidget.currentIndex()
                    if thisPage == 2:
                        thisPage = self.stackedWidget.setCurrentIndex(0)
                        time.sleep(self.defaultTimePause)
                    elif thisPage ==3:
                        thisPage = self.stackedWidget.setCurrentIndex(1)
                        time.sleep(self.defaultTimePause)

                elif self.bottomPagePushButton.underMouse():
                    thisPage = self.stackedWidget.currentIndex()
                    if thisPage == 0:
                        thisPage = self.stackedWidget.setCurrentIndex(2)
                        time.sleep(self.defaultTimePause)
                    elif thisPage == 1:
                        thisPage = self.stackedWidget.setCurrentIndex(3)
                        time.sleep(self.defaultTimePause)


        return QtGui.QMainWindow.eventFilter(self, source, event)

    def clearText(self):
        self.outputTextEdit.clear()

    def connectActions(self):
        self.connect(self.hotPushButton,QtCore.SIGNAL('released()'),self.hotOutputTextEdit)
        self.connect(self.kaPushButton,QtCore.SIGNAL('released()'),self.kaOutputTextEdit)
        self.connect(self.coldPushButton,QtCore.SIGNAL('released()'),self.coldOutputTextEdit)
        self.connect(self.yesPushButton,QtCore.SIGNAL('released()'),self.yesOutputTextEdit)
        self.connect(self.waterPushButton,QtCore.SIGNAL('released()'),self.waterOutputTextEdit)
        self.connect(self.foodPushButton,QtCore.SIGNAL('released()'),self.foodOutputTextEdit)
        self.connect(self.happyPushButton,QtCore.SIGNAL('released()'),self.happyOutputTextEdit)
        self.connect(self.noPushButton,QtCore.SIGNAL('released()'),self.noOutputTextEdit)
        self.connect(self.helloPushButton,QtCore.SIGNAL('released()'),self.helloOutputTextEdit)
        self.connect(self.sayPushButton,QtCore.SIGNAL('released()'),self.sayItLoud)


        self.connect(self.pushButton, QtCore.SIGNAL('released()'),self.pushButtonPress)
        self.connect(self.pushButton_2, QtCore.SIGNAL('released()'),self.pushButtonPress_2)
        self.connect(self.pushButton_3, QtCore.SIGNAL('released()'),self.pushButtonPress_3)
        self.connect(self.pushButton_4, QtCore.SIGNAL('released()'),self.pushButtonPress_4)
        self.connect(self.pushButton_5, QtCore.SIGNAL('released()'),self.pushButtonPress_5)
        self.connect(self.pushButton_6, QtCore.SIGNAL('released()'),self.pushButtonPress_6)
        self.connect(self.pushButton_7, QtCore.SIGNAL('released()'),self.pushButtonPress_7)
        self.connect(self.pushButton_8, QtCore.SIGNAL('released()'),self.pushButtonPress_8)
        self.connect(self.pushButton_9, QtCore.SIGNAL('released()'),self.pushButtonPress_9)
        self.connect(self.pushButton_10, QtCore.SIGNAL('released()'),self.pushButtonPress_10)
        self.connect(self.pushButton_11, QtCore.SIGNAL('released()'),self.pushButtonPress_11)
        self.connect(self.pushButton_12, QtCore.SIGNAL('released()'),self.pushButtonPress_12) 
        self.connect(self.pushButton_13, QtCore.SIGNAL('released()'),self.pushButtonPress_13)
        self.connect(self.pushButton_14, QtCore.SIGNAL('released()'),self.pushButtonPress_14)
        self.connect(self.pushButton_15, QtCore.SIGNAL('released()'),self.pushButtonPress_15)
        self.connect(self.pushButton_16, QtCore.SIGNAL('released()'),self.pushButtonPress_16)
        self.connect(self.pushButton_17, QtCore.SIGNAL('released()'),self.pushButtonPress_17)
        self.connect(self.pushButton_18, QtCore.SIGNAL('released()'),self.pushButtonPress_18)
        self.connect(self.pushButton_19, QtCore.SIGNAL('released()'),self.pushButtonPress_19)
        self.connect(self.pushButton_20, QtCore.SIGNAL('released()'),self.pushButtonPress_20)
        self.connect(self.pushButton_21, QtCore.SIGNAL('released()'),self.pushButtonPress_21)
        self.connect(self.pushButton_22, QtCore.SIGNAL('released()'),self.pushButtonPress_22) 
        self.connect(self.pushButton_23, QtCore.SIGNAL('released()'),self.pushButtonPress_23)
        self.connect(self.pushButton_24, QtCore.SIGNAL('released()'),self.pushButtonPress_24)

        
        self.connect(self.pushButton_25, QtCore.SIGNAL('released()'),self.pushButtonPress_25)
        self.connect(self.pushButton_26, QtCore.SIGNAL('released()'),self.pushButtonPress_26)
        self.connect(self.pushButton_27, QtCore.SIGNAL('released()'),self.pushButtonPress_27)

    def sayItLoud(self):
#        print unicode(self.outputTextEdit.toPlainText())
        p1 = subprocess.Popen(["echo", unicode(self.outputTextEdit.toPlainText())], stdout=subprocess.PIPE)
        p2 = subprocess.Popen(["festival","voice_hindi_NSK_diphone", "--tts"], stdin=p1.stdout, stdout=subprocess.PIPE)
        



    def pushButtonPress(self): #this has to be the saddest possible way of doing this!
         self.textEdit.insertPlainText(self.pushButton.text()) #unicorns are shedding tears at my incompetance. 
        
    def pushButtonPress_2(self):
        self.textEdit.insertPlainText(self.pushButton_2.text()) 

    def pushButtonPress_3(self):
         self.textEdit.insertPlainText(self.pushButton_3.text()) 

    def pushButtonPress_4(self):
        self.textEdit.insertPlainText(self.pushButton_4.text()) 

    def pushButtonPress_5(self):
         self.textEdit.insertPlainText(self.pushButton_5.text()) 

    def pushButtonPress_6(self):
        self.textEdit.insertPlainText(self.pushButton_6.text()) 

    def pushButtonPress_7(self):
        self.textEdit.insertPlainText(self.pushButton_7.text()) 

    def pushButtonPress_8(self):
         self.textEdit.insertPlainText(self.pushButton_8.text()) 

    def pushButtonPress_9(self):
        self.textEdit.insertPlainText(self.pushButton_9.text()) 

    def pushButtonPress_10(self):
         self.textEdit.insertPlainText(self.pushButton_10.text()) 

    def pushButtonPress_11(self):
         self.textEdit.insertPlainText(self.pushButton_11.text()) 

    def pushButtonPress_12(self):
        self.textEdit.insertPlainText(self.pushButton_12.text()) 

    def pushButtonPress_13(self):
         self.textEdit.insertPlainText(self.pushButton_13.text()) 

    def pushButtonPress_14(self):
        self.textEdit.insertPlainText(self.pushButton_14.text()) 

    def pushButtonPress_15(self):
         self.textEdit.insertPlainText(self.pushButton_15.text()) 

    def pushButtonPress_16(self):
        self.textEdit.insertPlainText(self.pushButton_16.text()) 

    def pushButtonPress_17(self):
        self.textEdit.insertPlainText(self.pushButton_17.text()) 

    def pushButtonPress_18(self):
         self.textEdit.insertPlainText(self.pushButton_18.text()) 

    def pushButtonPress_19(self):
        self.textEdit.insertPlainText(self.pushButton_19.text()) 

    def pushButtonPress_20(self):
         self.textEdit.insertPlainText(self.pushButton_20.text()) 

    def pushButtonPress_21(self):
         self.textEdit.insertPlainText(self.pushButton_21.text()) 

    def pushButtonPress_22(self):
         self.textEdit.insertPlainText(self.pushButton_22.text()) 

    def pushButtonPress_23(self):
         self.textEdit.insertPlainText(self.pushButton_23.text()) 

    def pushButtonPress_24(self):
         self.textEdit.insertPlainText(self.pushButton_24.text()) 

    def pushButtonPress_25(self): #backspace
         text = unicode(self.textEdit.toPlainText())[:-1]
#         text = text[:-1]
         self.textEdit.setPlainText('')
         self.textEdit.insertPlainText(text)

    def pushButtonPress_26(self):
         self.textEdit.insertPlainText(str(' ')) 

    def pushButtonPress_27(self):
#        print unicode(self.outputTextEdit.toPlainText())
        p1 = subprocess.Popen(["echo", unicode(self.textEdit.toPlainText())], stdout=subprocess.PIPE)
        p2 = subprocess.Popen(["festival","voice_hindi_NSK_diphone", "--tts"], stdin=p1.stdout, stdout=subprocess.PIPE)


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
app.installEventFilter(dmw)
dmw.show()
sys.exit(app.exec_())
                     
