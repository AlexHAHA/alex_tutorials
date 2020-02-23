"""
This program creates a toolbar.
The toolbar has one action, which
terminates the application, if triggered.
"""

import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QAction,qApp
from PyQt5.QtGui import QIcon


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        exitAction = QAction(QIcon('source//qt_logo.png'),'Exit',self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(qApp.quit)
        

        #
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)

        self.setGeometry(300,300,600,400)
        self.setWindowTitle('Menubar')
        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

