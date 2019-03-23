# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtWidgets,QtCore,QtGui,Qt
from PyQt5.QtWidgets import QMainWindow, QFileDialog
import sys
from canvas import Canvas
import os


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setCentralWidget(QtWidgets.QWidget())
        self.setFixedSize(950, 600)

        self.canvas = Canvas(self)
        self.idx = None
        self.img_list = None

        self.horizontalLayoutWidget = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 560, 921, 28))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.openImgBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.openImgBtn.setObjectName("openImgBtn")
        self.openImgBtn.setText("Open")
        self.horizontalLayout.addWidget(self.openImgBtn)

        self.preImgBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.preImgBtn.setObjectName("preImgBtn")
        self.preImgBtn.setText("Pre")
        self.horizontalLayout.addWidget(self.preImgBtn)

        self.nextImgBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.nextImgBtn.setObjectName("nextImgBtn")
        self.nextImgBtn.setText("Next")
        self.horizontalLayout.addWidget(self.nextImgBtn)

        self.detectBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.detectBtn.setObjectName("detectBtn")
        self.detectBtn.setText("Detect")
        self.horizontalLayout.addWidget(self.detectBtn)

        self.verticalLayoutWidget = QtWidgets.QWidget(self)
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
        self.detectBtn.raise_()
        self.frame.raise_()

        QtCore.QMetaObject.connectSlotsByName(self)

        self.connectEvent()

    def connectEvent(self):
            self.openImgBtn.clicked.connect(self.openImage)
            self.preImgBtn.clicked.connect(self.preImage)
            self.nextImgBtn.clicked.connect(self.nextImage)
            self.detectBtn.clicked.connect(self.detectKeypoints)

    def openImage(self):
        path = QFileDialog.getExistingDirectory(self, 'select Image Dir', '.')
        if path is None or path == '':
            return

        self.img_list = [file for file in os.listdir(path) if file.endswith(".jpg") or file.endswith(".png")]
        self.idx = -1 if len(self.img_list) > 0 else None

        if self.idx is None:
            return
        else:
            if self.idx < len(self.img_list) - 1:
                self.idx += 1
            self.img = os.path.join(path, self.img_list[self.idx])

            self.canvas.update(path)

    def preImage(self):
            pass

    def nextImage(self):
            pass

    def detectKeypoints(self):
            pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

