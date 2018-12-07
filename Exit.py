from Device import Device
from dbConnection import DBConnection
from flask import Flask
from datetime import datetime
import requests
from flask import request


app = Flask(__name__)
# creating the device object
exitSensor = Device()

# create the database connection for it
deviceCon = DBConnection()
if deviceCon.createConnection():
    print("Conection successful")

# setting up the base tables for the database
deviceCon.setupTables()


# write the API's for it
@app.route("/")
def home():
    return "Home app of the Device App"

@app.route("/receiveStateChange")
def receiveStateChange():
    exitSensor.receiveStateChange()
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    #deviceCon.executeQuery("""Insert into lot_Info(lot_ID,is_available,lot_timestamp) VALUES (%s,%s,%s)""",(lotSensor.deviceID,lotSensor.state,timestamp))
    requests.get('http://localhost:8000/receiveStateChange', params={'device': 'exit'})
    return str(exitSensor.state)

@app.route("/receiveAction")
def receiveAction():
    exitSensor.receiveAction()
    return str(exitSensor.state)


if __name__  == "__main__":
    app.run(host='0.0.0.0',port=6000,debug=True)


