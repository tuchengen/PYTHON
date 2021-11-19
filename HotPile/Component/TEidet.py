


from PyQt5 import QtCore, QtGui, QtWidgets

class MyCheckBox(QtWidgets.QFrame):
    # mySignal = pyqtSignal(str,str)

    def __init__(self, parent = None):
        super(MyCheckBox, self).__init__(parent)
        self.initUI()
    
    def initUI(self):
        pass