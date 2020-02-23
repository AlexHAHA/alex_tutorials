"""
This example shows an icon in the titlebar of the window.
"""
import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QIcon

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(500,300,600,400)
        self.setWindowTitle('Test2')
        # 可以识别多种格式图片，图片大小自动调整
        #self.setWindowIcon(QIcon('source//qt_logo.jpg')) 
        self.setWindowIcon(QIcon('source//qt_logo.png'))
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())