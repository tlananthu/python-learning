#bike class

class Bike:
    def __init__(self, colour, frame_material):
        self.colour=colour
        self.frame_material=frame_material

    def brake(self):
        print('{0} Colour bike is braking.'.format(self.colour))

redBike=Bike('Red','Carbon Fiber')
blueBike=Bike('Blue','Steel')

redBike.brake()
