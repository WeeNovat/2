class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self): return f"Vector({self.x}, {self.y})"
    def __str__(self): return f"({self.x}; {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __abs__(self):
        return (self.x**2 + self.y**2)**0.5

v1 = Vector(3, 4)
v2 = Vector(1, 2)
print(f"Додавання v1 + v2: {v1 + v2}")
print(f"Множення v1 * 2: {v1 * 2}")
print(f"Довжина (abs): {abs(v1)}")
print(f"Порівняння: {v1 == v2}")
