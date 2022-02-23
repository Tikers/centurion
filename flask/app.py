#!/usr/bin/python3

'''
    Raspberry Pi GPIO Status and Control
'''
#import RPi.GPIO as GPIO

from flask import Flask, render_template

app = Flask(__name__)



    
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
    
    app.run(host='192.168.2.111', port=5000, debug=True)

    