from PySide2 import QtCore, QtWidgets

class Calculator(QtWidgets.QWidget):
    def __init__(self):
        super(Calculator, self).__init__()

        self.setWindowTitle('Ma Super Calculatrice')
        self.setupUi()

    def setupUi(self):

        self.le_operation = QtWidgets.QLineEdit()
        self.le_result = QtWidgets.QLineEdit()

        self.gridLayout = QtWidgets.QGridLayout(self)

        self.btn_0 = QtWidgets.QPushButton('0')
        self.btn_1 = QtWidgets.QPushButton('1')
        self.btn_2 = QtWidgets.QPushButton('2')
        self.btn_3 = QtWidgets.QPushButton('3')
        self.btn_4 = QtWidgets.QPushButton('4')
        self.btn_5 = QtWidgets.QPushButton('5')
        self.btn_6 = QtWidgets.QPushButton('6')
        self.btn_7 = QtWidgets.QPushButton('7')
        self.btn_8 = QtWidgets.QPushButton('8')
        self.btn_9 = QtWidgets.QPushButton('9')

        self.btn_dot = QtWidgets.QPushButton('.')
        self.btn_addition = QtWidgets.QPushButton('+')
        self.btn_substraction = QtWidgets.QPushButton('-')
        self.btn_multipliation = QtWidgets.QPushButton('x')
        self.btn_division = QtWidgets.QPushButton('/')
        self.btn_equal = QtWidgets.QPushButton('=')
        self.btn_reset = QtWidgets.QPushButton('C')

        self.gridLayout.addWidget(self.le_operation, 0, 0 , 1, 4)
        self.gridLayout.addWidget(self.le_result, 1, 0 , 1, 4)
        self.gridLayout.addWidget(self.btn_reset, 2, 0 , 1, 1)
        self.gridLayout.addWidget(self.btn_division, 2, 3 , 1, 1)
        self.gridLayout.addWidget(self.btn_7, 3, 0 , 1, 1)
        self.gridLayout.addWidget(self.btn_8, 3, 1 , 1, 1)
        self.gridLayout.addWidget(self.btn_9, 3, 2 , 1, 1)
        self.gridLayout.addWidget(self.btn_multipliation, 3, 3 , 1, 1)
        self.gridLayout.addWidget(self.btn_4, 4, 0 , 1, 1)
        self.gridLayout.addWidget(self.btn_5, 4, 1 , 1, 1)
        self.gridLayout.addWidget(self.btn_6, 4, 2 , 1, 1)
        self.gridLayout.addWidget(self.btn_substraction, 4, 3 , 1, 1)
        self.gridLayout.addWidget(self.btn_1, 5, 0, 1, 1)
        self.gridLayout.addWidget(self.btn_2, 5, 1 , 1, 1)
        self.gridLayout.addWidget(self.btn_3, 5, 2 , 1, 1)
        self.gridLayout.addWidget(self.btn_addition, 5, 3 , 1, 1)
        self.gridLayout.addWidget(self.btn_0, 6, 1 , 1, 1)
        self.gridLayout.addWidget(self.btn_dot, 6, 2 , 1, 1)
        self.gridLayout.addWidget(self.btn_equal, 6, 3 , 1, 1)

        for i in range(self.gridLayout.count()):
            item = self.gridLayout.itemAt(i).widget()
            if isinstance(item, QtWidgets.QPushButton):
                item.setFixedSize(64, 64)






app = QtWidgets.QApplication([])
win = Calculator()
win.show()
app.exec_()