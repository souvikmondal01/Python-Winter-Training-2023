from sensorModule import Sensor

class AcceleratoMeter(Sensor):
    def showType(self):
        print(f"I am {self.name}")

class Gyro(AcceleratoMeter):
    def showType(self):
        print(f"This is {self.name} and location is at {self.location}")        

class GPS(Sensor):
    def __init__(self, name, location, recordDate,brand):
        super().__init__(name, location, recordDate)
        self.brand = brand 