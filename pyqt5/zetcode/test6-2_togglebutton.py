"""
In this example, we create three toggle buttons.
They will control the background color of a 
QFrame.
"""
from PyQt5.QtWidgets import (QWidget, QApplication,
                            QFrame, QPushButton)
from PyQt5.QtGui import QColor
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.col = QColor(0,0,0)
        redb = QPushButton('red',self)
        redb.setCheckable(True)
        redb.move(10,10)
        redb.clicked[bool].connect(self.setColor)

        greenb = QPushButton('green', self)
        greenb.setCheckable(True)
        greenb.move(10,60)
        greenb.clicked[bool].connect(self.setColor)

        blueb = QPushButton('blue', self)
        blueb.setCheckable(True)
        blueb.move(10,110)
        blueb.clicked[bool].connect(self.setColor)

        self.square = QFrame(self)
        self.square.setGeometry(150,20,100,100)
        self.square.setStyleSheet("QWidget { background-color: %s }" %  
            self.col.name())
        

        self.setWindowTitle('Toggle button')
        self.setGeometry(300,300,800,600)
        self.show()
    def changeTitle(self, state):
        print(type(state))
        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle(' ')
    def setColor(self, pressed):
        source = self.sender()
        print(type(source))
        if pressed:
            val=255
        else:
            val = 0
        if source.text()=='red':
            self.col.setRed(val)
        if source.text()=='green':
            self.col.setGreen(val)
        if source.text()=='blue':
            self.col.setBlue(val)
        self.square.setStyleSheet("QWidget { background-color: %s }" %  
            self.col.name())
           
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())