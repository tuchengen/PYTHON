from PyQt5.QtWidgets import QWidget


class TceLabel(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
    
    def slot1(self):
        print("你妹")