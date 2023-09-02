from machine import Pin,PWM,I2C
from imu import MPU6050
import time
import math
        
class Inertial_Sensor:
    def __init__(self,chan,sdaPin,sdlPin,freq=400000):
        self.name = 'MPU6050 Sensor'
        self.chan = chan
        self.sdaPin = sdaPin
        self.sdlPin = sdlPin
        self.freq = freq
        self.i2c = I2C(self.chan, sda=Pin(self.sdaPin), scl=Pin(self.sdlPin), freq=self.freq)
        self.mpu = MPU6050(self.i2c)
        
    def show(self):
        print(self.name)
        print(self.i2c)
        print(self.mpu)
        
    def calibrate(self,cal_ax=0,cal_ay=0,cal_az=0,cal_gx=0,cal_gy=0,cal_gz=0):
        self.cal_ax=cal_ax
        self.cal_ay=cal_ay
        self.cal_az=cal_az
        self.cal_gx=cal_gx
        self.cal_gy=cal_gy
        self.cal_gz=cal_gz
        
    def print_cals(self):
        print(self.cal_ax,self.cal_ay,self.cal_az,self.cal_gx,self.cal_gy,self.cal_gz)
        
    def read_data(self):
        self.accelX = self.mpu.accel.x-self.cal_ax
        self.accelY = self.mpu.accel.y-self.cal_ay
        self.accelZ = self.mpu.accel.z-self.cal_az
        self.gyroX = self.mpu.gyro.x-self.cal_gx
        self.gyroY = self.mpu.gyro.y-self.cal_gy
        self.gyroZ = self.mpu.gyro.z-self.cal_gz
        
    def print_data(self):
        print(self.accelX,self.accelY,self.accelZ,self.gyroX,self.gyroY,self.gyroZ)
        
    def accel_angles(self):
        self.angles_AX = math.atan2(self.accelX,self.accelZ)*57.3
        self.angles_AY=math.atan2(self.accelY,self.accelZ)*57.3
        
    def print_accel_data(self):
        print("inclination X: {:.3f} inclination Y: {:.3f}".format(self.angles_AX,self.angles_AY))
        
#     def get_accelA_X(self):
#         return anglesA[0]
# 
#     def get_accelA_Y(self):
#         return anglesA[1]
        
# s1 = Inertial_Sensor()
# s1.show()
# 
# s2 = s1.sensor
# s2.show()
# s2.read_data()
# s2.print_data()
