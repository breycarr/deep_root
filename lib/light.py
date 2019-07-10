import RPi.GPIO as GPIO 
import time

class Light():
            
      def __init__(self, redlight = 18, bluelight = 11):
            self.redlight = redlight
            self.bluelight = bluelight
            GPIO.setmode(GPIO.BCM)
            GPIO.setwarnings(False)
            GPIO.setup(redlight, GPIO.OUT)
            GPIO.setup(bluelight, GPIO.OUT)

      def red(self):
            GPIO.output(self.redlight, True)
            GPIO.output(self.bluelight, False)
            print("Soil too dry")


      def blue(self):
            print("Soil too wet")
            GPIO.output(self.bluelight, True)
            GPIO.output(self.redlight, False)
            
      def all_lights_off(self):
            GPIO.output(self.bluelight, False)
            GPIO.output(self.redlight, False)
