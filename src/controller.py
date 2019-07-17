class Controller():

    def welcome(self):
        return "Welcome to Deep Root"

    def soil_moisture(self, plant_class):
        plant = plant_class()
        return plant.soil_moisture()
