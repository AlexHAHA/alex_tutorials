"""
In this example, we position two push
buttons in the bottom-right corner 
of the window. 
"""

import sys
from PyQt5.QtWidgets import (QWidget,QLabel,QApplication,
                    QHBoxLayout,QVBoxLayout,QPushButton)

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        okButton = QPushButton("OK")
        cancleButton = QPushButton("Cancle")
        hbox = QHBoxLayout()
        # 添加一个伸缩空间
        #hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancleButton)
        hbox.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        self.setLayout(vbox)

        self.setGeometry(300,300,600,400)
        self.setWindowTitle('BoxLayout')
        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

