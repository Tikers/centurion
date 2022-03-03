#! /usr/bin/python3

# # from __future__ import division
import time
from flask import Flask
from flask import render_template


import RPi.GPIO as GPIO
from ..config import get_config
from ..modules.MotorControl import RPiMotor, stop

conf = get_config()

app = Flask(__name__)


GPIO.setmode(GPIO.BOARD)

left_motor = RPiMotor(conf['RPi']['left_motor']['forward'], 
                      conf['RPi']['left_motor']['reverse'], 
                      conf['RPi']['left_motor']['pwm'])
right_motor = RPiMotor(conf['RPi']['right_motor']['forward'], 
                       conf['RPi']['right_motor']['reverse'], 
                       conf['RPi']['right_motor']['pwm'])

# freq = 1000
# p_start = 25

# left_pwm = 11
# left_forward = 15
# left_back = 13
# right_pwm = 22
# right_forward = 18
# right_back = 16

# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(left_pwm,GPIO.OUT)
# GPIO.setup(left_forward,GPIO.OUT)
# GPIO.setup(left_back,GPIO.OUT)
# GPIO.setup(right_pwm,GPIO.OUT)
# GPIO.setup(right_forward,GPIO.OUT)
# GPIO.setup(right_back,GPIO.OUT)

# left_pwm = GPIO.PWM(left_pwm,freq)
# right_pwm = GPIO.PWM(right_pwm,freq)
# # right_pwm = GPIO.PWM

# left_dc = 50
# right_dc = 50

# left_pwm.start(left_dc)
# right_pwm.start(right_dc)



@app.route('/')
def index():
    return render_template('simple_links.html')

@app.route("/command/f")
def commandf():
    # GPIO.output(left_forward,True)
    # GPIO.output(right_forward,True)
    # GPIO.output(left_back,False)
    # GPIO.output(right_back,False)
    left_motor.change_speed(10)
    right_motor.change_speed(10)
    # time.sleep(1)
    return render_template('simple_links.html')    
    
@app.route("/command/b")
def commandb():
    # GPIO.output(left_forward,False)
    # GPIO.output(right_forward,False)
    # GPIO.output(left_back,True)
    # GPIO.output(right_back,True)
    # time.sleep(1)
    left_motor.change_speed(-10)
    right_motor.change_speed(-10)
    return render_template('simple_links.html')    

@app.route("/command/l")
def commandl():
    # GPIO.output(left_forward,False)
    # GPIO.output(right_forward,True)
    # GPIO.output(left_back,True)
    # GPIO.output(right_back,False)
    # time.sleep(1)
    left_motor.change_speed(-10)
    # right_motor.change_speed(10)
    return render_template('simple_links.html')    

@app.route("/command/r")
def commandr():
    # GPIO.output(left_forward,True)
    # GPIO.output(right_forward,False)
    # GPIO.output(left_back,False)
    # GPIO.output(right_back,True)
    # time.sleep(1)
    # left_motor.change_speed(10)
    right_motor.change_speed(-10)
    return render_template('simple_links.html')

if __name__ == '__main__':
    app.run(debug=True, host='192.168.2.111')
    GPIO.cleanup()
