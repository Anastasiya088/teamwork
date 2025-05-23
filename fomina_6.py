import math

# Базовий клас
class Shape:
    def area(self):
        raise NotImplementedError

    def perimeter(self):
        raise NotImplementedError

# Клас Трикутник
class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def is_valid(self):
        return (self.a + self.b > self.c and
                self.a + self.c > self.b and
                self.b + self.c > self.a)

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        if not self.is_valid():
            raise ValueError(f"Некоректний трикутник зі сторонами: {self.a}, {self.b}, {self.c}")
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

# Прямокутник
class Rectangle(Shape):
    def __init__(self, a, b):
        self.a, self.b = a, b

    def perimeter(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.b

# Трапеція
class Trapeze(Shape):
    def __init__(self, a, b, c, d):
        self.a, self.b, self.c, self.d = a, b, c, d

    def perimeter(self):
        return self.a + self.b + self.c + self.d

    def area(self):
        # Припущення: c і d — бокові сторони, висота вираховується через наближення
        h = math.sqrt(self.c**2 - (((self.b - self.a)**2 + self.c**2 - self.d**2) / (2*(self.b - self.a)))**2)
        return 0.5 * (self.a + self.b) * h

# Паралелограм
class Parallelogram(Shape):
    def __init__(self, a, b, h):
        self.a, self.b, self.h = a, b, h

    def perimeter(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.h

# Коло
class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def perimeter(self):
        return 2 * math.pi * self.r

    def area(self):
        return math.pi * self.r ** 2

# Розбір рядка
def parse_line(line):
    tokens = line.strip().split()
    shape_type = tokens[0]
    params = list(map(float, tokens[1:]))

    if shape_type == "Triangle":
        return Triangle(*params)
    elif shape_type == "Rectangle":
        return Rectangle(*params)
    elif shape_type == "Trapeze":
        return Trapeze(*params)
    elif shape_type == "Parallelogram":
        return Parallelogram(*params)
    elif shape_type == "Circle":
        return Circle(*params)
    else:
        raise ValueError(f"Невідома фігура: {shape_type}")

# Обробка файлу
def process_file(filename):
    shapes = []
    with open(filename) as f:
        for line in f:
            if line.strip():
                try:
                    shape = parse_line(line)
                    shape.area()      # перевірка валідності
                    shape.perimeter() # перевірка валідності
                    shapes.append(shape)
                except Exception as e:
                    print(f"Пропущено фігуру: {line.strip()} — {e}")

    if not shapes:
        print("Немає валідних фігур.")
        return

    max_area_shape = max(shapes, key=lambda s: s.area())
    max_perimeter_shape = max(shapes, key=lambda s: s.perimeter())

    print(f"Фігура з найбільшою площею: {type(max_area_shape).__name__} — площа: {max_area_shape.area():.2f}")
    print(f"Фігура з найбільшим периметром: {type(max_perimeter_shape).__name__} — периметр: {max_perimeter_shape.perimeter():.2f}")

# Виклик функції
process_file("fomina_6.txt")