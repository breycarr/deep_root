import RPi.GPIO as GPIO 
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

redlight = 18
bluelight = 11

GPIO.setup(redlight, GPIO.OUT)
GPIO.setup(bluelight, GPIO.OUT)

class Light():
         
    def red():
      print("Soil too dry")
      GPIO.output(self.redlight, True)
      GPIO.output(self.bluelight, False)

    def blue():
      print("Soil too wet")
      GPIO.output(self.bluelight, True)
      GPIO.output(self.redlight, False)

