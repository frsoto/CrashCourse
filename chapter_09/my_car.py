from car import Car

my_new_car = Car('audi', 'a4', 2015)
print(my_new_car.get_descriptive_name())

my_new_car.read_odometer()
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_new_car.update_odometer(21)
my_new_car.read_odometer()

my_new_car.update_odometer(25)
my_new_car.read_odometer()