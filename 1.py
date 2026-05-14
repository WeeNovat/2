class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        return "Транспортний засіб рухається"

    def __str__(self):
        return f"{self.brand} {self.model}"

class Car(Vehicle):
    def __init__(self, brand, model, fuel_type):
        super().__init__(brand, model)
        self.fuel_type = fuel_type

    def move(self):
        return f"Їде по дорозі на {self.fuel_type}"

class Plane(Vehicle):
    def __init__(self, brand, model, altitude):
        super().__init__(brand, model)
        self.altitude = altitude

    def move(self):
        return f"Летить у небі на висоті {self.altitude}м"

class Boat(Vehicle):
    def move(self):
        return "Пливе по воді"

fleet = [Car("Tesla", "S", "електриці"), Plane("Boeing", "747", 10000), Boat("Yamaha", "242X")]

for v in fleet:
    print(f"{v}: {v.move()}")

print(f"\nПеревірка типів: Plane є підкласом Vehicle? {issubclass(Plane, Vehicle)}")