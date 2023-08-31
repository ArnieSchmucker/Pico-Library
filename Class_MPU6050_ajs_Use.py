from Class_MPU6050_ajs import Inertial_Sensor
import time

s1 = Inertial_Sensor(1,2,3,400000)
s1.calibrate()
s1.print_cals()
s1.show()
while True:
    s1.read_data()
    #s1.print_data()
    s1.accel_angles()
    s1.print_accel_data()
    time.sleep(1)