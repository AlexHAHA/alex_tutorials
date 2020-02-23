"""
In this example, we connect a signal
of a QSlider to a slot of a QLCDNumber.
"""
import sys
from PyQt5.QtCore import   Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider,
                            QVBoxLayout, QApplication)
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display)

        self.setGeometry(300,300,800,600)
        self.setWindowTitle('signal & slot')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


