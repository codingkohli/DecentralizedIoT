class Device:
    def __init__(self):
        "Init method to define the properties of the device"
        self.ip = None
        self.state = 1
        self.deviceID = 1
        self.managerIP = None
        self.burstMode = True



    def __setIPOfDevice(self,IP):
        self.ip = IP


    def __setIPOfManager(self,managerIP):
        self.managerIP = managerIP

    #"Methods specifically for a device"
    def receiveAction(self):
        if self.state == 1:
            self.state = 0
        else:
            self.state = 1
        return

    def receiveStateChange(self):
        if self.state == 1:
            self.state = 0
        else:
            self.state = 1
        return

    def forceUpdateMetadata(self,ip,managerIP):
        self.__setIPOfDevice(ip)
        self.__setIPOfManager(managerIP)
        return

    def setModeOperation(self):
        return

    def setModeCommunication(self):
        return

    def updateMetadata(self,ip,managerIP):
        self.__setIPOfDevice(ip)
        self.__setIPOfManager(managerIP)
        return
