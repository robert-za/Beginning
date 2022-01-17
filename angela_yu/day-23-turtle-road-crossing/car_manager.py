import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 0.5


class CarManager:
    
    def __init__(self):
        self.all_cars = []
        self.swiftness = STARTING_MOVE_DISTANCE
        # self.loop_counter = 0
        # self.car_generator_frequency = 40

    def create_car(self):
        # if self.loop_counter % 6 == 0:
        # if self.loop_counter % self.car_generator_frequency == 0:
        random_chance = random.randint(1, 6)
        if random_chance == 6:
            new_car = Turtle("square")
            new_car.penup()
            new_car.setheading(180)
            new_car.color(random.choice(COLORS))
            new_car.shapesize(1,2)
            new_car.goto(320, random.randint(-250, 250))
            self.all_cars.append(new_car)
        # self.loop_counter += 1
        # self.car_generator_frequency -= 1

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.swiftness)

    def increase_speed(self):
        for car in self.all_cars:
           self.swiftness += MOVE_INCREMENT
        
