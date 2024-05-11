class Car:
    def __init__(self):
        self.speed = 0
        self.model = ""
        self.supercar = None

    def set_speed(self):
        self.speed = float(input("Enter the speed of the car: "))

    def set_model(self):
        self.model = input("Enter the model of the car: ")

    def set_supercar(self):
        self.supercar = input("Enter Yes/y if the car is a supercar or No/n if it isn't: ").lower()
        if self.supercar == "yes" or self.supercar == "y":
            self.supercar = True
        elif self.supercar == "no" or self.supercar == "n":
            self.supercar = False
        else:
            self.supercar = None

    def get_speed(self):
        return self.speed

    def get_model(self):
        return self.model

    def get_supercar(self):
        return self.supercar

class FrenchCar(Car):
    def __init__(self):
        super().__init__()
        self.price = int(input("Enter the price of your French car: "))
        self.french = True
        self.set_speed()
        self.set_model()
        self.set_supercar()


car = Car()
car.set_speed()
car.set_model()
car.set_supercar()

print("The current speed is", car.get_speed())
print("The current model of the car is", car.get_model())
print("The current car is a supercar:", car.get_supercar())

car2 = FrenchCar()

print("The current speed is", car2.speed)
print("The current model of the car is", car2.model)
print("The current car is a supercar:", car2.supercar)
print("The car created is French : ", car2.french)
print("The price of the French car is "+str(car2.price)+"$")


