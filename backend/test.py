import sys
from PyQt5.QtWidgets import QApplication,QWidget

if __name__ == '__main__':

    app=QApplication(sys.argv)
    w=QWidget()
    w.resize(780,700)
    w.move(600,600)
    w.setWindowTitle("test")
    w.show()
    sys.exit(app.exec_())