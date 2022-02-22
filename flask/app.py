#!/usr/bin/python3

'''
    Raspberry Pi GPIO Status and Control
'''
import RPi.GPIO as GPIO
from flask import Flask, render_template

app = Flask(__name__)


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
def config_io_pins():
    # BOARD refers to pin BVM refers to GPIO
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(left_pwm,GPIO.OUT)
    GPIO.setup(left_forward,GPIO.OUT)
    GPIO.setup(left_back,GPIO.OUT)
    GPIO.setup(right_pwm,GPIO.OUT)
    GPIO.setup(right_forward,GPIO.OUT)
    GPIO.setup(right_back,GPIO.OUT)

    
@app.route("/")
def index():
    # Read Sensors Status
#     ledRedSts = GPIO.input(ledRed)
#     ledYlwSts = GPIO.input(ledYlw)
#     ledGrnSts = GPIO.input(ledGrn)
    ledRedSts = 10
    ledYlwSts = 12
    ledGrnSts = 22
    templateData = {
              'title' : 'GPIO output Status!',
               'ledRed'  : ledRedSts,
               'ledYlw'  : ledYlwSts,
               'ledGrn'  : ledGrnSts,
        }
    return render_template('index.html', **templateData)
    
@app.route("/<deviceName>/<action>")
def action(deviceName, action):
    if deviceName == 'ledRed':
        print("Red")
    #     actuator = ledRed
    if deviceName == 'ledYlw':
        print("ylw")
    #     actuator = ledYlw
    if deviceName == 'ledGrn':
        print("Grn")
    #     actuator = ledGrn
   
    if action == "on":
        print("on")
        # GPIO.output(actuator, GPIO.HIGH)
    if action == "off":
        print("off")
        # GPIO.output(actuator, GPIO.LOW)
             
    # ledRedSts = GPIO.input(ledRed)
    # ledYlwSts = GPIO.input(ledYlw)
    # ledGrnSts = GPIO.input(ledGrn)
    ledRedSts = 10
    ledYlwSts = 12
    ledGrnSts = 22
    
    templateData = {
              'ledRed'  : ledRedSts,
              'ledYlw'  : ledYlwSts,
              'ledGrn'  : ledGrnSts,
    }
    return render_template('index.html', **templateData)


if __name__ == "__main__":
    config_io_pins()

    left_pwm = GPIO.PWM(left_pwm,freq)
    right_pwm = GPIO.PWM(right_pwm,freq)
    
    left_dc = 25
    right_dc = 25
    
    left_pwm.start(left_dc)
    right_pwm.start(right_dc)

    app.run(host='192.168.2.111', port=80, debug=True)

    #print("gets to end")
    GPIO.cleanup()