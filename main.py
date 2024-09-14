from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow
import random

class Widget(QMainWindow):

    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.generate)

    def generate(self):
        signs=""
        if self.ui.checkBox.isChecked():
            signs +="qwertyuiopastddfghjklzxcvbnm"
        if self.ui.checkBox_2.isChecked():
            signs +="0123456789"
        
        result =""
        number = random.randint(5,10)
        for _ in range(number):
            result +=random.choice(signs)
        self.ui.label.setText(result)


app = QApplication([])
ex = Widget()
ex.show()
app.exec_()
