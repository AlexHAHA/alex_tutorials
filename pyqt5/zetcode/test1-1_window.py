import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(600,400)
    w.move(300,500)
    w.setWindowTitle('Test1')
    w.show()

    sys.exit(app.exec_())