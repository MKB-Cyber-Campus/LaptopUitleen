import sqlite3

class DataHandler():
    def __init__(self):
        '''
        The init establishes the connection with the database, and creates 
        '''
        conn = sqlite3.connect('laptop_uitleningen.db')
        c = conn.cursor()
        self.CreateTable(c, conn)

    def CreateTable(self, c, conn):
        '''
        Creates a table with specific parameters within the database
        
        Args:
            c : A database cursor that allows us to interact with the database
            conn : The connection to the database
        
        '''
        c.execute('''CREATE TABLE IF NOT EXISTS uitleenregistraties (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                leerling_medewerker_barcode TEXT,
                laptop_barcode TEXT,
                uitgifte_datum TEXT,
                inleverdatum TEXT,
                verwijderd INTEGER DEFAULT 0
            )''')
        conn.commit()

    def DataWrite(self, PersoonBarcode, LaptopBarcode, Datum):
        '''
        Schrijft de combinatie van Persoon, Laptop en Datum naar de database
        Args:
            PersoonBarcode: Barcode nummer van een persoon die een laptop leent
            LaptopBarcode: Barcode nummer van een laptop die door een persoon wordt geleend
            Datum: Datum waarop de laptop wordt geleend
        '''
        pass

    def DataSearch(self, ZoekBarcode):
        '''
        Zoekt op een Barcode, om de omringende data op te halen die er bij hoort
        '''
        pass

    def DataDump(self):
        '''
        Leest de data uit de database file, en schrijft deze weg naar een excel bestand
        '''
        pass
