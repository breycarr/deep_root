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

    def test_blue(self, capsys):
        class MockPlant():
            def soil_moisture(self):
                return 900
        controller = Controller()
        soil_moisture = controller.soil_moisture(MockPlant)
        controller.light(soil_moisture, MockLight)
        captured = capsys.readouterr()
        assert captured.out == "Soil too wet\n"

    def test_red(self, capsys):
        class MockPlant():
            def soil_moisture(self):
                return 300
        controller = Controller()
        soil_moisture = controller.soil_moisture(MockPlant)
        controller.light(soil_moisture, MockLight)
        captured = capsys.readouterr()
        assert captured.out == "Soil too dry\n"

    def test_green(self, capsys):
        class MockPlant():
            def soil_moisture(self):
                return 650
        controller = Controller()
        soil_moisture = controller.soil_moisture(MockPlant)
        controller.light(soil_moisture, MockLight)
        captured = capsys.readouterr()
        assert captured.out == "Soil just right\n"
