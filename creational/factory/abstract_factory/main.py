# Главное:
#   Абстрактная фабрика — это порождающий паттерн проектирования, который решает проблему создания целых семейств
#   связанных продуктов, без указания конкретных классов продуктов. Абстрактная фабрика задаёт интерфейс создания
#   всех доступных типов продуктов, а каждая конкретная реализация фабрики порождает продукты одной из вариаций.
#   Клиентский код вызывает методы фабрики для получения продуктов, вместо самостоятельного создания.
# Применение:
#   Паттерн можно часто встретить в условиях, где требуется создание семейств продуктов (например, внутри фреймворков).
# Реализация:
#   1. Создать несколько семейств продуктов.
#   2. Создать абстрактный класс создатель, определяющий методы создания продуктов.
#   3. Для каждого конкретного семейства продуктов создать конкретный класс создатель, переопределяющий
#   методы, возвращающие конкретные продукты.


from abc import ABCMeta, abstractmethod
from random import choice

from knights import HeavyKnight, LightKnight
from archers import HeavyArcher, LightArcher


class IWarriorMaker(metaclass=ABCMeta):
    """ Абстрактный класс 'Создатель' """
    def __init__(self):
        self.names = ['Arthur', 'Lancelot', 'Robin', 'Bedevere', 'Galahad', 'Who Say Ni']

    @abstractmethod
    def get_light_warrior(self):
        pass

    @abstractmethod
    def get_heavy_warrior(self):
        pass


class ArcherMaker(IWarriorMaker):
    """ Конкретный класс для создания лучников """
    def get_light_warrior(self):
        return LightArcher(choice(self.names))

    def get_heavy_warrior(self):
        return HeavyArcher(choice(self.names))


class KnightMaker(IWarriorMaker):
    """ Конкретный класс для создания рыцарей """

    def get_light_warrior(self):
        return LightKnight(choice(self.names))

    def get_heavy_warrior(self):
        return HeavyKnight(choice(self.names))


if __name__ == '__main__':
    light_archer = ArcherMaker().get_light_warrior()
    print(light_archer)
    light_archer.die()

    heavy_knight = KnightMaker().get_heavy_warrior()
    print(heavy_knight)
    heavy_knight.die()
