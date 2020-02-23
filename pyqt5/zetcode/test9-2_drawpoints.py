"""
In the example, we draw randomly 1000 red points
on the window.
注意，红点很小
"""
import sys
from PyQt5.QtWidgets import (QWidget, QApplication)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter,QColor,QFont,QPen
import random

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
 
    def initUI(self):        
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('Points')
        self.show()
    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawPoints(qp)
        qp.end()
    def drawPoints(self, qp):
        print(self.size())
        qp.setPen(Qt.red)
        size = self.size()
        for i in range(100):
            x = random.randint(1, size.width()-1)
            y = random.randint(1, size.height()-1)
            qp.drawPoint(x,y)
            qp.drawRect(x,y,20,20)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())