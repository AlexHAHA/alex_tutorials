"""
This program shows a confirmation 
message box when we click on the close
button of the application window. 
"""
import sys
from PyQt5.QtWidgets import QWidget,QDesktopWidget,QApplication

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(1000,600)
        self.center()

        self.setWindowTitle('Center')
        self.show()

    def center(self):
        #获取窗口
        qr = self.frameGeometry()
        #获取屏幕中心点
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

