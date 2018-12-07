from Manager import Manager
from dbConnection import DBConnection
from flask import Flask
from flask import request
import requests


app = Flask(__name__)
# creating the device object
lotManager = Manager()

# create the database connection for it
managerCon = DBConnection()



if managerCon.createConnection():
    print("Conection successful")

print("Lots avaliable are: "+str(lotManager.lotsAvailable))

# write the API's for it
@app.route("/")
def home():
    return "Home app of the Manager App"

@app.route("/receiveStateChange")
def receiveStateChange():
    device = 'None'
    device = request.args.get('device')
    if device == 'lot':
        print("Request from:"+device)
    elif device == 'entry':
        print("Request from:" + device)
        res = checkAvailableSlots()
        requests.get('http://localhost:5000/receiveAction',params={'result':res})
    elif device == 'exit':
        requests.get('http://localhost:6000/receiveAction', params={'result': 1})
    else:
        print("No device")
    return "State Updated"

@app.route("/registerDevice")
def registerDevice():
    print("Lots availe at entering the mode"+str(lotManager.lotsAvailable))
    lotManager.recieveRegistration()
    deviceID = -1
    deviceID = request.args.get('deviceID')
    print("Parameters recieved are:"+deviceID)
    return "Device Registered"

@app.route("/deregisterDevice")
def deregisterDevice():
    lotManager.recieveDeRegistration()
    deviceID = -1
    deviceID = request.args.get('deviceID')
    print("Parameters recieved are:"+deviceID)
    return "Device De Registered"

@app.route("/checkAvailableSlots")
def checkAvailableSlots():
    if lotManager.lotsAvailable > 0:
        return str(lotManager.lotsAvailable)
    return "0"


if __name__  == "__main__":
    print("Restarting app")
    app.run(host='0.0.0.0',port=8000,debug=True)
