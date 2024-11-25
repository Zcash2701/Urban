import threading
import random
import time

lock = threading.Lock()

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):

        for transaction_i in range(1, 101):
            replenishment = random.randint(50, 500)
            self.balance += replenishment
            print(f'Пополнение №{transaction_i}: {replenishment}. Баланс: {self.balance}')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            time.sleep(0.001)

    def take(self):

        for transaction_i in range(1, 101):
            withdrawal = random.randint(50, 500)
            print(f'Запрос  №{transaction_i} на {withdrawal}')
            if withdrawal <= self.balance:
                self.balance -= withdrawal
                print(f'Снятие №{transaction_i}: {withdrawal}. Баланс: {self.balance}')
            else:
                print(f'Запрос №{transaction_i} отклонён, недостаточно средств.')
                self.lock.acquire()
            time.sleep(0.001)

bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')