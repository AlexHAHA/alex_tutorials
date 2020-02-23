"""
This is a simple drag and
drop example.
你可以选中一些文本，然后把文本拖到button上，button会将文本显示。
你可以从窗口的QLineEdit控件中选择文本，也可以从其他应用程序选择，例如浏览器等。
"""
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QApplication)
from PyQt5.QtCore import Qt

class Button(QPushButton):
    def __init__(self, title, parent):
        super().__init__(title, parent)
        self.setAcceptDrops(True)
    def dragEnterEvent(self, e):
        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore()
    def dropEvent(self, e):
        self.setText(e.mimeData().text())

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
 
    def initUI(self):
        edit = QLineEdit('', self)
        edit.setDragEnabled(True)
        edit.move(100,100)
        
        button = Button("Button", self)
        button.move(100,200)

        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('Simple drag&drop')
        self.show()
    def onActivated(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())