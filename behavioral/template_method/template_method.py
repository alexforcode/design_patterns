# Главное:
#    Паттерн Template Method определяет основные шаги алгоритма, оставляя подклассам возможность переопределять
#    некоторые из них, не меняя общей структуры.
# Применение:
#    1. Когда подклассы должны расширять базовый алгоритм, не меняя его структуры.
#    2. Когда есть несколько классов, делающих одно и то же с незначительными отличиями. Если редактировать один класс,
#    то приходится вносить такие же правки и в остальные классы.
# Реализация:
#    1. Создать абстрактный базовый класс. Определить в нём шаблонный метод. Этот метод должен состоять из вызовов
#    шагов алгоритма.
#    2. Добавить в абстрактный класс методы для каждого из шагов алгоритма. Можно сделать эти методы абстрактными или
#    добавить какую-то реализацию по умолчанию. Также можно добавить в алгоритм хуки (дополнительные методы, которые
#    подклассы могут переопределять, но это необязательно, потому что у хуков уже должна быть стандартная (пустая,
#    pass) реализация).
#    3. Создать конкретные классы, унаследовав их от абстрактного класса. Реализовать в них все недостающие шаги и хуки.


from abc import ABCMeta, abstractmethod


class IBeverage(metaclass=ABCMeta):
    """ Абстрактный класс для приготовления напитков """
    def boil_water(self):
        print('Boiling water...')

    def pour_in_cup(self):
        print('Pouring water into cup...')

    @abstractmethod
    def brew(self):
        """ Абстрактный метод для реализации в подклассе """
        pass

    def add_extra(self):
        """ Метод-хук """
        pass

    @abstractmethod
    def finish(self):
        """ Абстрактный метод для реализации в подклассе """
        pass

    def make(self):
        """ Шаблонный метод """
        self.boil_water()
        self.pour_in_cup()
        self.brew()
        self.add_extra()
        self.finish()


class Tea(IBeverage):
    """ Конкретный класс напитка """
    def brew(self):
        print('Steeping the tea...')

    def add_extra(self):
        """ Реализация метода-хука """
        if input('Add lemon? (y/n): ').lower() == 'y':
            print('Adding lemon...')

    def finish(self):
        print('Tea is ready!')


class Coffee(IBeverage):
    """ Конкретный класс напитка """
    def brew(self):
        print('Pouring coffee...')

    def add_extra(self):
        """ Реализация метода-хука """
        if input('Add milk? (y/n): ').lower() == 'y':
            print('Adding milk...')

    def finish(self):
        print('Coffee is ready!')


class CoffeeHouse(object):
    """ Класс клиента """
    def __init__(self):
        self._beverages = {
            'tea': Tea,
            'coffee': Coffee
        }

    def choose_beverage(self):
        beverage = None
        while beverage not in ['tea', 'coffee']:
            beverage = input('Do you want tea or coffee? ').lower()
        self._make_beverage(self._beverages[beverage]())

    @staticmethod
    def _make_beverage(beverage):
        beverage.make()


if __name__ == '__main__':
    cafe = CoffeeHouse()
    cafe.choose_beverage()
