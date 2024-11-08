class Vehicle:
    __color_variants = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, model, color, horsepower):
        self.owner = owner
        self.__model = model
        self.__engine_power = horsepower
        self.__color = color


    def get_model(self):
        print(f'Модель: {self.__model}')

    def get_horsepower(self):
        print(f'Мощность двигателя: {self.__engine_power}')

    def get_color(self):
        print(f'Цвет: {self.__color}')

    def print_info(self):
        print(f'Модель: {self.__model}\n'
              f'Мощность двигателя: {self.__engine_power}\n'
              f'Цвет: {self.__color}\n'
              f'Владелец: {self.owner}')

    def set_color(self, str_color):
        if str_color.lower() in self.__color_variants:
            self.__color = str_color
        else:
            print(f'Нельзя изменить цвет на {str_color}')

class Sedan(Vehicle):
    __passengers_limit = 5


if __name__ == '__main__':
    # Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

    # Изначальные свойства
    vehicle1.print_info()

    # Меняем свойства (в т.ч. вызывая методы)
    vehicle1.set_color('Pink')
    vehicle1.set_color('BLACK')
    vehicle1.owner = 'Vasyok'

    # Проверяем что поменялось
    vehicle1.print_info()