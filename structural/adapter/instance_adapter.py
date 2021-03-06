# Главное:
#    Паттерн Adapter преобразует интерфейс класса к другому интерфейсу, на который рассчитан клиент. Это позволяет
#    объектам с несовместимыми интерфейсами работать вместе.
# Применение:
#    Необходимо использовать сторонний класс (сервис), но его интерфейс не соответствует остальному коду приложения
#    (клиент).
# Реализация:
#    1. Описать клиентский интерфейс, через который классы приложения смогли бы использовать класс сервиса.
#    2. Создать класс адаптера, реализовав этот интерфейс.
#    3. В адаптере должен быть атрибут, который хранит ссылку на объект сервиса. Либо созданный в конструкторе,
#    либо переданный через параметры методов класса.
#    4. Реализовать все методы клиентского интерфейса в адаптере. Адаптер должен делегировать основную работу сервису.


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


class RunForrest(IClient):
    """ Адаптер для взаимодействия класса сервиса с клиентом """
    def __init__(self):
        self.forrest = Forrest()

    def run(self, speed):
        print(f'Run, {self.forrest.name}, run!')
        self.forrest.walk(speed)


if __name__ == '__main__':
    # Проверка класса сервиса
    forrest = Forrest()
    forrest.walk(5)

    # Код клиента
    forrest = RunForrest()
    forrest.run(20)