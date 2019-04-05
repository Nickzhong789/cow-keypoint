# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(976, 595)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 560, 921, 28))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.openImgBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.openImgBtn.setObjectName("openImgBtn")
        self.horizontalLayout.addWidget(self.openImgBtn)
        self.preImgBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.preImgBtn.setObjectName("preImgBtn")
        self.horizontalLayout.addWidget(self.preImgBtn)
        self.nextImgBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.nextImgBtn.setObjectName("nextImgBtn")
        self.horizontalLayout.addWidget(self.nextImgBtn)
        self.showBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.showBtn.setObjectName("showBtn")
        self.horizontalLayout.addWidget(self.showBtn)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 30, 921, 511))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout.addWidget(self.frame)
        self.horizontalLayoutWidget.raise_()
        self.verticalLayoutWidget.raise_()
        self.frame.raise_()
        self.nextImgBtn.raise_()
        self.showBtn.raise_()
        self.frame.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.openImgBtn.setText(_translate("Form", "Open"))
        self.preImgBtn.setText(_translate("Form", "Pre"))
        self.nextImgBtn.setText(_translate("Form", "Next"))
        self.showBtn.setText(_translate("Form", "Show"))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = Ui_Form()
    main_window.show()
    sys.exit(app.exec_())

