from mazda import Mazda3

class CarFactory:
    def __init__(self):
        pass

    def create(self, year, color, make, model):
        if make == "Mazda" and model == "Mazda3":
            return Mazda3(year, color)
