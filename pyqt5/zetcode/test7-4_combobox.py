"""
This example shows
how to use QComboBox widget.
"""
import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QComboBox, QApplication)
from PyQt5.QtCore import Qt
class Example(QWidget):
    def __init__(self):
        super().__init__()
 
        self.initUI()
 
    def initUI(self):
        self.lbl = QLabel('ubuntu', self)
        combo = QComboBox(self)
        combo.addItem("Ubuntu")
        combo.addItem("Mandriva")
        combo.addItem("Fedora")
        combo.addItem('Arch')
        combo.addItem("Gentoo")
        combo.activated[str].connect(self.onActivated)

        combo2 = QComboBox(self)
        combo2.addItems(["9600","115200","230400"])

        self.lbl.move(100,200)
        combo.move(100,100)
        combo2.move(100,300)

        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('QComboBox')
        self.show()
    def onActivated(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())