class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def show(self):
        return f"{self.name} is a {self.species}."

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "Dog")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "Cat")

dog = Dog(name="Buddy")
cat = Cat(name="Mittens")

print(dog.show())
print(cat.show())
