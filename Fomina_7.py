import math

# Базовий клас
class Figure:
    def dimension(self):
        raise NotImplementedError

    def perimeter(self):
        return None

    def area(self):
        return None

    def surface_area(self):
        return None

    def base_area(self):
        return None

    def height(self):
        return None

    def volume(self):
        raise NotImplementedError

# Двовимірні фігури
class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def dimension(self):
        return 2

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def volume(self):
        return self.area()

class Rectangle(Figure):
    def __init__(self, a, b):
        self.a, self.b = a, b

    def dimension(self):
        return 2

    def perimeter(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.b

    def volume(self):
        return self.area()

class Parallelogram(Figure):
    def __init__(self, a, b, h):
        self.a, self.b, self.h = a, b, h

    def dimension(self):
        return 2

    def perimeter(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.h

    def volume(self):
        return self.area()

class Circle(Figure):
    def __init__(self, r):
        self.r = r

    def dimension(self):
        return 2

    def perimeter(self):
        return 2 * math.pi * self.r

    def area(self):
        return math.pi * self.r ** 2

    def volume(self):
        return self.area()

class Trapeze(Figure):
    def __init__(self, a, b, c, d):
        self.a, self.b, self.c, self.d = a, b, c, d

    def dimension(self):
        return 2

    def perimeter(self):
        return self.a + self.b + self.c + self.d

    def area(self):
        # Припущення: прямокутна трапеція
        h = abs(self.c - self.d)
        return 0.5 * (self.a + self.b) * h

    def volume(self):
        return self.area()

# Тривимірні фігури
class Ball(Figure):
    def __init__(self, r):
        self.r = r

    def dimension(self):
        return 3

    def surface_area(self):
        return 4 * math.pi * self.r ** 2

    def volume(self):
        return (4 / 3) * math.pi * self.r ** 3

class Cone(Figure):
    def __init__(self, r, h):
        self.r, self.h = r, h

    def dimension(self):
        return 3

    def base_area(self):
        return math.pi * self.r ** 2

    def surface_area(self):
        l = math.sqrt(self.r ** 2 + self.h ** 2)
        return math.pi * self.r * (self.r + l)

    def height(self):
        return self.h

    def volume(self):
        return (1 / 3) * math.pi * self.r ** 2 * self.h

class TriangularPyramid(Triangle):
    def __init__(self, a, h):
        super().__init__(a, a, a)
        self.h = h

    def dimension(self):
        return 3

    def base_area(self):
        return super().area()

    def height(self):
        return self.h

    def volume(self):
        return (1 / 3) * self.base_area() * self.h

class QuadrangularPyramid(Rectangle):
    def __init__(self, a, b, h):
        super().__init__(a, b)
        self.h = h

    def dimension(self):
        return 3

    def base_area(self):
        return super().area()

    def height(self):
        return self.h

    def volume(self):
        return (1 / 3) * self.base_area() * self.h

class RectangularParallelepiped(Rectangle):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c

    def dimension(self):
        return 3

    def surface_area(self):
        return 2 * (self.a * self.b + self.a * self.c + self.b * self.c)

    def volume(self):
        return self.a * self.b * self.c

class TriangularPrism(Triangle):
    def __init__(self, a, b, c, h):
        super().__init__(a, b, c)
        self.h = h

    def dimension(self):
        return 3

    def surface_area(self):
        return 2 * super().area() + self.perimeter() * self.h

    def height(self):
        return self.h

    def volume(self):
        return super().area() * self.h