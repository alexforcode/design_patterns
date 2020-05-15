from abc import ABCMeta, abstractmethod
from random import randint


class IKnight(metaclass=ABCMeta):
    """ Абстрактный класс рыцаря """
    @abstractmethod
    def die(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class LightKnight(IKnight):
    """ Конкретный класс легкого рыцаря """
    def __init__(self, name):
        self.health = 200
        self.damage = 30
        self.name = name

    def die(self):
        print(f'Light knight {self.name} dies!')

    def __str__(self):
        return f'Light knight {self.name}\nHealth: {self.health}\nDamage: {self.damage}'


class HeavyKnight(IKnight):
    """ Конкретный класс тяжелого рыцаря """
    def __init__(self, name):
        self.health = 250
        self.damage = 35
        self.name = name

    def die(self):
        print(f'Heavy knight {self.name} dies!')

    def __str__(self):
        return f'Heavy knight {self.name}\nHealth: {self.health}\nDamage: {self.damage}'


if __name__ == '__main__':
    pass
