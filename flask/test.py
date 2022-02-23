#! /user/bin/python3

from flask import Flask, render_template, Response, request, redirect, url_for
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('button.html')

@app.route("/forward/", methods=['POST'])
def move_forward():
    #Moving forward code
    forward_message = "Moving Forward..."
    return render_template('button.html', forward_message=forward_message);


if __name__ == "__main__":
    
    app.run(host='192.168.2.111', port=5000, debug=True)