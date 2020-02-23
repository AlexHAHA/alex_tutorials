"""
In the example, we draw randomly 1000 red points
on the window.
注意，红点很小
"""
import sys
from PyQt5.QtWidgets import (QWidget, QApplication)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter,QColor,QFont,QBrush,QPen
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
        self.drawRectangles(qp)
        qp.end()

    def drawRectangles(self, qp):
        col = QColor(0,0,0)
        col.setNamedColor('#d4d4d4')
        # 用于绘制线条、曲线和矩形、椭圆、多边形或其他形状的轮廓
        qp.setPen(col)

        # 用于油漆的背景图形形状,如矩形、椭圆形或多边形的填充
        qp.setBrush(QColor(200,0,0))
        qp.drawRect(130,30,90,60)

        qp.setBrush(QColor(25,0,0,200))
        qp.drawRect(330,30,90,60)

        # 不同的轮廓和填充的组合
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        brush = QBrush(Qt.SolidPattern)
        qp.setPen(pen)
        qp.setBrush(brush)
        qp.drawRect(130,130,90,60)

        pen.setStyle(Qt.DotLine)
        brush = QBrush(Qt.DiagCrossPattern)
        brush.setColor(QColor(0,0,200))
        qp.setPen(pen)
        qp.setBrush(brush)
        qp.drawRect(330,130,90,60)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())