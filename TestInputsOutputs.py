from gpiozero import Button, DigitalOutputDevice
from gpiozero.pins.rpigpio import RPiGPIOPin, RPiGPIOFactory
from time import sleep
from flask import Flask, request, jsonify

#Tried using the debounce option but it isn't working as expected
#This bug is confirmed by the interwebs...
greenButton = Button(4, pull_up = False)
redButton = Button(17, pull_up = False)

output1 = DigitalOutputDevice(27)
output2 = DigitalOutputDevice(14)
output1.on()

class Actuator():
    pin1 = 27
    pin2 = 14
    
    def __init__(self):
        output1 = DigitalOutputDevice(pin1)
        output2 = DigitalOutputDevice(pin2)
        
    def Work(self):
        output1.on()
        output2.off()
    
    def Home(self):
        output1.off()
        output2.on()
        
    def Off(self):
        output1.off()
        output2.off()


def PrintColor(button):
    print(type(button.pin))
    #if button.pin == RPiGPIOPin(None,4):
    if str(button.pin) == "GPIO4":
        print("Turning on output!")
        output1.on()
        output2.on()
    else:
        print("Turning off output")
        output1.off()
        output2.off()
        
    print(str(button.pin) + " was pressed!")

greenButton.when_pressed = PrintColor
redButton.when_pressed = PrintColor

while True:
#    if greenButton.is_pressed:
#        print("Pressed green!")
#    else:
#        print("Released green")
#    if redButton.is_pressed:
#        print("Pressed red!")
#    else:
#        print("Released red!")
    sleep(1)