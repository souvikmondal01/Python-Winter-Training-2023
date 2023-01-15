class Sensor():
    def __init__(self, name, location, recordDate):
        self.name = name
        self.location = location
        self.recordDate = recordDate
        self.data = {}

    def addData(self, time, data):
        self.data["data"] = data
        self.data["time"] = time
        print(f"Received {len(data)} point")

    def clearData(self):
        self.data = {}
        print("Data cleared!!")