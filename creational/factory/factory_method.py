# Главное:
#   Паттерн Фабричный метод определяет интерфейс для создания объекта, но оставляет подклассам решение о том,
#   какой класс инстанцировать. Фабричный метод позволяет классу делегировать создание подклассов.
# Применение:
#   Паттерн можно часто встретить в условиях, где требуется гибкость при создании продуктов.
# Реализация:
#   1. Создать абстрактный класс продукта.
#   2. Создать несколько конкретных классов продуктов, экземпляры которых необходимо вернуть.
#   3. Создать абстрактный класс создатель, содержащий метод-фабрику.
#   4. Для каждого конкртеного продукта создать конкретный класс создатель, содержащий переопределенный метод-фабрику,
#   возвращающий этот продукт.


from abc import ABCMeta, abstractmethod


class Hero(metaclass=ABCMeta):
    """ Абстрактный класс героя """
    def __init__(self, name, health):
        self.name = name
        self.health = health

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def __str__(self):
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


class HeroMaker(metaclass=ABCMeta):
    """ Абстрактный класс 'Создатель', объявляющий фабричный метод create_hero, который должен возвращать экземпляр
    класса Hero (или его подклассов).
    """
    @abstractmethod
    def create_hero(self, name, health):
        pass


class KnightMaker(HeroMaker):
    """ Конкретный 'Создатель'.
    Метод create_hero возвращает экземпляр класса Knight.
    """
    def create_hero(self, name, health):
        return Knight(name, health)


class ArcherMaker(HeroMaker):
    """ Конкретный 'Создатель'.
    Метод create_hero возвращает экземпляр класса Archer.
    """
    def create_hero(self, name, health):
        return Archer(name, health)


if __name__ == '__main__':
    knight = KnightMaker().create_hero('King Arthur', 200)
    archer = ArcherMaker().create_hero('Robin Hood', 150)

    print(knight)
    print(archer)

    knight.attack()
    archer.attack()
