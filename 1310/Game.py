class Game:
    def __init__(self, length):
        self.length = length

    def play(self, maps, cars):
        winners = []
        n = 0
        k = len(cars)
        while len(winners) != k:
            for car in cars:
                if car.speed * n >= self.length * maps:
                    winners.append(car.name)
                    cars.remove(car)
            n += 1
        return winners


class Car:
    def __init__(self, speed, name):
        self.speed = speed
        self.name = name


car1 = Car(25, "Car1")
car2 = Car(20, "Car2")
car3 = Car(30, "Car3")
game1 = Game(100)
print(game1.play(7, [car1, car2, car3]))
