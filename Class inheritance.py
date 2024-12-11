import math

class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self._color = self._check_color(*color)
        self.filled = True
        self._sides = self._check_sides(*sides)

    def _check_color(self, r, g, b):
        if all(isinstance(i, int) and 0 <= i <= 255 for i in [r, g, b]):
            return [r, g, b]
        else:
            return [222, 35, 130]

    def get_color(self):
        return self._color

    def set_color(self, r, g, b):
        self._color = self._check_color(r, g, b)

    def _check_sides(self, *sides):
        if len(sides) == self.sides_count and all(isinstance(s, (int, float)) and s > 0 for s in sides):
            return list(sides)
        elif self.sides_count > 0:
            return [1] * self.sides_count
        else:
            return []

    def get_sides(self):
        return self._sides

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count and all(isinstance(s, (int, float)) and s > 0 for s in new_sides):
            self._sides = list(new_sides)

    def __len__(self): # Исправлено: __len__ вместо len
        return sum(self._sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self._radius = self._calculate_radius(self._sides[0])

    def _calculate_radius(self, circumference):
        return circumference / (2 * math.pi)

    def get_radius(self):
        return self._radius

    def get_square(self):
        return math.pi * self._radius*2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_square(self):
        a, b, c = self._sides
        s = (a + b + c) / 2
        if s > 0 and s > a and s > b and s > c:
            return math.sqrt(s * (s - a) * (s - b) * (s - c))
        else:
            return 0


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        if len(sides) == 1:
            side = sides[0]
            super().__init__(color, *([side] * 12))
        else:
            super().__init__(color, *([1] * 12))

    def get_volume(self):
        return (self._sides[0])*3


# Код для проверки:
circle1 = Circle((200, 200, 100), 10, 15, 6) # лишние параметры игнорируются
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())

cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())

circle1.set_sides(15)
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())