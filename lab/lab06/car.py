class Car(object):
    num_wheels = 4
    gas = 30
    headlights = 2
    size = 'Tiny'

    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.color = 'No color yet. You need to paint me.'
        self.wheels = Car.num_wheels
        self.gas = Car.gas

    def paint(self, color):
        self.color = color
        return self.make + ' ' + self.model + ' is now ' + color

    def drive(self):
        if self.wheels < Car.num_wheels or self.gas <= 0:
            return 'Cannot drive!'
        self.gas -= 10
        return self.make + ' ' + self.model + ' goes vroom!'

    def pop_tire(self):
        if self.wheels > 0:
            self.wheels -= 1

    def fill_gas(self):
        self.gas += 20
        return 'Gas level: ' + str(self.gas)

deneros_car = Car('Tesla', 'Model S')
deneros_car.model

deneros_car.gas = 10
deneros_car.drive()

deneros_car.drive()
deneros_car.fill_gas()
deneros_car.gas

Car.gas

deneros_car = Car('Tesla', 'Model S')
deneros_car.wheels = 2
deneros_car.wheels

Car.num_wheels

deneros_car.drive()
Car.drive()
Car.drive(deneros_car)

#%%
class MonsterTruck(Car):
    size = 'Monster'

    def rev(self):
        print('Vroom! This Monster Truck is huge!')

    def drive(self):
        self.rev()
        return Car.drive(self)
    
deneros_car = MonsterTruck('Monster', 'Batmobile')
deneros_car.drive() #子类的方法覆盖了父类的方法
Car.drive(deneros_car) #如果再父类中调用，只会返回父类的方法
MonsterTruck.drive(deneros_car)
Car.rev(deneros_car)
