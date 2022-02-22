#! /usr/bin/python3



import RPi.GPIO as GPIO

"""
Motor init and controls
"""
class RPiMotor:
    __motor_type = ""

    #class TwoWayPWM(TwoWayMotor):
    def __init__(self, forward_pin, reverse_pin=False, pwm_pin=False):
#        TwoWayMotor.__init__(self, forward_pin, reverse_pin)
        
        self.__motor_forward = forward_pin
        GPIO.setup(forward_pin,GPIO.OUT)
        self.__motor_type = "Directional"

        if reverse_pin:
            self.__motor_reverse = reverse_pin
            GPIO.setup(reverse_pin,GPIO.OUT)
            self.__motor_type = "Bi Directional"
        elif pwm_pin: 
            self.__motor_pwm = pwm_pin
            GPIO.setup(forward_pin,GPIO.OUT)
            self.__motor_type = "Bi PWM"
        
    def set_speed(self):
        


    



if __name__ == "__main__":
    print("Main Started from MotroControl.py v2")
    
    GPIO.setmode(GPIO.BOARD)

    left_motor = RPiMotor(15)
    right_motor = RPiMotor(22 ,18 , 16)

    print(left_motor.__dict__)
    #print(None==False)
    GPIO.cleanup()
