"""
This example shows a QSlider widget.
"""
from PyQt5.QtWidgets import (QWidget, QApplication,
                            QLabel, QSlider)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        sld = QSlider(Qt.Horizontal, self)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setGeometry(30,40,300,30)
        sld.valueChanged[int].connect(self.changeValue)

        self.label = QLabel('label', self)
        #self.label.setPixmap(QPixmap('source//pyqt_logo.png'))
        self.label.setGeometry(160,100,100,80)

        self.setGeometry(300,300,800,600)
        self.setWindowTitle('QSlider')
        self.show()
    def changeTitle(self, state):
        print(type(state))
        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle(' ')
    def changeValue(self, value):
        if value == 0:
            #self.label.setPixmap(QPixmap('source//mute.png'))
            self.label.setText("mute")
        elif value > 0 and value <= 30:
            self.label.setText("min")
        elif value > 30 and value < 80:
            self.label.setText("med")
        else:
            #self.label.text = "max"         
            self.label.setText("max")  
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())