# Главное:
#   Паттерн Простая фабрика представляет собой объект (класс), содержащий метод, который на основе некоего параметра
#   создает необходимый экземпляр класса (продукт).
# Применение:
#   Генерирует для клиента экземпляр класса, скрывая от него (клиента) логику экземпляра.
# Реализация:
#   1. Создать несколько классов, экземпляры которых необходимо вернуть.
#   2. Создать класс, содержащий метод-фабрику, который возвращает необходимый экземпляр на основе параметра.


from abc import ABC, abstractmethod


class Hero(ABC):
    """ Абстрактный класс героя """
    def __init__(self, name, health):
        self.name = name
        self.health = health

    @abstractmethod
    def attack(self):
        pass


class Knight(Hero):
    """ Конкретный класс героя (рыцарь) """
    def attack(self):
        print(f'Knight {self.name} is attacking!')

    def __str__(self):
        return f'Knight: {self.name}. Health: {self.health}'


class Archer(Hero):
    """ Конкретный класс героя (лучник) """
    def attack(self):
        print(f'Archer {self.name} is attacking!')

    def __str__(self):
        return f'Archer: {self.name}. Health: {self.health}'


class HeroFactory(object):
    """ Класс с методом-фабрикой create_hero, возвращающим
    конекретный класс героя на основе атрибута hero_class
    """
    @staticmethod
    def create_hero(hero_class, name, health):
        try:
            if hero_class.lower() == 'knight':
                return Knight(name, health)
            if hero_class.lower() == 'archer':
                return Archer(name, health)
            raise AssertionError('Cannot find hero class!')
        except AssertionError as _e:
            print(_e)


if __name__ == '__main__':
    lancelot = HeroFactory().create_hero('Knight', 'Lancelot', 150)
    arthur = HeroFactory().create_hero('Knight', 'Arthur', 200)
    robin_hood = HeroFactory().create_hero('Archer', 'Robin Hood', 100)

    print(lancelot)
    print(arthur)
    print(robin_hood)

    lancelot.attack()
    arthur.attack()
    robin_hood.attack()

