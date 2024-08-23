from threading import Thread
import time


class Knight(Thread):
    def __init__(self, name, power, wariors=100):
        super().__init__()
        self.wariors = wariors
        self.name = name
        self.power = power


    def run(self):
        print(f'{self.name} на нас напали!')
        days = 0
        while self.wariors != 0:
            self.wariors = self.wariors - self.power
            days += 1
            print(f'{self.name} сражается {days} день(дня) осталось {self.wariors} воинов')
            time.sleep(1)
        print(f'{self.name} одержал победу спустя {days} дней')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
