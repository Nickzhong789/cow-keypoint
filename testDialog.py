# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testDialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 565)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(0, -30, 501, 571))
        self.widget.setObjectName("widget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.widget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 210, 501, 231))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Res18Button = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.Res18Button.setObjectName("Res18Button")
        self.verticalLayout.addWidget(self.Res18Button)
        self.Res34Button = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.Res34Button.setObjectName("Res34Button")
        self.verticalLayout.addWidget(self.Res34Button)
        self.Res50Button = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.Res50Button.setObjectName("Res50Button")
        self.verticalLayout.addWidget(self.Res50Button)
        self.hgButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.hgButton.setObjectName("hgButton")
        self.verticalLayout.addWidget(self.hgButton)
        self.pyraButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.pyraButton.setObjectName("pyraButton")
        self.verticalLayout.addWidget(self.pyraButton)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Res18Button.setText(_translate("Dialog", "ResNet18"))
        self.Res34Button.setText(_translate("Dialog", "ResNet34"))
        self.Res50Button.setText(_translate("Dialog", "ResNet50"))
        self.hgButton.setText(_translate("Dialog", "Stack Hourglass"))
        self.pyraButton.setText(_translate("Dialog", "PyraNet"))


