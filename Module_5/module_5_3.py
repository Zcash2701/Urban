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

    def __add__(self, value):
        self.number_floor = self.number_floor + value
        return self.number_floor

    def __radd__(self, other):
        self.number_floor = other + self.number_floor
        return self.number_floor

    def __eq__(self, other):
        return self.number_floor == other
    
    def __lt__(self, other):
        return self.number_floor < other

    def __le__(self, other):
        return self.number_floor <= other

    def __gt__(self, other):
        return self.number_floor > other 

    def __ge__(self, other):
        return self.number_floor >= other

    def __ne__(self, other):
        return self.number_floor != other


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__
