from gpiozero import DigitalOutputDevice


class Actuator:
    def __init__(self, pin1, pin2):
        print("Instantiated actuator with pin1 = " + str(pin1) + " and pin2 = " + str(pin2))
        self.pin1 = pin1
        self.pin2 = pin2
        self.atWork = False
        self.atHome = False
        self.output1 = DigitalOutputDevice(pin1)
        self.output2 = DigitalOutputDevice(pin2)
        
    def __str__(self):
        return "Actuator's position is " + self.Position() + ". Pin1 = " + str(self.pin1) + " and Pin2 = " + str(self.pin2)

    def __repr__(self):
        return "Actuator(" + str(self.pin1) + ", " + str(self.pin2)
    
    def Work(self):
        self.output1.on()
        self.output2.off()
        self.atHome = False
        self.atWork = True
        print("Sending actuator to work! Output1 is On. Output 2 is Off")
    
    def Home(self):
        self.output1.off()
        self.output2.on()
        self.atHome = True
        self.atWork = False
        print("Sending actuator to home! Output1 is Off. Output 2 is On")
        
    def Off(self):
        self.output1.off()
        self.output2.off()
        print("Sending actuator nowhere! Output1 is Off. Output 2 is Off")
        
    def IsAtHome(self):
        return self.atHome
    
    def IsAtWork(self):
        return self.atWork
    
    def Position(self):
        if self.atHome:
            position = 'at home'
        elif self.atWork:
            position = 'at work'
        else:
            position = 'unknown'
        return position
        
        
