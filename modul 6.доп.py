import math

class Figure:
    def __init__(self, color, *sides):
        self._sides = list(sides) if self.is_valid_sides(*sides) else [1] * self.sides_count
        self._color = color
        self.filled = False

    @property
    def sides_count(self):
        return 0

    @property
    def color(self):
        return self._color

    def __is_valid_color(self, r, g, b):
        """Проверяет корректность переданных цветовых значений."""
        return all(isinstance(x, int) and 0 <= x <= 255 for x in (r, g, b))

    def set_color(self, r, g, b):
        """Устанавливает цвет фигуры, проверяя корректность."""
        if self.__is_valid_color(r, g, b):
            self._color = (r, g, b)

    def is_valid_sides(self, *new_sides):
        """Проверяет корректность сторон."""
        return all(isinstance(side, int) and side > 0 for side in new_sides) and len(new_sides) == self.sides_count

    @property
    def sides(self):
        """Возвращает список сторон."""
        return self._sides

    def len__(self):
        """Возвращает периметр фигуры."""
        return sum(self._sides)

    def set_sides(self, *new_sides):
        """Устанавливает новые стороны при выполнении условий."""
        if self.is_valid_sides(*new_sides):
            self._sides = list(new_sides)

    def get_color(self):
        """Возвращает цвет фигуры в формате RGB."""
        return self._color


class Circle(Figure):
    @property
    def sides_count(self):
        return 1

    def __init__(self, color, circumference):
        self.__radius = circumference / (2 * math.pi)
        super().__init__(color, *[1])  # Один сторона у круга

    def get_square(self):
        """Возвращает площадь круга."""
        return math.pi * (self.__radius ** 2)


class Triangle(Figure):
    @property
    def sides_count(self):
        return 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_square(self):
        """Возвращает площадь треугольника по формуле Герона."""
        a, b, c = self._sides
        s = self.len__() / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))


class Cube(Figure):
    @property
    def sides_count(self):
        return 12

    def __init__(self, color, side):
        sides = [side] * 12
        super().__init__(color, *sides)

    def get_volume(self):
        """Возвращает объем куба."""
        side = self._sides[0]
        return side ** 3


# Пример использования:
circle1 = Circle((200, 200, 100), 10)  # (Цвет, длина окружности)
print(f"Circle Color: {circle1.get_color()}")
print(f"Circle Area: {circle1.get_square()}")

cube1 = Cube((222, 35, 130), 6)  # (Цвет, сторона)
print(f"Cube Color: {cube1.get_color()}")
print(f"Cube Volume: {cube1.get_volume()}")

triangle1 = Triangle((255, 0, 0), 3, 4, 5)  # (Цвет, стороны)
print(f"Triangle Color: {triangle1.get_color()}")
print(f"Triangle Area: {triangle1.get_square()}")















