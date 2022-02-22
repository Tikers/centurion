#! /usr/bin/python3

import RPi.GPIO as GPIO



#TODO correct way? Not yet in course
class SpeedError(Exception):    
    """_summary_

    Args:
        Exception (_type_): _description_
    """
    pass


class RPiDCMotor:
    """control motor settings with the raspberry pi
    """


    #class TwoWayPWM(TwoWayMotor):
    def __init__(self, forward_pin, reverse_pin=False, pwm_pin=False):
        """
        set the pinout of the raspberry pi depending on the number of pins to use
        1 simple on off motor
        2 bi direcitonal
        3 single or multi direction with PWM controller eg wit L298n

        Args:
            forward_pin (_type_): Pin number for forward movement (or movement if only one)
            reverse_pin (bool, optional): Pin number for reverse movement. Defaults to False if not used.
            pwm_pin (bool, optional): Pin number for pwm/speed control. Defaults to False if not used.
        """
        
        self.__pin_forward = forward_pin
        GPIO.setup(forward_pin,GPIO.OUT)
        if reverse_pin:
            self.__pin_reverse = reverse_pin
            GPIO.setup(reverse_pin,GPIO.OUT)
        if pwm_pin: 
            self.__pin_pwm = pwm_pin
            GPIO.setup(forward_pin,GPIO.OUT)
            self.__current_dc = 0
            
        
    def set_speed(self, desired_dc):
        if not self.__pin_pwm:
            raise SpeedError("No speed control!") #TODO correct way? Not yet in course
        else:
            if desired_dc < -100 or desired_dc > 100:
                #TODO check for bi directional otherwhise
                raise SpeedError("Must be value between 0 and 100!") #TODO correct way? Not yet in course
        
            GPIO.PWM(self.__pin_pwm, desired_dc)

    def move_forward(self):
        GPIO.output(self.__pin_forward, True)
        if self.__pin_reverse:
            GPIO.output(self.__pin_reverse, False)

    def move_reverse(self):
        GPIO.output(self.__pin_forward, False)
        if self.__pin_reverse:
            GPIO.output(self.__pin_reverse, True)

    def change_direction(self):
        self.__current_dc *= -1
        #TODO ad change speed here for new current speed
        #TODO change direction of motor (LOW PRIO)
        
    def change_speed(self, delta):
        #TODO change speed increase and decrease
        new_speed = self.__current_dc + delta
        if sign(new_speed) != sign(self.__current_dc):
            #TODO change direction
            pass

    



if __name__ == "__main__":
    print("Main Started from MotroControl.py v2")
    
    GPIO.setmode(GPIO.BOARD)

    left_motor = RPiDCMotor(15, 13, 11)
    right_motor = RPiDCMotor(18 , 16, 22)



    GPIO.cleanup()
