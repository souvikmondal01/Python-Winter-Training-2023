from sensorModule import Sensor
from my_sensors import AcceleratoMeter,Gyro,GPS
import numpy as np

acc = AcceleratoMeter(name="Accelerometer_v1",location="Haldia",recordDate="2023-01-10")
gyro = Gyro(name="Gyroscope_v1",location="Kolkata",recordDate="2023-01-10")
gps = GPS(name="GPS_v1",location="Deldhi",recordDate="2023-01-10",brand="espressif")


#get data
time = np.arange(10)
acc_data = np.random.randint(-20,20,10)
gyro_data = np.random.randint(-10,30,10)
gps_data = np.random.randint(-10,5,10)

#add data to sensors
acc.addData(data=acc_data,time=time)
gyro.addData(data=gyro_data,time=time)
gps.addData(data=gps_data,time=time)

#print data points
print("Acceleratometer data:",acc.data)
print("Gyroscope data:",gyro.data)
print("GPS data:",gps.data)