"""
This is a simple drag and
drop example.
你可以使用鼠标右键点中button拖动到窗口内其他位置
"""
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QApplication)
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDrag

class Button(QPushButton):
    def __init__(self, title, parent):
        super().__init__(title, parent)
        self.setAcceptDrops(True)
    def mouseMoveEvent(self, e):
        if e.buttons() != Qt.RightButton:
            return
        mimeData = QMimeData()
        drag = QDrag(self)
        drag.setMimeData(mimeData)
        drag.setHotSpot(e.pos()-self.rect().topLeft())
        
        dropAction = drag.exec_(Qt.MoveAction)
    def mousePressEvent(self, e):
        QPushButton.mousePressEvent(self, e)
        if e.button() == Qt.LeftButton:
            print('press')

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
 
    def initUI(self):
        self.setAcceptDrops(True)
        self.button = Button('button', self)
        self.button.move(100,100)

        self.button2 = Button('button2', self)
        self.button2.move(100,200)

        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('Simple drag&drop')
        self.show()
    def dragEnterEvent(self, e):
        e.accept()
    def dropEvent(self, e):
        print(type(e))
        source = self.sender()
        print(type(source))
        position = e.pos()
        self.button.move(position)

        e.setDropAction(Qt.MoveAction)
        e.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())