__config = {
    "RPi":{
        "left_motor":{
            "forward": 15,
            "reverse": 13,
            "pwm": 11
        },
        "right_motor":{
            "forward": 18,
            "reverse": 16,
            "pwm": 22
        }
    }
}

def get_config():
    return __config