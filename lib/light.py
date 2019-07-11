import RPi.GPIO as GPIO 

class Light():
            
      def __init__(self, redlight = 18, bluelight = 11, greenlight = 16):
            self.redlight = redlight
            self.bluelight = bluelight
            self.greenlight = greenlight
            GPIO.setmode(GPIO.BCM)
            GPIO.setwarnings(False)
            GPIO.setup(redlight, GPIO.OUT)
            GPIO.setup(bluelight, GPIO.OUT)
            GPIO.setup(greenlight, GPIO.OUT)


      def red(self):
            GPIO.output(self.redlight, True)
            GPIO.output(self.bluelight, False)
            GPIO.output(self.greenlight, False)
            print("Soil too dry")


      def blue(self):
            print("Soil too wet")
            GPIO.output(self.bluelight, True)
            GPIO.output(self.redlight, False)
            GPIO.output(self.greenlight, False)

      def green(self):
            print("Soil just right")
            GPIO.output(self.greenlight, True)
            GPIO.output(self.redlight, False)
            GPIO.output(self.bluelight, False)
            
      def all_lights_off(self):
            GPIO.output(self.bluelight, False)
            GPIO.output(self.redlight, False)
            GPIO.output(self.greenlight, False)

