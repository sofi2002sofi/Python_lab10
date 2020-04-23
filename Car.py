class Car:
    count_of_cars = 0

    def __init__(self, engine_power_in_horsepower=100, brand="Chevrolet", maximum_speed_in_km_per_hour=180,
                 count_of_passengers=5, assignment="passenger_car", fuel_type="gas"):
        self.engine_power_in_horsepower = engine_power_in_horsepower
        self.brand = brand
        self.maximum_speed_in_km_per_hour = maximum_speed_in_km_per_hour
        self.count_of_passengers = count_of_passengers
        self.assignment = assignment
        self.fuel_type = fuel_type
        Car.count_of_cars += 1

    def __del__(self):
        print("Видалення екземпляра класу")

    def __str__(self):
        return "Information about this car: engine_power_in_horsepower = " + str(self.engine_power_in_horsepower) + \
               "; brand = " + str(self.brand) + "; maximum_speed_in_km_per_hour = " + \
               str(self.maximum_speed_in_km_per_hour) + "; count_of_passengers = " + str(self.count_of_passengers) + \
               "; assignment = " + str(self.assignment) + "; fuel_type = " + str(self.fuel_type)

    @staticmethod
    def get_count_of_cars():
        return Car.count_of_cars

def main():
    rental_car = Car(120, "Volkswagen", 220, 5, "passenger_car", "petrol")
    trunk = Car(352, "Mercedes", 200, 3, "trunk", "diesel_fuel")
    neighbors_car = Car()
    print(rental_car)
    print(trunk)
    print(neighbors_car)
    print(Car.get_count_of_cars())

if __name__ == "__main__":
    main()