"""
This example shows a QProgressBar  widget.
"""
from PyQt5.QtWidgets import (QWidget, QApplication,
                            QPushButton, QProgressBar)
from PyQt5.QtCore import QBasicTimer
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(100,100,400,30)
        self.btn = QPushButton('start', self)
        self.btn.move(200,200)
        self.btn.clicked.connect(self.doAction)

        self.timer = QBasicTimer()
        self.step = 0
        
        self.setGeometry(300,300,800,600)
        self.setWindowTitle('QProgressBar')
        self.show()

    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('Finished')
            return
        self.step = self.step + 1
        self.pbar.setValue(self.step)

    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('start')
        else:
            self.timer.start(100,self)
            self.btn.setText('stop')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())