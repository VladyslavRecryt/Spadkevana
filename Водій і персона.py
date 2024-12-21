class Person:
    def __init__(self, name):
        self.name = name

    def age(self, birth_year, current_year):
        return current_year - birth_year

class Driver(Person):
    def __init__(self, name, license_number):
        super().__init__(name)
        self.license_number = license_number

person = Person(name="Petro")
driver = Driver(name="Vasa", license_number="WNDR4627642TYH452")

print(f"{person.name} is {person.age(1990, 2024)} years old.")
print(f"Driver {driver.name} has license number {driver.license_number}.")
