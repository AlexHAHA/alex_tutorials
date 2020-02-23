"""
In this example, we determine the event sender
object.
"""
import sys
from PyQt5.QtCore import   pyqtSignal, QObject, Qt
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication

class Communicate(QObject):
    #pyqt5信号要定义为类属性
    closeApp = pyqtSignal()


class Example(QMainWindow):
    #pyqt5信号要定义为类属性
    s2 = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        
        self.c = Communicate()
        # closeApp信号连接的事self.close插槽！
        self.c.closeApp.connect(self.close)

        self.s2.connect(self.close)

        self.setGeometry(300,300,800,600)
        self.setWindowTitle('Emit signal')
        self.show()

    def mousePressEvent(self, event):
        # 触发信号
        self.c.closeApp.emit()
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.s2.emit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


