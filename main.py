from gpiozero import Button
from flask import Flask
from actuator import Actuator    

app = Flask(__name__)

pin1 = 14
pin2 = 27

actuator = Actuator(pin1, pin2)

#Tried using the debounce option but it isn't working as expected
#This bug is confirmed by the interwebs...
greenButton = Button(4, pull_up = False)
redButton = Button(17, pull_up = False)

greenButton.when_pressed = actuator.Work
redButton.when_pressed = actuator.Home

@app.route('/', methods=['GET'])
def home():
    return "Hello actuator world!"

@app.route('/actuator/', methods=['GET'])
def actuatorMain():
    return "You are trying to call actuator! " + str(actuator)

@app.route('/actuator/work', methods=['GET'])
def actuatorWork():
    actuator.Work()
    return str(actuator.IsAtWork())

@app.route('/actuator/home', methods=['GET'])
def actuatorHome():
    actuator.Home()
    return str(actuator.IsAtHome())

@app.route('/actuator/off', methods=['GET'])
def actuatorOff():
    #actuator.Off()
    return str(actuator.Off())

@app.route('/actuator/position', methods=['GET'])
def actuatorPosition():
    return str(actuator)


if (__name__) == '__main__':
    print("Starting server")
    app.run(debug = True,
            #host='0.0.0.0',
            use_reloader = False)