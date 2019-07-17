from controller import Controller


class MockLight():
    def blue(self):
        print("Soil too wet")

    def green(self):
        print("Soil just right")

    def red(self):
        print("Soil too dry")


class TestController(object):

    def test_welcome_message(self):
        controller = Controller()
        assert controller.welcome() == "Welcome to Deep Root"

    def test_soil_moisture_reading(self):
        class MockPlant():
            def soil_moisture(self):
                return 900
        controller = Controller()
        assert controller.soil_moisture(MockPlant) == 900
