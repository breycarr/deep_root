from lib.plant import Plant

# As a user
# I want to know how moist the soil is

def test_soil_moisture():
    plant = Plant()
    assert plant.soil_moisture() == 350
