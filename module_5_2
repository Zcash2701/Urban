class House:
    def __init__(self, name, number_floor):
        self.name = name
        self.number_floor = number_floor

    def go_to(self, new_floor):
        if new_floor > self.number_floor or new_floor < 1:
            print('Такого этажа не существует')
        elif new_floor == 1:
            print('Вы и так на первом этаже')
        else:
            for i in range(1, new_floor + 1):
                print(i)

    def __len__(self):
        return self.number_floor

    def __str__(self):
        result = f'Название {self.name}, количество этажей {self.number_floor}'
        return result

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))
