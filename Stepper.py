rom machine import Pin
from time import sleep
stepPin = 17
dirPin = 16
ms1Pin = 18
ms2Pin = 19

# steps_per_revolution = 400
# rev_divider = 8

class stepper:
    
    def __init__(self,stepPin,dirPin,ms1Pin,ms2Pin,rev_multiplier, steps_per_revolution,time_delay):
        self.stepPin = stepPin
        self.dirPin = dirPin
        self.ms1Pin = ms1Pin
        self.ms2Pin = ms2Pin
        self.rev_multiplier = rev_multiplier
        self.steps_per_revolution = steps_per_revolution
        self.time_delay = time_delay
    
    def get_init_data(self):
        return self.stepPin,self.dirPin,self.ms1Pin,self.ms2Pin,self.rev_multiplier,self.steps_per_revolution,self.time_delay
    
    def begin(self):
        self.step = Pin(self.stepPin, Pin.OUT)
        self.dir = Pin(self.dirPin, Pin.OUT)
        self.ms1 = Pin(self.ms1Pin, Pin.OUT)
        self.ms2 = Pin(self.ms2Pin, Pin.OUT)
        if (self.rev_multiplier == 1):
            self.ms1.value(0)
            self.ms2.value(0)
        elif (self.rev_multiplier == 2):
            self.ms1.value(1)
            self.ms2.value(0)
        elif (self.rev_multiplier == 4):
            self.ms1.value(0)
            self.ms2.value(1)
        elif (self.rev_multiplier == 8):
            self.ms1.value(1)
            self.ms2.value(1)
        else:
            pass
            
        self.counts_per_revolution = self.steps_per_revolution * self.rev_multiplier
        self.position_counter = 0
        
#     def set_MSx_pins(): 
#         # MS1 MS2
#         # LL = Full Step
#         # HL = Half Step
#         # LH = Quarter Step
#         # HH = Eigth Step
#         if rev_divider == 1:
#             ms1Pin.value(0)
#             ms2Pin.value(0)
#         elif rev_divider == 2:
#             ms1Pin.value(1)
#             ms2Pin.value(0)
#         elif rev_divider == 4:
#             ms1Pin.value(0)
#             ms2Pin.value(1)    
#         elif rev_divider == 8:
#             ms1Pin.value(1)
#             ms2Pin.value(1)
# 
    def stepCW(self):
        self.dir.value(1)
        self.step.value(1)
        sleep(.01)
        self.step.value(0)
        self.position_counter += 1
        sleep(.01)
        
    def stepCCW(self):
        self.dir.value(0)
        self.step.value(1)
        sleep(.01)
        self.step.value(0)
        self.position_counter -= 1
        sleep(.01)
    
    def stepOff(self):
        self.step.value(0)
        
    def get_position_counter(self):
        return self.position_counter

    def multistepCW(self, n_steps):
        self.dir.value(1)
        for i in range(n_steps):
            self.step.value(1)
            sleep(.01)
            self.step.value(0)
            self.position_counter += 1
            sleep(.01)

    def multistepCCW(self, n_steps):
        self.dir.value(0)
        for i in range(n_steps):
            self.step.value(1)
            sleep(.01)
            self.step.value(0)
            self.position_counter -= 1
            sleep(.01)
