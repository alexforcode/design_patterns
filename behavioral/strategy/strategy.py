# Главное:
#    Паттерн Strategy определяет семейство схожих алгоритмов и помещает каждый из них в собственный класс, после чег
#    алгоритмы можно взаимозаменять прямо во время исполнения программы.
# Применение:
#    1. Когда нужно использовать разные вариации какого-то алгоритма внутри одного объекта.
#    2. Когда есть множество похожих классов, отличающихся только некоторым поведением.
#    3. Когда нужно скрыть детали реализации алгоритмов для других классов.
# Реализация:
#    1. Создать интерфейс стратегий, описывающий алгоритм. Он должен быть общим для всех вариантов алгоритма.
#    2. Поместить вариации алгоритма в собственные классы, которые реализуют этот интерфейс.
#    3. В классе контекста должно присутствовать поле для хранения ссылки на текущий объект-стратегию, а также метод
#    для её изменения. Контекст должен работать с этим объектом только через общий интерфейс стратегий.
#    4. Клиенты контекста должны подавать в него соответствующий объект-стратегию, когда хотят, чтобы контекст вёл себя
#    определённым образом.


from abc import ABCMeta, abstractmethod
from random import randint


class ISortStrategy(metaclass=ABCMeta):
    """ Абстрактный класс сортировки """
    @abstractmethod
    def sort(self, lst):
        pass


class BubbleSortStrategy(ISortStrategy):
    """ Конкретный класс пузырьковой сортировки """
    def sort(self, lst):
        print('Bubble sort performing...')

        for i in range(1, len(lst)):
            for k in range(len(lst) - i):
                if lst[k] > lst[k + 1]:
                    lst[k], lst[k + 1] = lst[k + 1], lst[k]

        return lst


class InsertionSortStrategy(ISortStrategy):
    """ Конкретный класс сортировки вставками"""
    def sort(self, lst):
        print('Insertion sort performing...')

        for top in range(1, len(lst)):
            k = top
            while k > 0 and lst[k - 1] > lst[k]:
                lst[k], lst[k - 1] = lst[k - 1], lst[k]
                k -= 1

        return lst


class Context(object):
    """ Класс контекста для хранения и изменения ссылки на конкретную стратегию сортировки """
    def __init__(self):
        self._strategy = None

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, val):
        """ Изменение выбранной стратегии сортировки """
        self._strategy = val

    def sort(self, lst):
        """ Сортировать список, используя метод выбранной стратегии сортировки """
        return self._strategy.sort(lst)


class SortMachine(object):
    """ Класс сортировочной машины, выбирает стратегию сортировки на основе длины списка """
    def __init__(self):
        self.context = Context()

    def perform_sort(self, lst):
        if len(lst) <= 50:
            self.context.strategy = BubbleSortStrategy()
        else:
            self.context.strategy = InsertionSortStrategy()
        return self.context.sort(lst)


if __name__ == '__main__':
    sort_machine = SortMachine()

    not_sorted_lst = [randint(0, 100) for i in range(50)]
    sorted_lst = sort_machine.perform_sort(not_sorted_lst)
    print(sorted_lst)

    not_sorted_lst = [randint(0, 100) for i in range(100)]
    sorted_lst = sort_machine.perform_sort(not_sorted_lst)
    print(sorted_lst)
