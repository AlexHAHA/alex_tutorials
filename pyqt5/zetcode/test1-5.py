"""
This program shows a confirmation 
message box when we click on the close
button of the application window. 
"""
import sys
from PyQt5.QtWidgets import QWidget,QMessageBox,QApplication
from PyQt5.QtCore import QCoreApplication

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(1000,800,600,400)
        self.setWindowTitle('Quit button')
        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self,'Message',
                'Are you sure to quit?',QMessageBox.Yes|QMessageBox.No, 
                QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

