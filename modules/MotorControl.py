#! /usr/bin/python3

# for debug:
import time

import RPi.GPIO as GPIO
import json
from numpy import sign

config_file = 'config.json'
with open(config_file) as f:
    conf = json.loads(f.read())
    motors = conf['RPi']

# print(conf['RPi']['left_motor'])


# TODO correct way? Not yet in course
class DC_Error(Exception):
    """_summary_

    Args:
        Exception (_type_): _description_
    """
    pass


class RPiMotor:
    """
    control motor settings with the raspberry pi
    """

    # class TwoWayPWM(TwoWayMotor):
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
        GPIO.setup(forward_pin, GPIO.OUT)
        # self.__motor_type = "direct drive"
        if reverse_pin:
            self.__pin_reverse = reverse_pin
            GPIO.setup(reverse_pin, GPIO.OUT)
            # self.__motor_type = "bi directional"
        if pwm_pin:
            self.__pin_pwm = pwm_pin
            GPIO.setup(pwm_pin, GPIO.OUT)
            self.__pwm = GPIO.PWM(pwm_pin, pwm_freq)
            self.__duty_cycle = 0
            self.__pwm.start(self.__duty_cycle)
            # self.__motor_type = "PWM control"
        # set motors in to forward as default
        self.__set_direction()

    def __str__(self) -> str:
        str = "one direction"
        if self.__pin_reverse: str = "bi directional"
        if self.__pin_pwm: str + " with pwm control;" 
        str += self.__duty_cycle + " dutycicy"
        return str

    def __set_speed(self, desired_dc):
        if not self.__pin_pwm:
            # TODO correct way? Not yet in course
            raise DC_Error("No speed control!")
        else:
            desired_dc = abs(desired_dc) if abs(desired_dc) < 100 else 100
            self.__duty_cycle = desired_dc
            self.__pwm.ChangeDutyCycle(desired_dc)

    def __set_direction(self, forward=True):
        """set direction of the motor

        Args:
            forward (bool, optional): True if forward, False for reverse. Defaults to True.
        """
        # self.__forward = forward
        GPIO.output(self.__pin_forward, forward)
        if self.__pin_reverse:
            GPIO.output(self.__pin_reverse, not forward)

    def stop(self):
        GPIO.output(self.__pin_forward, False)
        if self.__pin_reverse:
            GPIO.output(self.__pin_reverse, False)

    def change_speed(self, delta):
        if not self.__pin_pwm:
            # TODO correct way? Not yet in course
            raise DC_Error("No speed control!")

        new_dc = self.__duty_cycle + delta
        new_direction = sign(new_dc)

        if new_direction != 0 and new_direction != sign(self.__duty_cycle):
            if new_direction == 1:
                self.__set_direction(True)
            else:
                self.__set_direction(False)
            pass
        self.__set_speed(new_dc)

    def get_active_dc(self) -> int:
        return self.__duty_cycle




def steer(motor, steer_rate):
    #-x move left at rate x, x move right at rate x
    #TODO we dont have motors yes... we dont want to pass motor...
    #TODO if motor already on minimum increase other side speed?
    if steer_rate < 0:
        #left.change_speed(-steer_rate)
        pass
    else:
        pass


def steer(speed_change):
    #TODO steering!!! of the robot
    return


def stop(left_motor, right_motor):
    left_motor.stop()
    right_motor.stop()

if __name__ == "__main__":
    
    GPIO.setmode(GPIO.BOARD)

    left_motor = RPiMotor(motors['left_motor']['forward'], 
                          motors['left_motor']['reverse'], 
                          motors['left_motor']['pwm'])
    right_motor = RPiMotor(motors['right_motor']['forward'], 
                          motors['right_motor']['reverse'], 
                          motors['right_motor']['pwm'])

    for i in range(4):
        left_motor.change_speed(20)
        right_motor.change_speed(20)
        print("DC= ", left_motor.get_active_dc())
        time.sleep(2) 
    stop(left_motor, right_motor)

    GPIO.cleanup()
