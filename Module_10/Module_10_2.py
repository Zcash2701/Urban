import threading
import time
class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def counter(self, name, power):
        enemy = 100
        count_day = 0
        while enemy:
            enemy -= power
            count_day += 1
            time.sleep(1)
            print(f'{name}, сражается {count_day} день(дня)..., осталось {enemy} воинов')

        return count_day
    def run(self):
        print(f'{self.name} На нас напали!')
        count_day = self.counter(self.name, self.power)
        print(f'{self.name} одержал победу спустя {count_day} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()