from abc import ABCMeta, abstractmethod


class IArcher(metaclass=ABCMeta):
    """ Абстрактный класс лучника """
    @abstractmethod
    def die(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class LightArcher(IArcher):
    """ Конкретный класс легкого лучника """
    def __init__(self, name):
        self.health = 150
        self.damage = 15
        self.name = name

    def die(self):
        print(f'Light archer {self.name} dies!')

    def __str__(self):
        return f'Light archer {self.name}\nHealth: {self.health}\nDamage: {self.damage}'


class HeavyArcher(IArcher):
    """ Конкретный класс тяжелого лучника """
    def __init__(self, name):
        self.health = 200
        self.damage = 20
        self.name = name

    def die(self):
        print(f'Heavy archer {self.name} dies!')

    def __str__(self):
        return f'Heavy archer {self.name}\nHealth: {self.health}\nDamage: {self.damage}'


if __name__ == '__main__':
    pass
