from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QPushButton, QMessageBox
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSignal, QThread, QObject
from PyQt5.uic.uiparser import QtWidgets
import sys

class Ui(QMainWindow):
    def __init__(self):
        # Starts the UI
        super(Ui, self).__init__()