import sqlite3

class DataHandler():
    def __init__(self):
        '''
        The init establishes the connection with the database, and creates 
        '''
        self.conn = sqlite3.connect('laptop_uitleningen.db')
        self.c = self.conn.cursor()
        self.CreateTable()

    def CreateTable(self):
        '''
        Creates a table with specific parameters within the database
        
        Args:
            c : A database cursor that allows us to interact with the database
            conn : The connection to the database
        
        '''
        self.c.execute('''CREATE TABLE IF NOT EXISTS uitleenregistraties (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                leerling_medewerker_barcode TEXT,
                laptop_barcode TEXT,
                uitgifte_datum TEXT,
                inleverdatum TEXT,
                verwijderd INTEGER DEFAULT 0
            )''')
        self.conn.commit()

    def DataWrite(self, PersoonBarcode, LaptopBarcode, Datum):
        '''
        Schrijft de combinatie van Persoon, Laptop en Datum naar de database
        Args:
            PersoonBarcode: Barcode nummer van een persoon die een laptop leent
            LaptopBarcode: Barcode nummer van een laptop die door een persoon wordt geleend
            Datum: Datum waarop de laptop wordt geleend
        '''
        self.c.execute("INSERT INTO uitleenregistraties (leerling_medewerker_barcode, laptop_barcode, uitgifte_datum) VALUES (?, ?, ?)", 
              (PersoonBarcode, LaptopBarcode, Datum))
        self.conn.commit()

    def DataSearch(self, ZoekBarcode):
        '''
        Zoekt op een Barcode, om de omringende data op te halen die er bij hoort
        '''
        self.c.execute("SELECT * FROM uitleenregistraties WHERE (leerling_medewerker_barcode = ? OR laptop_barcode = ?) AND inleverdatum IS NULL ORDER BY uitgifte_datum DESC", 
              (ZoekBarcode, ZoekBarcode))
        resultaten = self.c.fetchall()
        return resultaten[0]

    def DataDump(self):
        '''
        Leest de data uit de database file, en schrijft deze weg naar een excel bestand
        
        Return:
            De data uit het .db bestand
        '''
        self.c.execute("SELECT * FROM uitleenregistraties")
        registraties = self.c.fetchall()
        return registraties
