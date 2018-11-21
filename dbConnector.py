import sqlite3

conn = sqlite3.connect('sensorDB.db')
print("Connection to database established")

conn.execute('CREATE TABLE IF NOT EXISTS lot_Master (lot_ID integer PRIMARY KEY,is_available integer NOT NULL,lot_timestamp datetime)')
print("Create for lot_Master successful")

conn.execute('CREATE TABLE IF NOT EXISTS vehicle_Master (vehicle_ID integer PRIMARY KEY,lot_assigned integer NOT NULL,vehicle_timestamp datetime)')
print("Create for vehicle_Master successful")

conn.execute('CREATE TABLE IF NOT EXISTS lot_Info (lot_ID integer PRIMARY KEY,is_available integer NOT NULL,lot_timestamp datetime)')
print("Create for lot_Info successful")

conn.execute('CREATE TABLE IF NOT EXISTS lot_Master (vehicle_ID integer PRIMARY KEY,is_exiting integer NOT NULL,lot_timestamp datetime)')
print("Create for lot_Master successful")

conn.close()
print("Connection closed successfully")
