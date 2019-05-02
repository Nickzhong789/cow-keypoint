# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testDialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog


class TrainDialog(QDialog):
    def __init__(self, parent=None):
        super(TrainDialog, self).__init__(parent)
        self.setWindowTitle("Dialog")
        self.setFixedSize(550, 565)

        self.verticalLayoutWidget = QtWidgets.QWidget(parent)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 210, 501, 231))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.Res18Button = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.Res18Button.setObjectName("Res18Button")
        self.Res18Button.setText("ResNet18")
        self.verticalLayout.addWidget(self.Res18Button)

        self.Res34Button = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.Res34Button.setObjectName("Res34Button")
        self.Res34Button.setText("ResNet34")
        self.verticalLayout.addWidget(self.Res34Button)

        self.Res50Button = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.Res50Button.setObjectName("Res50Button")
        self.Res50Button.setText("ResNet50")
        self.verticalLayout.addWidget(self.Res50Button)

        self.hgButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.hgButton.setObjectName("hgButton")
        self.hgButton.setText("Stack Hourglass")
        self.verticalLayout.addWidget(self.hgButton)

        self.pyraButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.pyraButton.setObjectName("pyraButton")
        self.pyraButton.setText("PyraNet")
        self.verticalLayout.addWidget(self.pyraButton)

        self.verticalLayoutWidget.raise_()
        self.Res18Button.raise_()

        QtCore.QMetaObject.connectSlotsByName(self)

        self.setLayout(self.verticalLayout)
