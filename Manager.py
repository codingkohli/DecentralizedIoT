class Manager:
    def __init__(self):
        "Init method to define the properties of the manager"
        self.ip = None
        self.lotsAvailable = 0
        self.capacity = 0

    def __setIPOfDevice(self,IP):
        self.ip = IP

    def __setAvailableLots(self,n):
        self.lotsAvailable = n
        self.capacity = n

    def recieveStateChange(self):
        return

    def recieveHeartBeat(self):
        return

    def recieveRegistration(self):
        print("Lot before it is"+str(self.lotsAvailable))
        self.lotsAvailable += 1
        return

    def recieveDeRegistration(self):
        self.lotsAvailable -= 1
        return

    def updateMetadata(self):
        return


