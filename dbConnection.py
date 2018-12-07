import sqlite3

class DBConnection:
    def __init__(self):
        conn = None

    def createConnection(self):
        self.conn = sqlite3.connect('sensorDB.db')
        return self.conn

    def setupTables(self):
        self.conn.execute('CREATE TABLE IF NOT EXISTS lot_Master (lot_ID integer PRIMARY KEY,is_available integer NOT NULL,lot_timestamp datetime)')
        self.conn.execute('CREATE TABLE IF NOT EXISTS vehicle_Master (vehicle_ID integer PRIMARY KEY,lot_assigned integer NOT NULL,vehicle_timestamp datetime)')
        self.conn.execute('CREATE TABLE IF NOT EXISTS lot_Info (lot_ID integer PRIMARY KEY,is_available integer NOT NULL,lot_timestamp datetime)')
        self.conn.execute('CREATE TABLE IF NOT EXISTS lot_Master (vehicle_ID integer PRIMARY KEY,is_exiting integer NOT NULL,lot_timestamp datetime)')
        return
    def executeQuery(self,query):
        try:
            self.conn.execute(query)
        except:
            return False
        return True

    def closeConnection(self):
        try:
            self.conn.close()
        except:
            return False
        return True


