import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from sudokuwindow import Ui_Sudoku

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Sudoku()
        self.ui.setupUi(self)
        self.ui.button_1.clicked.connect(self.counter)
        self.ui.exit.clicked.connect(self.exit)

    def counter(self):
        text = self.ui.counter.text()
        try:
            self.ui.counter.setText(str(int(text) + 1))
        except Exception as e:
            print('Error occured in method change_exucution: ', e)

    def exit(self):
        global app
        sys.exit(app.exec())

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())