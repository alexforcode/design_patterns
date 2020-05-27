# Главное:
#    Паттерн Iterator даёт возможность последовательно обходить элементы составных объектов, не раскрывая их
#    внутреннего представления.
# Применение:
#    1. Когда есть сложная структура данных, и нужно скрыть от клиента детали её реализации (из-за сложности или
#    вопросов безопасности).
#    2. Когда нужно иметь несколько вариантов обхода одной и той же структуры данных.
#    3. Когда нужно иметь единый интерфейс обхода различных структур данных.
# Реализация:
#    1. Создать общий интерфейс итераторов. Обязательный минимум — это операция получения следующего элемента коллекции.
#    Но для удобства можно предусмотреть и другое. Например, методы для получения предыдущего элемента, текущей позиции,
#    проверки окончания обхода и прочие.
#    2. Создать интерфейс коллекции, в нём должен быть метод получения итератора. Важно, чтобы сигнатура метода
#    возвращала общий интерфейс итераторов, а не один из конкретных итераторов.
#    3. Создать классы конкретных итераторов для тех коллекций, которые нужно обходить с помощью паттерна. Итератор
#    должен быть привязан только к одному объекту коллекции. Обычно эта связь устанавливается через конструктор.
#    4. Определить методы получения итератора в конкретных классах коллекций. Они должны создавать новый итератор
#    того класса, который способен работать с данным типом коллекции. Коллекция должна передавать ссылку на собственный
#    объект в конструктор итератора.
#    5. В клиентском коде и в классах коллекций не должно остаться кода обхода элементов. Клиент должен получать новый
#    итератор из объекта коллекции каждый раз, когда ему нужно перебрать её элементы.


from collections.abc import Iterable, Iterator
"""
Для создания итератора в Python есть два абстрактных класса из встроенного модуля collections - Iterable, Iterator. 
Нужно реализовать метод __iter__() в итерируемом объекте (списке), а метод __next__() в итераторе. (два первых шага 
реализации)
"""


class RadioStation(object):
    def __init__(self, name, frequency):
        self._name = name
        self._frequency = frequency

    @property
    def name(self):
        return self._name

    @property
    def frequency(self):
        return self._frequency

    def __str__(self):
        return f'{self._frequency} - {self._name}'


class StationIterator(Iterator):
    """ Конкретный итератор """
    def __init__(self, collection, reverse=False):
        self._collection = collection
        self._reverse = reverse  # направление обхода
        self._position = -1 if reverse else 0  # текущее положение обхода

    def __next__(self):
        """ Метод возвращает следующий элемент в последовательности. При достижении конца последовательности
        выбрасывается исключение StopIteration
        """
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()

        return value


class StationList(Iterable):
    """ Конкретная коллекция """
    def __init__(self):
        self._collection = []

    def __iter__(self):
        """ Метод возвращает объект итератора (по возрастанию) """
        return StationIterator(self._collection)

    def get_reverse(self):
        """ Метод возвращает объект итератора (по убыванию) """
        return StationIterator(self._collection, reverse=True)

    def add_station(self, item):
        self._collection.append(item)


if __name__ == '__main__':
    station_list = StationList()
    station_list.add_station(RadioStation('Silver Rain', '100.1 FM'))
    station_list.add_station(RadioStation('Radio NRJ', '104.2 FM'))
    station_list.add_station(RadioStation('Europa Plus', '106.2 FM'))

    print('Straight:')
    for station in station_list:
        print(station)
    print('')

    print('Reversed:')
    for station in station_list.get_reverse():
        print(station)
