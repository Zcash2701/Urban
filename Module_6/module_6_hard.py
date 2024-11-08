import math


class Figure:
    side_count = 0

    def __init__(self, *params):
        temp_list = list(params[0])
        color = temp_list.pop(0)
        self.set_color(color)
        self.set_sides(temp_list)
        self.filled = bool

    def set_sides(self, *new_sides):

        if type(new_sides[0]) == int:
            new_sides = list(new_sides)

        elif type(new_sides) == tuple and len(new_sides) == 1 and type(new_sides[0]) == list:
            new_sides = new_sides[0]

        if len(new_sides) == self.side_count:
            self.__side = new_sides
        else:
            side_list = [1 for i in range(self.side_count)]
            self.__side = side_list

    def get_sides(self):
        return self.__side

    def get_color(self):
        return self.__color

    def set_color(self, *color):

        if len(color) == 3 and type(color[0]) == int:
            pass
        else:
            color = list(color[0])

        r = color[0]
        g = color[1]
        b = color[2]

        if self.__is_valid_color(r, g, b):
            self.__color = list(color)

    def __is_valid_color(self, r, g, b):
        flag = True
        if r < 0 or r > 255:
            return False
        if g < 0 or g > 255:
            return False
        if b < 0 or b > 255:
            return False
        return flag


class Circle(Figure):
    side_count = 1

    def __init__(self, *params):
        super().__init__(params)
        self.__radius = (self._Figure__side[0] / (math.pi * 2))

    def get_square(self):
        square = math.pi * math.pow(self.__radius, 2)
        return square

    def __len__(self):
        return self._Figure__side[0]


class Triangle(Figure):
    side_count = 3

    def __init__(self, *params):
        super().__init__(params)

    def get_square(self):
        params = self._Figure__side
        a = params[0]
        b = params[1]
        c = params[2]
        p = (a + b + c) / 2
        result = math.sqrt(p * (p - a) * (p - b) * (p - c))
        return result


class Cube(Figure):
    side_count = 12

    def __init__(self, *params):
        super().__init__(params)

    def set_sides(self, *new_sides):
        if type(new_sides[0]) == list:  # Инициализация
            new_sides = new_sides[0]
            if len(new_sides) == 1:
                temp_list = [new_sides[0] for i in range(self.side_count)]
                self._Figure__side = temp_list
                return
            else:
                temp_list = [1 for i in range(self.side_count)]
                self._Figure__side = temp_list
                return
        else:  # Вызов в коде
            if type(new_sides[0]) == int and len(new_sides) == 1:
                temp_list = [new_sides[0] for i in range(self.side_count)]
                self._Figure__side = temp_list
                return
            elif type(new_sides[0]) == int and len(new_sides) > 1:
                return

    def get_volume(self):
        result = math.pow(self._Figure__side[0], 3)
        return result


if __name__ == '__main__':
    circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)

    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77)  # Изменится
    print(circle1.get_color())
    cube1.set_color(300, 70, 15)  # Не изменится
    print(cube1.get_color())

    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    print(cube1.get_sides())
    circle1.set_sides(15)  # Изменится
    print(circle1.get_sides())

    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))

    # Проверка объёма (куба):
    print(cube1.get_volume())
