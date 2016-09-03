import dealership.pratice as dl

car_list = dl.CarList()

car_make = dl.Mazda()
car_model = dl.Mazda3()
car_trim = dl.Touring()
car_list.add_car(dl.Car(2016, "red",
                     car_make, car_model, car_trim))
print(car_list.show_cars()[0].slogan)
