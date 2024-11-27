from threading import Thread

from time import sleep


class Knight(Thread):

    def __init__(self, name, power):
        self.lancelot = name
        self.power = power
        super().__init__()

    def run(self):
        print(f'{self.lancelot}, на нас напали!')
        enemy = 100
        day = 0

        while enemy > 0:
            enemy -= self.power
            day += 1
            sleep(1)
            print(f'{self.lancelot} сражается {day}, осталось {enemy} воинов')
        print(f'{self.lancelot} одержал победу спустя {day} дней(дня)!')


first_knight = Knight("Sir Lancelot", 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все враги повержены!')
