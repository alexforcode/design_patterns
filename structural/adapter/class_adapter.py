# Реализация:
#    1. Описать клиентский интерфейс, через который классы приложения смогли бы использовать класс сервиса.
#    2. Создать класс адаптера, реализовав этот интерфейс и унаследоваться от класса сервиса.
#    3. Реализовать все методы клиентского интерфейса в адаптере. Адаптер должен делегировать основную работу сервису.


from abc import ABCMeta, abstractmethod


class Forrest(object):
    """ Класс стороннего сервиса """
    def __init__(self):
        self.name = 'Forrest'

    def walk(self, speed):
        print(f'{self.name}: {speed} km/h')


class IClient(metaclass=ABCMeta):
    """ Интерфейс клиента для взаимодействия с классом сервиса """
    @abstractmethod
    def run(self, speed):
        pass


class RunForrest(Forrest, IClient):
    """ Адаптер для взаимодействия класса сервиса с клиентом """
    def run(self, speed):
        print(f'Run, {self.name}, run!')
        self.walk(speed)


if __name__ == '__main__':
    # Проверка класса сервиса
    forrest = Forrest()
    forrest.walk(5)

    # Код клиента
    forrest = RunForrest()
    forrest.run(20)
