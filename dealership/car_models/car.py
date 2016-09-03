class Car:
    def __init__(self, year, color, model, trim=None):
        self.car = "Car"
        self.year = year
        self.color = color
        # self.car_make = car_make
        self.model = model
        self.trim = trim

    def wheels(self):
        return 4

    # def __getattr__(self, attr):
    #     return getattr(self.car_make, attr)
    # def __getattr__(self, attr):
    #     return getattr(self.car_model, attr)
    # def __getattr__(self, attr):
    #     return getattr(self.car_trim, attr)
