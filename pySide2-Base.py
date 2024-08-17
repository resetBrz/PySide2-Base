# Importa o PySide2 / Import PySide2
# For install PySide2 use "pip install pyside2"
import sys
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget

# Define a janela / Def the window
class rawWindow(QWidget):
    def __init__(self):
        super().__init__()
        # Define o nome da janela e seu tamanho / Def window name and size
        self.setWindowTitle("Example")
        self.setGeometry(100, 100, 400, 200)

# Mostra a janela / Show the Window
myApp = QApplication(sys.argv)
window = rawWindow()
window.show()
myApp.exec_()
sys.exit(0)
