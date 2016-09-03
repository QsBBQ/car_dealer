
# Composition pratice
# http://python-textbok.readthedocs.io/en/latest/Object_Oriented_Programming.html
# http://stackoverflow.com/questions/26467564/how-to-copy-all-attributes-of-one-python-object-to-another

# question what is better passing objects into car or passing car into objects?
# question it seems this is useful to work with data in general but if using a
# db do you do something like this to load up and use data?

# service, wash, brakes, transmission
# financing,
# load from file and load from db


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





# car_list = [{"make": "Mazda",
#                 "model": "Mazda6",
#                 "year": 2016,
#                 "color": "red",
#                 "vin": 123},
#                 {"make": "Mazda",
#                  "model": "Mazda6",
#                  "year": 2007,
#                  "color": "red",
#                  "vin": 456}]
# def main():
#     car_list = CarList()
#
#     car_mazda = Mazda3(2016, "red")
#     # car_model = Mazda3()
#     # car_trim = Touring()
#     car_list.add_car(car_mazda)
#     print(car_list.show_cars()[0].slogan)

# if __name__ == "__main__":
#     main()
