import sys
from PyQt5.QtWidgets import QApplication

app = QApplication(sys.argv)
screen=app.desktop().screenGeometry()
w=screen.width()/1920
h=screen.height()/1080