class Sensor():
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.__recordDate = "2023-01-10"
        self.__version = "0.001"
        self.data = {}

    def getRecordDate(self):
        print(f"The record date for {self.name} is {self.__recordDate}")

    def getVersion(self):
        print(f"The version for {self.name} is {self.__version}")

    def setVersion(self, version):
        self.__version = version
        print(f"The version for {self.name} is now {self.__version} ")

    def addData(self, time, data):
        self.data["data"] = data
        self.data["time"] = time
        print(f"Received {len(data)} point")

    def clearData(self):
        self.data = {}
        print("Data cleared!!")


Sensor1 = Sensor(name="Sensor1", location="Kolkata")
print(Sensor1.name)
print(Sensor1.location)
# print(Sensor1.__recordDate)
# print(Sensor1.__version)


Sensor1.getRecordDate()
Sensor1.getVersion()
Sensor1.setVersion("0.009")
Sensor1.getVersion()


