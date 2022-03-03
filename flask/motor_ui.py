#! /usr/bin/python3

from centurion.modules.MotorControl import RPiMotor, stop
from centurion.config import get_config
from flask import Flask, render_template, Response, request, redirect, url_for
import RPi.GPIO as GPIO

conf = get_config()

app = Flask(__name__)

GPIO.setmode(GPIO.BOARD)
left_motor = RPiMotor(conf['RPi']['left_motor']['forward'], 
                      conf['RPi']['left_motor']['reverse'], 
                      conf['RPi']['left_motor']['pwm'])
right_motor = RPiMotor(conf['RPi']['right_motor']['forward'], 
                       conf['RPi']['right_motor']['reverse'], 
                       conf['RPi']['right_motor']['pwm'])

# @app.route("/motor")
# def index():

#     GPIO.setmode(GPIO.BOARD)
#     left_motor = RPiMotor(conf['RPi']['left_motor']['forward'], 
#                       conf['RPi']['left_motor']['reverse'], 
#                       conf['RPi']['left_motor']['pwm'])
#     right_motor = RPiMotor(conf['RPi']['right_motor']['forward'], 
#                        conf['RPi']['right_motor']['reverse'], 
#                        conf['RPi']['right_motor']['pwm'])

#     templateData = {
#     #   'title' : 'GPIO input Status!',
#       'current_dc': left_motor.get_active_dc(),
#       'direction': 0
#     }
#     return render_template('motor.html', **templateData)


#TODO via action or form? What is difference?
@app.route("/<action>",  methods=('GET', 'POST'))
def action(action):

    # print("some action: " + action)
    if request.method == 'POST':
        # print("Post")
        # if action == "forward":
            # print("forward")
            # GPIO.output(actuator, GPIO.HIGH)
        # if action == "reverse":
            # print("reverse")
            # GPIO.output(actuator, GPIO.LOW)
        if request.form["submit_button"] == 'forward':
            print("form forward")
            left_motor.change_speed(10)
            # right_motor.change_speed(20)
        elif request.form["submit_button"] == 'reverse':
            print("form reverse")
            left_motor.change_speed(-10)
        elif request.form["submit_button"] == 'left':
            print("form left")
        elif request.form["submit_button"] == 'right':
            print("form right")
        elif request.form["submit_button"] == 'stop':
            print("form stop")
            left_motor.stop()


    templateData = {
    #   'title' : 'GPIO input Status!',
      'current_dc': left_motor.get_active_dc,
      'direction': 0
    }
             
    return render_template('motor.html', **templateData)


if __name__ == "__main__":  
    # GPIO.setmode(GPIO.BOARD)

    # left_motor = RPiMotor(conf['RPi']['left_motor']['forward'], 
    #                       conf['RPi']['left_motor']['reverse'], 
    #                       conf['RPi']['left_motor']['pwm'])
    # right_motor = RPiMotor(conf['RPi']['right_motor']['forward'], 
    #                       conf['RPi']['right_motor']['reverse'], 
    #                       conf['RPi']['right_motor']['pwm'])

    # for i in range(4):
        # left_motor.change_speed(20)
        # right_motor.change_speed(20)
        # print("DC= ", left_motor.get_active_dc())
        # time.sleep(2) 
    # stop(left_motor, right_motor)

    # GPIO.cleanup()

    app.run(host='192.168.2.111', port=5000, debug=True)
    print("bye!")
    GPIO.cleanup()