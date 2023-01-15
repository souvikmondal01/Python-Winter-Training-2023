import numpy as np


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


sensor1 = Sensor(name="sensor1", location="Haldia", recordDate="2023-01-09")

print(sensor1.name, sensor1.location, sensor1.recordDate)

# generatig random data points of length 10
data = np.random.randint(-10, 10, 10)
# generating random time in seconds corresponding to the points above
time = np.arange(10)
print(data)
print(time)

# adding the generated data points into the sensor object
sensor1.addData(time=time, data=data)

# printing the sensor dictionary within the class
print(sensor1.data)

print("-------------------------------------------")


class AcceleratoMeter(Sensor):
    def showType(self):
        print(f"I am {self.name}")


acc = AcceleratoMeter("acceleratometer", "Haldia", "2023-01-09")

acc.showType()

acc.addData(data=data, time=time)
print(acc.data)


class Gyro(AcceleratoMeter):
    def showType(self):
        print(f"This is {self.name} and location is at {self.location}")


gyro = Gyro(name="Gyroscoppe", location="Kolkata", recordDate="2023-01-10")

gyroData = np.random.randint(-25, 5, 10)
gyroTime = np.arange(10)

gyro.addData(data=gyroData, time=gyroTime)

gyro.showType()


print("##############################################")
class GPS(Sensor):
    def __init__(self, name, location, recordDate,brand):
        super().__init__(name, location, recordDate)
        self.brand = brand    


gps = GPS(name="GPS",location="Delhi",recordDate="2023-01-10",brand="espressif")

print(gps.name,gps.location,gps.recordDate)
print(gps.brand)

