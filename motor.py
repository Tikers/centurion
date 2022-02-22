#! /usr/bin/python3

import curses
import RPi.GPIO as GPIO


freq = 1000
p_start = 25

left_pwm = 11
left_forward = 15
left_back = 13
right_pwm = 22
right_forward = 18
right_back = 16

""" 
Set all the print to the desired configuration
"""
def config_pins():
    # BOARD refers to pin BVM refers to GPIO
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(left_pwm,GPIO.OUT)
    GPIO.setup(left_forward,GPIO.OUT)
    GPIO.setup(left_back,GPIO.OUT)
    GPIO.setup(right_pwm,GPIO.OUT)
    GPIO.setup(right_forward,GPIO.OUT)
    GPIO.setup(right_back,GPIO.OUT)

"""
increase the speed of the motors
"""
def increase_speed():
    
    return 0

def decrease_speed():

    return 0

def forward():
    GPIO.output(left_forward,True)
    GPIO.output(right_forward,True)
    GPIO.output(left_back,False)
    GPIO.output(right_back,False)

def reverse():
    GPIO.output(left_forward,False)
    GPIO.output(right_forward,False)
    GPIO.output(left_back,True)
    GPIO.output(right_back,True)
    
def steer_left():
    GPIO.output(left_forward,False)
    GPIO.output(right_forward,True)
    GPIO.output(left_back,True)
    GPIO.output(right_back,False)

def steer_right():
    GPIO.output(left_forward,True)
    GPIO.output(right_forward,False)
    GPIO.output(left_back,False)
    GPIO.output(right_back,True)

def stop():
    GPIO.output(left_forward,False)
    GPIO.output(right_forward,False)
    GPIO.output(left_back,False)
    GPIO.output(right_back,False)


if __name__ == "__main__":
    print("Simple motor controll started.\nPress 'q' to quit stop is 'z'")
    config_pins()
    
    left_pwm = GPIO.PWM(left_pwm,freq)
    right_pwm = GPIO.PWM(right_pwm,freq)
    
    left_dc = 25
    right_dc = 25
    
    left_pwm.start(left_dc)
    right_pwm.start(right_dc)

    # Get the curses window, turn off echoing of keyboard to screen, turn on
    # instant (no waiting) key response, and use special values for cursor keys
    screen = curses.initscr()
    curses.noecho() 
    curses.cbreak()
    screen.keypad(True)

    try:
        while True:   
            char = screen.getch()
            if char == ord('q'):
                break

            elif char == curses.KEY_UP:
                forward()
                left_dc += 5
                right_dc += 5
                
            elif char == curses.KEY_DOWN:
                reverse()
                left_dc -= 5
                right_dc -= 5
                
            elif char == curses.KEY_RIGHT:
                steer_right()
            elif char == curses.KEY_LEFT:
                steer_left()
            elif char == ord('z'):
                stop()
                left_dc = 25
                right_dc = 25
                
            left_pwm.ChangeDutyCycle(left_dc)
            right_pwm.ChangeDutyCycle(right_dc)
                
    finally:
        #Close down curses properly, inc turn echo back on!
        curses.nocbreak(); screen.keypad(0); curses.echo()
        curses.endwin()
        GPIO.cleanup()