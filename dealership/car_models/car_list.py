class CarList:
    def __init__(self):
        self.my_cars = []
    def add_car(self, car):
        self.my_cars.append(car)
    def show_cars(self):
        return self.my_cars
