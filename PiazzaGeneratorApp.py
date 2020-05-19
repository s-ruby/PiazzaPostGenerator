from text_generator2 import generate
import sys
from PyQt5 import QtWidgets, uic, QtGui

class App():
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        
        self.words = []

        self.window = uic.loadUi("untitled.ui")
        self.window.textEdit.setReadOnly(True)
        pixel = QtGui.QPixmap("litaiBackground3.jpg")
        self.window.label.setPixmap(pixel)
        
        self.window.comboBox.addItem("Week 1")
        self.window.comboBox.addItem("Week 2")
        self.window.comboBox.addItem("Week 3")
        self.window.comboBox.addItem("Week 4")
        self.window.comboBox.addItem("Week 5")
        self.window.comboBox.addItem("Week 6")

        self.window.pushButton.clicked.connect(self.buttonPushed)
        self.window.resetButton.clicked.connect(self.resetPushed)
        self.window.show()
        self.app.exec() 
          
    def buttonPushed(self):
        week = str(self.window.comboBox.currentText())[-1]
        words = generate(week)
        new_line = "".join(words)
        current_post = self.window.textEdit.toPlainText()
        self.window.textEdit.setText(current_post+  " " + new_line)
        
    def resetPushed(self):
        self.window.textEdit.setText("")


if __name__ == '__main__':
	a = App()