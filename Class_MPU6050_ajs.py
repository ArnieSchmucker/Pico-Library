from machine import Pin,PWM,I2C
from imu import MPU6050
import time
import math

class Inertial_Sensor:
    def __init__(self):
        self.name = 'Outer Classs'
        self.sensor = self.Sensor()
        
    def show(self):
        print(self.name)
        print(self.sensor)
        
    class Sensor:
        def __init__(self):
            self.name = 'Inner Class'
            self.i2c = I2C(1, sda=Pin(2), scl=Pin(3), freq=400000)
            self.mpu = MPU6050(self.i2c)
            
        def show(self):
            print(self.name)
            print(self.i2c)
            print(self.mpu)
            
        def read_data(self):
            self.accelX = self.mpu.accel.x
            self.accelY = self.mpu.accel.y
            self.accelZ = self.mpu.accel.z
            
        def print_data(self):
            print(self.accelX,self.accelY,self.accelZ)
        
# s1 = Inertial_Sensor()
# s1.show()
# 
# s2 = s1.sensor
# s2.show()
# s2.read_data()
# s2.print_data()