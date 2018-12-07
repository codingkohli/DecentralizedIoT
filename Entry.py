from Device import Device
from dbConnection import DBConnection
from flask import Flask
from flask import request
from datetime import datetime
import requests

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
    #timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    #deviceCon.executeQuery("""Insert into lot_Info(lot_ID,is_available,lot_timestamp) VALUES (%s,%s,%s)""",(lotSensor.deviceID,lotSensor.state,timestamp))
    requests.get('http://localhost:8000/receiveStateChange',params={'device':'entry'})

    return str(lotSensor.state)

@app.route("/receiveAction")
def receiveAction():
    lotSensor.receiveAction()
    result = -1
    # result if the parking parking lot had available slots or not
    result = request.args.get('result')
    print("The decision for the lot is: " +result)
    return str(result)


if __name__  == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)


