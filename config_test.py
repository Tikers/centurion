import json

config_file = 'config.json'
with open(config_file) as f:
    conf = json.loads(f.read())

print(conf['RPi']['left_motor'])