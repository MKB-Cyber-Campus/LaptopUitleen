from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QPushButton, QMessageBox
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSignal, QThread, QObject
from PyQt5.uic.uiparser import QtWidgets
import sys

class Ui(QMainWindow):
    def __init__(self):
        '''
        Start de UI        
        '''
        super(Ui, self).__init__()
        uic.loadUi("C:/Users/marti/Dropbox/Hacklab/Opdrachten/LaptopUitleen/LaptopUitleen/LaptopUitleen/LaptopUitleenUI.ui", self)
        self.show()
        self.RegistreerUitleenButton.clicked.connect(self.RegistreerUitleenButtonClicked)
        self.ZoekUitleenButton.clicked.connect(self.ZoekUitleenButtonClicked)
        self.ExporteerNaarExcelButton.clicked.connect(self.ExporteerNaarExcelButtonClicked)
        self.ToggleFullscreenButton.clicked.connect(self.ToggleFullscreenButtonClicked)

    def WarnMSG(self, type):
        '''
        Geeft een waarschuwing weer met uitleg als er fouten worden opgevangen

        Args:
            type: Het type waarschuwing        
        '''
        msg = QMessageBox()
        msg.setWindowTitle("Er is iets fout gegaan")
        messagewarnings = {"EmptyPersoonBarcode" : "Het veld Leerling/Leraar barcode is leeg!",
                           "EmptyLaptopBarcode" : "Het veld Laptop Barcode is leeg!",
                           "EmptySearchBarcode" : "Het veld Zoek op Barcode is leeg!"}
        msg.setText(messagewarnings[type])
        msg.setIcon(QMessageBox.Warning)
        msg.exec_()

    def RegistreerUitleenButtonClicked(self):
        '''
        Registreet de uitleen van een laptop.
        Neemt de input van de textboxes Leerling/Leraar Barcode en Laptop Barcode en verstuurt deze naar de data handler die het verder afhandelt.
        '''
        PersoonBarcode = self.GetPersonBarcode()
        LaptopBarcode = self.GetLaptopBarcode()

        if PersoonBarcode == "":
            self.WarnMSG("EmptyPersoonBarcode")
            return
        if LaptopBarcode == "":
            self.WarnMSG("EmptyLaptopBarcode")
            return

    def ZoekUitleenButtonClicked(self):
        '''
        Zoekt een uitleen op basis van een ingevoerde barcode. Dit kan een Gebruiker of een Laptop barcode zijn.
        '''
        ZoekBarcode = self.GetSearchBarcode()
        if ZoekBarcode == "":
            self.WarnMSG("EmptySearchBarcode")
            return
        

    def ExporteerNaarExcelButtonClicked(self):
        '''
        Exporteert de gegevens naar een excel bestand wat makkelijk leesbaar is
        '''
        # Kijken of dit met Pandas goed wil, anders oude unit gebruiken
        pass

    def ToggleFullscreenButtonClicked(self):
        '''
        Switched het scherm naar fullscreen (en terug)
        '''
        if self.isFullScreen() == True:
            self.showNormal()
            self.ToggleFullscreenButton.setText("Toggle Fullscreen")
        else:
            self.showFullScreen()
            self.ToggleFullscreenButton.setText("Toggle Windowed")

    def GetPersonBarcode(self):
        '''
        Functie om Leerling/Leraar barcode uit de textbox te halen

        Return:
            De text uit PersoonBarcodeLineEdit
        '''
        return self.PersoonBarcodeLineEdit.text()

    def GetLaptopBarcode(self):
        '''
        Functie om Laptop barcode uit de textbox te halen

        Return:
            De text uit LaptopBarcodeLineEdit
        '''
        return self.LaptopBarcodeLineEdit.text()

    def GetSearchBarcode(self):
        '''
        Functie om te zoeken barcode uit de textbox te halen

        Return
            De text uit ZoekLaptopBarcodeLineEdit
        '''
        return self.ZoekLaptopBarcodeLineEdit.text()

if __name__ == "__main__":
    app = QApplication(sys.argv)  # Create an instance of QtWidgets.QApplication
    window = Ui()  # Create an instance of our class
    app.exec_()  # Start the application    