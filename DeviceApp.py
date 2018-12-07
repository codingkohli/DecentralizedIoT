from Device import Device
from dbConnection import DBConnection
from flask import Flask
from datetime import datetime

app = Flask(__name__)
# creating the device object
lotSensor = Device()

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
    lotSensor.receiveStateChange()
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    #deviceCon.executeQuery("""Insert into lot_Info(lot_ID,is_available,lot_timestamp) VALUES (%s,%s,%s)""",(lotSensor.deviceID,lotSensor.state,timestamp))

    return str(lotSensor.state)

@app.route("/receiveAction")
def receiveAction():
    lotSensor.receiveAction()
    return str(lotSensor.state)


if __name__  == "__main__":
    app.run(host='0.0.0.0',debug=True)


