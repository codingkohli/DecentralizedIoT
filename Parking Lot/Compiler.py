import yaml
"""
This file takes in input from the YAML file,
reads the inplementation specific info and
generates the executables to be run on the Iot devices in the network
"""

def loadConfigFile():
    try:
        config=yaml.load(open('Config.yaml'))
        return config
    except:
        print("File Not Found")
    return None

def generateEntryGate(config):
    if not config:
        return
    ManagerIP = config['manager_address']
    EntryGate = config['entry_gate']
    fPtrEntry = open('EntryConfig.txt',"w+")
    fPtrEntry.write(ManagerIP)
    fPtrEntry.write(EntryGate['operation_mode'])
    return

def generateParkingLot(config):
    if not config:
        return
    ManagerIP = config['manager_address']
    ParkingLot = config['parking_lot']
    fPtrEntry = open('ParkingLot.txt',"w+")
    fPtrEntry.write(ManagerIP)
    fPtrEntry.write(ParkingLot['operation_mode'])
    return

def generateExitGate(config):
    if not config:
        return
    ManagerIP = config['manager_address']
    ExitGate = config['exit_gate']
    fPtrEntry = open('ExitConfig.txt',"w+")
    fPtrEntry.write(ManagerIP)
    fPtrEntry.write(ExitGate['operation_mode'])
    return

config = loadConfigFile()
generateEntryGate(config)
generateParkingLot(config)
generateExitGate(config)
#print yaml.dump(yaml.load())