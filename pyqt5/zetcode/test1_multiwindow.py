
import cv2 as cv
import numpy as np
import sys
import threading, time
from PyQt5.QtWidgets import (QMainWindow, QWidget, QApplication, 
                QDesktopWidget, QPushButton, QLabel, QAction,QDialog,
                QGridLayout)
from PyQt5.QtCore import  Qt
from PyQt5.QtGui import QImage, QPixmap


class A(QWidget):		 
    def __init__(self):	
        super(A,self).__init__()
        self.initUI()	 	 
    def initUI(self):			 
        self.btn = QPushButton('跳转按钮', self)	
        self.btn.setGeometry(100,100,100,100)

        self.setGeometry(1000,1000,1000,800)
        self.setWindowTitle('A')
class B(QDialog):		 
    def __init__(self):	
        super(B,self).__init__()		 
        self.initUI()
    def initUI(self):			 
        pass	 
    
if __name__ == '__main__':		 
    app = QApplication(sys.argv)		 
    a = A()		 
    b = B()		 
    a.show()		 
    a.btn.clicked.connect(b.show)		 
    app.exec_()	