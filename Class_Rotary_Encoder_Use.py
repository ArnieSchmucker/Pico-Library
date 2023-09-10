#copied from Chris DeHut, Pico Interfacing with Quadrature Encoders

from Class_Rotary_Encoder import R_Encoder
import time



Enc_1= R_Encoder(12,13)
Enc_1.DisplayPins()
last_Enc_Counter = 0      #Preset variables for first encoder 
Enc_Counter = 0
Last_Qtr_Cntr = 0
Qtr_Cntr = 0
error = 0

while True:
    time.sleep(.01)
    Qtr_Cntr = round(Enc_1.Enc_Counter/4)
    if Qtr_Cntr != Last_Qtr_Cntr:
        print(Qtr_Cntr)
        last_Enc_Cntr = Enc_1.Enc_Counter
        Last_Qtr_Cntr = Qtr_Cntr   
