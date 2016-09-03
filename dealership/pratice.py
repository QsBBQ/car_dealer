
# Composition pratice
# http://python-textbok.readthedocs.io/en/latest/Object_Oriented_Programming.html
# http://stackoverflow.com/questions/26467564/how-to-copy-all-attributes-of-one-python-object-to-another

# question what is better passing objects into car or passing car into objects?
# question it seems this is useful to work with data in general but if using a
# db do you do something like this to load up and use data?

# service, wash, brakes, transmission
# financing,
# load from file and load from db

class Car:
    def __init__(self, year, color, car_make, car_model, car_trim):
        self.car = "Car"
        self.year = year
        self.color = color
        self.car_make = car_make
        self.car_model = car_model
        self.car_trim = car_trim

    def wheels(self):
        return 4
    def __getattr__(self, attr):
        return getattr(self.car_make, attr)
    # def __getattr__(self, attr):
    #     return getattr(self.car_model, attr)
    # def __getattr__(self, attr):
    #     return getattr(self.car_trim, attr)

class Mazda:
    def __init__(self):
        self.manufacturer = "Mazda"
        self.slogan = "zoom zoom"
    def warranty(self):
        return 32

class GrandTouring:
    def seat_material(self):
        return "leather"
    def navigation(self):
        return True

class Touring:
    def seat_material(self):
        return "leathette"

class Sport:
    def seat_material(self):
        return "cloth"

class Mazda3:
    def __init__(self): # trim
        # self.mazda = Mazda()
        self.model = "Mazda3"
    # def __getattr__(self, attr):
    #     return getattr(self.mazda, attr)
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

class CarList:
    def __init__(self):
        self.my_cars = []
    def add_car(self, car):
        self.my_cars.append(car)
    def show_cars(self):
        return self.my_cars

car_list = [{"make": "Mazda",
                "model": "Mazda6",
                "year": 2016,
                "color": "red",
                "vin": 123},
                {"make": "Mazda",
                 "model": "Mazda6",
                 "year": 2007,
                 "color": "red",
                 "vin": 456}]
def main():
    car_list = CarList()

    car_make = Mazda()
    car_model = Mazda3()
    car_trim = Touring()
    car_list.add_car(Car(2016, "red",
                         car_make, car_model, car_trim))
    print(car_list.show_cars()[0].slogan)

if __name__ == "__main__":
    main()
