#! /usr/bin/python3

from flask import Flask, render_template, Response, request, redirect, url_for
app = Flask(__name__)

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
        elif request.form["submit_button"] == 'reverse':
            print("form reverse")
        elif request.form["submit_button"] == 'left':
            print("form left")
        elif request.form["submit_button"] == 'right':
            print("form right")
        elif request.form["submit_button"] == 'stop':
            print("form stop")
             
    return render_template('button.html')


if __name__ == "__main__":  
    app.run(host='192.168.2.111', port=5000, debug=True)