import sys

from PyQt5 import QtWidgets as QtW


WIDTH = 250
HIGH = 150


def btn_click():
    frame.close()


app = QtW.QApplication(sys.argv)
master = QtW.QWidget()
master.resize(WIDTH, HIGH)
master.setWindowTitle('Hello!')


m_frame = QtW.QFrame  # Main app.
btn = QtW.QPushButton('Add!', master)
btn.clicked.connect(btn_click)
btn.move(20, 20)
frame = QtW.QFrame(master)
frame.move(btn.size().width() + 20, 20)
lbl = QtW.QLabel('Hello!', frame)

QtW.QCheckBox("I'm checkbox!", master)
a.move(10, 70)


master.show()

sys.exit(app.exec())
