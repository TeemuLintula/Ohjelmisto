import random


class Car:
    current_speed = 0
    travelled_distance = 0

    def __init__(self, license_plate, maximum_speed):
        self.license_plate = license_plate
        self.maximum_speed = maximum_speed

    def accelerate(self, amount):
        self.current_speed += amount
        if self.current_speed < 0:
            self.current_speed = 0
        elif self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed

    def drive(self, hours):
        self.travelled_distance += hours * self.current_speed

def race(cars):
    raceEnded = False
    while raceEnded == False:
        for car in cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)
            if(car.travelled_distance > 10000):
                print(f"Car: {car.license_plate} won the race")
                raceEnded = True
                break

cars = [Car("ABC-123", 145),
        Car("DEF-456", 230),
        Car("GHI-678", 200)]

race(cars)