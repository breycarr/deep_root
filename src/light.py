try:
    import RPi.GPIO as GPIO
except ImportError:
    from rpidevmocks import MockGPIO
    GPIO = MockGPIO()

REDLIGHT = 18
BLUELIGHT = 11
GREENLIGHT = 16

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(REDLIGHT, GPIO.OUT)
GPIO.setup(BLUELIGHT, GPIO.OUT)
GPIO.setup(GREENLIGHT, GPIO.OUT)


class Light():

    def red(self):
        print("Soil too dry")
        self.all_lights_off()
        GPIO.output(REDLIGHT, True)

    def blue(self):
        print("Soil too wet")
        self.all_lights_off()
        GPIO.output(BLUELIGHT, True)

    def green(self):
        print("Soil just right")
        self.all_lights_off()
        GPIO.output(GREENLIGHT, True)

    def all_lights_off(self):
        GPIO.output(BLUELIGHT, False)
        GPIO.output(REDLIGHT, False)
        GPIO.output(GREENLIGHT, False)
