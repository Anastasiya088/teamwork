import os
from math import gcd

class Rational:
    def __init__(self, *args):
        if len(args) == 1:
            if isinstance(args[0], str):
                try:
                    n, d = map(int, args[0].split('/'))
                except ValueError:
                    raise ValueError(f"Invalid rational string: {args[0]}")
            elif isinstance(args[0], int):
                n, d = args[0], 1
            else:
                raise ValueError("Invalid argument type")
        elif len(args) == 2 and all(isinstance(arg, int) for arg in args):
            n, d = args
        else:
            raise ValueError("Invalid number of arguments or argument types")

        if d == 0:
            raise ZeroDivisionError("Denominator cannot be zero")
        if d < 0:
            n, d = -n, -d

        g = gcd(n, d)
        self.numerator = n // g
        self.denominator = d // g

    def __repr__(self):
        return f"{self.numerator}/{self.denominator}"

    def __float__(self):
        return self.numerator / self.denominator

    def __getitem__(self, key):
        if key == 'n':
            return self.numerator
        elif key == 'd':
            return self.denominator
        else:
            raise KeyError("Key must be 'n' or 'd'")

    def __setitem__(self, key, value):
        if key == 'n':
            if not isinstance(value, int):
                raise TypeError("Numerator must be an integer")
            self.numerator = value
        elif key == 'd':
            if not isinstance(value, int):
                raise TypeError("Denominator must be an integer")
            if value == 0:
                raise ZeroDivisionError("Denominator cannot be zero")
            self.denominator = value
        else:
            raise KeyError("Key must be 'n' or 'd'")
        g = gcd(self.numerator, self.denominator)
        self.numerator //= g
        self.denominator //= g


class RationalList:
    def __init__(self, *args):
        self.rationals = []
        for arg in args:
            if isinstance(arg, (str, int)):
                try:
                    self.rationals.append(Rational(arg))
                except ValueError as e:
                    print(f"Error creating Rational from '{arg}': {e}")
            elif isinstance(arg, Rational):
                self.rationals.append(arg)
            else:
                raise TypeError(f"Unsupported type for RationalList element: {type(arg)}")

    def __iter__(self):
        return iter(sorted(self.rationals, key=lambda r: (-r.denominator, -r.numerator)))

    def __getitem__(self, index):
        return self.rationals[index]

    def __setitem__(self, index, value):
        if isinstance(value, (str, int)):
            try:
                self.rationals[index] = Rational(value)
            except ValueError as e:
                print(f"Error setting Rational at index {index} from '{value}': {e}")
        elif isinstance(value, Rational):
            self.rationals[index] = value
        else:
            raise TypeError(f"Unsupported type for RationalList element: {type(value)}")

    def append(self, value):
        if isinstance(value, (str, int)):
            try:
                self.rationals.append(Rational(value))
            except ValueError as e:
                print(f"Error appending Rational from '{value}': {e}")
        elif isinstance(value, Rational):
            self.rationals.append(value)
        else:
            raise TypeError(f"Unsupported type for RationalList element: {type(value)}")

    def __len__(self):
        return len(self.rationals)

    def __add__(self, other):
        new_list = RationalList(*self.rationals)
        if isinstance(other, RationalList):
            new_list.rationals.extend(other.rationals)
        elif isinstance(other, (Rational, int)):
            try:
                new_list.append(Rational(other))
            except ValueError as e:
                print(f"Error adding to RationalList: {e}")
        else:
            raise TypeError("Unsupported operand type(s) for +")
        return new_list

    def __iadd__(self, other):
        if isinstance(other, RationalList):
            self.rationals.extend(other.rationals)
        elif isinstance(other, (Rational, int)):
            try:
                self.append(Rational(other))
            except ValueError as e:
                print(f"Error adding to RationalList: {e}")
        else:
            raise TypeError("Unsupported operand type(s) for +=")
        return self


def read_rationals_from_file(Zinchuk_10):
    rationals = RationalList()
    if os.path.exists(Zinchuk_10):
        with open(Zinchuk_10, 'r') as file:
            for line in file:
                for item in line.split():
                    try:
                        rationals.append(Rational(item))
                    except ValueError as e:
                        print(f"Invalid rational number in {Zinchuk_10}: {item} - {e}")
    else:
        print(f"File {Zinchuk_10} not found.")
    return rationals

if __name__ == "__main__":
    # Приклад використання класу Rational
    r1 = Rational(1, 2)
    r2 = Rational("3/4")
    r3 = Rational(5)

    print(f"r1: {r1}")
    print(f"r2: {r2}")
    print(f"r3: {r3}")
    print(f"float(r1): {float(r1)}")
    print(f"r2['n']: {r2['n']}")
    print(f"r2['d']: {r2['d']}")

    r1['n'] = 7
    print(f"r1 після зміни чисельника: {r1}")

    # Приклад використання класу RationalList
    rl1 = RationalList(r1, r2, "1/3", 2)
    rl2 = RationalList(Rational(5, 6), "7/8")

    print(f"\nrl1: {[str(r) for r in rl1]}")
    print(f"len(rl1): {len(rl1)}")
    print(f"rl1[1]: {rl1[1]}")

    rl1[3] = Rational(9, 10)
    print(f"rl1 після зміни елемента: {[str(r) for r in rl1]}")

    rl3 = rl1 + rl2
    print(f"rl1 + rl2: {[str(r) for r in rl3]}")

    rl1 += Rational("11/12")
    print(f"rl1 += Rational('11/12'): {[str(r) for r in rl1]}")

    print("\nВідсортований rl1:")
    for r in rl1:
        print(r)

    # Приклад використання функції read_rationals_from_file
    filename = "rationals.txt"
    # Створимо тестовий файл
    with open(filename, 'w') as f:
        f.write("1/2 3/4 5 -1/3 invalid 7/8\n")
        f.write("9/10 11 0/1 12/-5\n")

    rationals_from_file = read_rationals_from_file(filename)
    print(f"\nРаціональні числа з файлу '{filename}': {[str(r) for r in rationals_from_file]}")

    # Очистимо тестовий файл
    os.remove(filename)