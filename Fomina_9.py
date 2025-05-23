import math

class Rational:
    def __init__(self, *args):
        if len(args) == 1:
            self.numerator, self.denominator = map(int, args[0].split('/'))
        elif len(args) == 2:
            self.numerator, self.denominator = args
        else:
            raise ValueError("Неправильна кількість аргументів")

        if self.denominator == 0:
            raise ValueError("Знаменник не може дорівнювати нулю")

        self._simplify()

    def _simplify(self):
        gcd = math.gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd
        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator

    def __add__(self, other):
        if isinstance(other, Rational):
            num = self.numerator * other.denominator + self.denominator * other.numerator
            denom = self.denominator * other.denominator
        elif isinstance(other, int):
            num = self.numerator + other * self.denominator
            denom = self.denominator
        else:
            raise TypeError("Непідтримуваний тип операнду")
        return Rational(num, denom)

    def __sub__(self, other):
        if isinstance(other, Rational):
            num = self.numerator * other.denominator - self.denominator * other.numerator
            denom = self.denominator * other.denominator
        elif isinstance(other, int):
            num = self.numerator - other * self.denominator
            denom = self.denominator
        else:
            raise TypeError("Непідтримуваний тип операнду")
        return Rational(num, denom)

    def __mul__(self, other):
        if isinstance(other, Rational):
            num = self.numerator * other.numerator
            denom = self.denominator * other.denominator
        elif isinstance(other, int):
            num = self.numerator * other
            denom = self.denominator
        else:
            raise TypeError("Непідтримуваний тип операнду")
        return Rational(num, denom)

    def __truediv__(self, other):
        if isinstance(other, Rational):
            num = self.numerator * other.denominator
            denom = self.denominator * other.numerator
        elif isinstance(other, int):
            num = self.numerator
            denom = self.denominator * other
        else:
            raise TypeError("Непідтримуваний тип операнду")
        return Rational(num, denom)

    def __float__(self):
        return self.numerator / self.denominator

    def __getitem__(self, key):
        if key == 'n':
            return self.numerator
        elif key == 'd':
            return self.denominator
        else:
            raise KeyError("Невірний ключ")

    def __setitem__(self, key, value):
        if key == 'n':
            self.numerator = value
        elif key == 'd':
            self.denominator = value
        else:
            raise KeyError("Невірний ключ")
        self._simplify()

    def __repr__(self):
        return f"{self.numerator}/{self.denominator}"


class RationalList:
    def __init__(self):
        self.items = []

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        if isinstance(value, Rational):
            self.items[index] = value
        else:
            raise TypeError("Додавати можна лише екземпляри Rational")

    def __len__(self):
        return len(self.items)

    def __add__(self, other):
        result = RationalList()
        result.items = self.items[:]
        if isinstance(other, RationalList):
            result.items += other.items
        elif isinstance(other, Rational):
            result.items.append(other)
        elif isinstance(other, int):
            result.items.append(Rational(other, 1))
        else:
            raise TypeError("Непідтримуваний тип операнду")
        return result

    def __iadd__(self, other):
        if isinstance(other, list):
            for item in other:
                if isinstance(item, Rational):
                    self.items.append(item)
                else:
                    raise TypeError("У списку можуть бути лише Rational")
        elif isinstance(other, Rational):
            self.items.append(other)
        elif isinstance(other, int):
            self.items.append(Rational(other, 1))
        else:
            raise TypeError("Непідтримуваний тип операнду")
        return self

    def __repr__(self):
        return f"RationalList({self.items})"


# Тестування
r1 = Rational(3, 4)
r2 = Rational('5/6')

sum_r = r1 + r2
product_r = r1 * 2

decimal_r = float(r1)

r_list = RationalList()
r_list += r1
r_list += [r2, Rational(7, 8)]
r_list[1] = Rational(2, 3)

print("Сума:", sum_r)
print("Добуток:", product_r)
print("Десятковий вигляд:", decimal_r)
print("Довжина списку:", len(r_list))
print("Список:", r_list)