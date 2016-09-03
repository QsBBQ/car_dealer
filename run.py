from dealership.car_models.car_list import CarList
from dealership.car_models.mazda import Mazda3
from dealership.car_models.factory import CarFactory

car_list = CarList()
car_mazda = Mazda3(2016, "red")
car_list.add_car(car_mazda)
print(car_list.show_cars()[0].slogan)



factory = CarFactory()
car_data = [{"make": "Mazda",
                 "model": "Mazda3",
                 "year": 2016,
                 "color": "red"},
                 {"make": "Mazda",
                  "model": "Mazda6",
                  "year": 2007,
                  "color": "red"}]

for item in car_data:
    car_list.add_car( factory.create(item['year'], item['color'],
                                   item['make'], item['model']) )

for car in car_list.show_cars():
    if car:
        print(car.model)
