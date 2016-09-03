from car import Car

class Mazda:
    def __init__(self, year, color, model):
        self.manufacturer = "Mazda"
        self.slogan = "zoom zoom"
        self.car = Car(year, color, model)

    def __getattr__(self, attr):
        return getattr(self.car, attr)

    @property
    def warranty(self):
        return 32

class Mazda3:
    def __init__(self, year, color): # trim
        # self.model = "Mazda3"
        self.car = Mazda(year, color, "Mazda3")

    def __getattr__(self, attr):
        return getattr(self.car, attr)
    # @property
    # def slogan(self):
    #     return self.car.slogan


    def car_size(self):
        return "compact-size"

class Mazda6:
    def __init__(self):
        # self.mazda = Mazda()
        self.model = "Mazda6"
    # def __getattr__(self, attr):
    #     return getattr(self.mazda, attr)
    def car_size(self):
        return "mid-size"
