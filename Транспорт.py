class Transport:
    def __init__(self, speed):
        self.speed = speed 

    def move(self):
        return f"Транспортний засіб рухається зі швидкістю {self.speed} км/год."

class Car(Transport):
    def __init__(self, speed, model):
        super().__init__(speed)
        self.model = model  

    def move(self):
        return f"Автомобіль {self.model} рухається зі швидкістю {self.speed} км/год."


class Moto(Transport):
    def __init__(self, speed, type_of_moto):
        super().__init__(speed)
        self.type_of_moto = type_of_moto  

    def move(self):
        return f"Мотоцикл {self.type_of_moto} рухається зі швидкістю {self.speed} км/год."

car = Car(120, "Toyota")
moto = Moto(25, "Geon")

print(car.move())
print(moto.move())

