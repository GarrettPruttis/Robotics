#Class PWM Controller *UNTESTED*
import RPi.GPIO as GPIO


class PWMController:

    # init

    #frequency is clock speed mhz - int
    
    def _init_(self,Frequency):

        self.frequency = Frequency
        self.outputs = []
        self.outputPins = []
        self.dc = []


    #getter method for frequency
    def get_frequency(self):
        return self.frequency

    #setter method for frequency
    #returns an int
    def set_frequency(self,Frequency):
        self.frequency = Frequency

    #getter method for outputs
    # return a list of all outputs -this will be object or strings
    def get_outputs(self):
        return self.outputs

    #initial setup for names of the pwm channels
    def set_outputs(self,output):
        self.outputs = output

    #getter method for all the output pins
    # returns a list of ints
    def get_output_pins(self):
        return self.outputPins

    #setter method for init setup of outputs
    #the pins correlate with the output channels
    def set_output_pins(self,output):
        self.outputPins = output

    #setups the outputs to PWM channels on Pi
    def setup(self):
        for pin in self.outputPins:
            GPIO.setup(pin, GPIO.OUT)

        for i in range(self.outputs):
            self.outputs[i] = GPIO.PWM(self.outputPins[i],self.frequency)

    #starts pwm
    def start(self):
        for i,channel in enumerate(self.outputs):
            channel.start(self.dc[i])
    #stops pwm
    def stop(self):
        for channel in self.outputs:
            channel.stop()

    #changes pwm duty cycle
    def setDC(self,channel,DC):
        self.outputs[self.outputs.index(channel)].ChangeDutyCycles(DC)
    
        
