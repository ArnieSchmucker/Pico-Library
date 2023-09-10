from stepper_ajs import stepper
import time

motor = stepper(17,16,18,19,1,400,.1)

init_data = motor.get_init_data()
motor.begin()

def interval_mapping(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

steps_old = 0
angle_old = 90

while True:
    req_angle = float(input("Enter angle: "))
    trans_angle = interval_mapping(req_angle, 0,180,-90,90)
    delta_angle = req_angle - angle_old
    angle_old = req_angle
    n_steps = int(delta_angle/1.8*5)
    #print(req_angle, trans_angle, delta_angle,angle_old)
    if n_steps >=0:
        for i in range(n_steps):
            motor.stepCW()
            #time.sleep(.01)
    else:
          for i in range(abs(n_steps)):
            motor.stepCCW()
            #time.sleep(.01)
                        
    actual_position = motor.get_position_counter()
    actual_degrees = actual_position*1.8/5
    print(actual_degrees)
