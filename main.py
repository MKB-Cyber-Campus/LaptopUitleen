from UI import Ui
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QPushButton, QMessageBox
import sys

if __name__ == "main":
    app = QApplication(sys.argv)  # Create an instance of QtWidgets.QApplication
    window = Ui()  # Create an instance of our class
    app.exec_()  # Start the application