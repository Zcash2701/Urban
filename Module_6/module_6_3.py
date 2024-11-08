class Horse:
    def __init__(self):
        self.x_distance = 0
        self.sound = 'Frrr'
        super().__init__()

    def run(self, dx, dy):
        self.x_distance += dx
        super().fly(dy)

class Eagle():
    def __init__(self):
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance += dy

class Pegasus(Horse, Eagle):
    def __init__(self):
        super().__init__()

    def move(self, dx, dy):
        super().run(dx, dy)

    def voice(self):
        return print(self.sound)

    def get_pos(self):
        tuple_pos = (self.x_distance, self.y_distance)
        return tuple_pos

if __name__ == '__main__':

    p1 = Pegasus()

    print(p1.get_pos())
    p1.move(10, 15)
    print(p1.get_pos())
    p1.move(-5, 20)
    print(p1.get_pos())
    p1.voice()


