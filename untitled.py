# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created: Tue Aug 07 15:55:58 2012
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(430, 253)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButtonHelloWorld = QtGui.QPushButton(self.centralwidget)
        self.pushButtonHelloWorld.setObjectName(_fromUtf8("pushButtonHelloWorld"))
        self.gridLayout.addWidget(self.pushButtonHelloWorld, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 430, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMenu = QtGui.QMenu(self.menubar)
        self.menuMenu.setObjectName(_fromUtf8("menuMenu"))
        self.menuFag = QtGui.QMenu(self.menubar)
        self.menuFag.setObjectName(_fromUtf8("menuFag"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionYes = QtGui.QAction(MainWindow)
        self.actionYes.setCheckable(False)
        self.actionYes.setEnabled(True)
        self.actionYes.setObjectName(_fromUtf8("actionYes"))
        self.actionNo = QtGui.QAction(MainWindow)
        self.actionNo.setObjectName(_fromUtf8("actionNo"))
        self.menuMenu.addAction(self.actionQuit)
        self.menuFag.addAction(self.actionYes)
        self.menuFag.addAction(self.actionNo)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuFag.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonHelloWorld.setText(QtGui.QApplication.translate("MainWindow", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.menuMenu.setTitle(QtGui.QApplication.translate("MainWindow", "Menu", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFag.setTitle(QtGui.QApplication.translate("MainWindow", "fag", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionYes.setText(QtGui.QApplication.translate("MainWindow", "yes", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNo.setText(QtGui.QApplication.translate("MainWindow", "no", None, QtGui.QApplication.UnicodeUTF8))

