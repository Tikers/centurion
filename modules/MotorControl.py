#! /usr/bin/python3

#for debug:
import time

import RPi.GPIO as GPIO
from numpy import sign


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
    def __init__(self, forward_pin, reverse_pin=False, pwm_pin=False, pwm_freq=100):
        """
        set the pinout of the raspberry pi depending on the number of pins to use
        1 simple on off motor
        2 bi direcitonal
        3 single or multi direction with PWM controller eg wit L298n

        Args:
            forward_pin (int): Pin number for forward movement (or movement if only one)
            reverse_pin (int, optional): Pin number for reverse movement. Defaults to False if not used.
            pwm_pin (int, optional): Pin number for pwm/speed control. Defaults to False if not used.
            pwm_freq (int, optional): Set PWM frequency. Defaults to 1000Hz
        """
        
        self.__pin_forward = forward_pin
        GPIO.setup(forward_pin,GPIO.OUT)
        if reverse_pin:
            self.__pin_reverse = reverse_pin
            GPIO.setup(reverse_pin,GPIO.OUT)
        if pwm_pin: 
            self.__pin_pwm = pwm_pin
            GPIO.setup(pwm_pin,GPIO.OUT)
            self.__pwm = GPIO.PWM(pwm_pin,pwm_freq)
            # set duty cycle to 0 #TODO check if this is always off!
            self.__duty_cycle = 0
            self.__pwm.start(self.__duty_cycle)
        
        # set motors in to forward motion as default
        self.__set_direction()



        
    def set_speed(self, desired_dc):
        if not self.__pin_pwm:
            raise SpeedError("No speed control!") #TODO correct way? Not yet in course
        else:
            min = 0 if not self.__pin_reverse else -100
            if min < desired_dc or desired_dc > 100:
                raise SpeedError("Must be value between 0 and 100!") #TODO correct way? Not yet in course
            else:
                self.__duty_cycle = desired_dc
                self.__pwm.ChangeDutyCycle(desired_dc)
            

    def __set_direction(self, forward=True):
        self.__forward = forward
        GPIO.output(self.__pin_forward, forward)
        if self.__pin_reverse:
            GPIO.output(self.__pin_reverse, not forward)
        
    # changed move forwarde to set direction this makes reverse and change direction redundant
    # def __move_reverse(self):
    #     GPIO.output(self.__pin_forward, False)
    #     if self.__pin_reverse:
    #         GPIO.output(self.__pin_reverse, True)
    #     self.__forward = False

    # def __change_direction(self):
    #     #self.__duty_cycle *= -1
    #     if self.__forward:
    #         self.__move_reverse
    #     else:
    #         self.__set_direction
        

    def stop(self):
        GPIO.output(self.__pin_forward, False)
        if self.__pin_reverse:
            GPIO.output(self.__pin_reverse, False)
        

    def change_speed(self, delta):
        if not self.__pin_pwm:
            raise SpeedError("No speed control!") #TODO correct way? Not yet in course
        new_speed = self.__duty_cycle + delta
        new_direction = sign(new_speed)
        if new_direction != sign(self.__duty_cycle):
            if not new_direction: #sign = 0

            #TODO change direction
            return 0
        #TODO check for min max overload (maybe use set speed and update that?)
        else:
            self.__duty_cycle = new_speed
            self.__pwm.ChangeDutyCycle(new_speed)
            
    def get_active_dc(self):
        return self.__duty_cycle


# def sign(val):
#     """Simple function to check if value is possitive (False) or negative (1)

#     Args:
#         val (number): number to validate

#     Returns:
#         bool: True if < 0 else False
#     """
#     return True if val < 0 else False

def steer(speed_change):
    return


if __name__ == "__main__":
    print("Main Started from MotroControl.py v2")
    
    GPIO.setmode(GPIO.BOARD)

    left_motor = RPiDCMotor(15, 13, 11)
    right_motor = RPiDCMotor(18 , 16, 22)

    for i in range(4):
        left_motor.change_speed(25)
        right_motor.change_speed(25)
        print("DC= ", left_motor.get_active_dc())
        time.sleep(2) 

    GPIO.cleanup()
