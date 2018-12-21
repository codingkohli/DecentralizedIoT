from Device import Device
from dbConnection import DBConnection
from flask import Flask
from datetime import datetime
import requests
from status_led import status_change_led

app = Flask(__name__)
# creating the device object
lotSensor = Device()

# create the database connection for it
deviceCon = DBConnection()
if deviceCon.createConnection():
    print("Conection successfully")

def setupApp():
    # setting up the base tables for the database
    deviceCon.setupTables()

    # registering the lot with the manager
    requests.get('http://localhost:8000/registerDevice',params={'deviceID':'1'})




# write the API's for it
@app.route("/")
def home():
    return "Home app of the Device App"

@app.route("/receiveStateChange")
def receiveStateChange():
    lotSensor.receiveStateChange()
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # communicate to the manager
    requests.get('http://localhost:8000/receiveStateChange',params={'device':'lot'})
    status_change_led(lotSensor.state,16,15)
    #deviceCon.executeQuery("""Insert into lot_Info(lot_ID,is_available,lot_timestamp) VALUES (%s,%s,%s)""",(lotSensor.deviceID,lotSensor.state,timestamp))

    return str(lotSensor.state)

@app.route("/receiveAction")
def receiveAction():
    lotSensor.receiveAction()
    return str(lotSensor.state)


if __name__  == "__main__":
    setupApp()
    app.run(host='0.0.0.0',port=7000,debug=True,use_reloader=False)


