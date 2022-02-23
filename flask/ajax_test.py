#! /usr/bin/python3

from flask import Flask, render_template

app = Flask(__name__)


#rendering the HTML page which has the button
@app.route('/')
def json():
    return render_template('button_ajax.html')

#background process happening without any refreshing
@app.route('/background_process_test')
def background_process_test():
    print ("Hello")
    return ("nothing")



if __name__ == "__main__":
    
    app.run(host='192.168.2.111', port=5000, debug=True)
