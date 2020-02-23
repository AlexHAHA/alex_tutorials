"""
In this example, we create a skeleton
of a calculator using a QGridLayout.
"""

import sys
from PyQt5.QtWidgets import (QWidget,QLabel,QApplication,
                    QGridLayout,QPushButton)

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)
        names = ['Cls','Bck','','close',
                '7', '8', '9', '/',
                '4', '6', '7', '*',
                '1', '2', '3', '-',
                '0', '.', '=', '+']
        positions = [(i,j) for i in range(5) for j in range(4)]
        for position,name in zip(positions,names):
            if name == '':
                continue
            btn = QPushButton(name)
            grid.addWidget(btn, *position)

        self.setGeometry(300,300,600,400)
        self.setWindowTitle('QGridLayout')
        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

