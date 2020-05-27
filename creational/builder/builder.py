# Главное:
#    Паттерн Decorator позволяет создавать сложные объекты пошагово. Строитель даёт возможность использовать один и
#    тот же код строительства для получения разных представлений объектов.
# Применение:
#    1. Когда нужно избавиться от «телескопического конструктора».
#    2. Когда код должен создавать разные представления какого-то объекта.
#    3. Когда нужно собирать сложные составные объекты.
# Реализация:
#    1. Описать общие шаги создания разных представлений объекта в общем интерфейсе строителей.
#    2. Для каждого из представлений объекта-продукта создать по одному классу-строителю и реализовать их методы
#    строительства. Также нужно описать метод получения результата. Обычно конкретные строители определяют собственные
#    методы получения результата строительства, поскольку продукты не обязательно должны иметь общий базовый класс или
#    интерфейс. Но всегда можно добавить метод получения результата в общий интерфейс, если строители производят
#    однородные продукты с общим предком.
#    3. При необходимости создать класс директора. Его методы будут создавать различные конфигурации продуктов, вызывая
#    разные шаги одного и того же строителя.
#    4. Перед началом строительства клиент должен связать определённого строителя с директором. Это можно сделать либо
#    через конструктор, либо через сеттер, либо подав строителя напрямую в строительный метод директора.
#    5. Результат строительства можно вернуть из директора, но только если метод возврата продукта удалось поместить
#    в общий интерфейс строителей. Иначе директор будет жестко привязан к конкретным классам строителей.


from abc import ABCMeta, abstractmethod


class Person(object):
    """ Класс объекта-продукта """
    def __init__(self):
        self._name = None
        self._surname = None
        self._age = None

    def with_name(self, name):
        self._name = name

    def with_surname(self, surname):
        self._surname = surname

    def with_age(self, age):
        self._age = age

    def __str__(self):
        data = f'Name: {self._name} \n' if self._name else 'Name: - \n'
        data += f'Surname: {self._surname} \n' if self._surname else 'Surname: - \n'
        data += f'Age: {self._age}' if self._age else 'Age: -'
        return data


class IBuilder(metaclass=ABCMeta):
    """ Абстрактный класс строителя объявляет создающие методы для различных частей объектов продуктов """
    @abstractmethod
    def _reset(self):
        pass

    @abstractmethod
    def add_name(self, name):
        pass

    @abstractmethod
    def add_surname(self, surname):
        pass

    @abstractmethod
    def add_age(self, age):
        pass


class PersonBuilder(IBuilder):
    """ Конкретный класс строителя """
    def __init__(self):
        """ Новый экземпляр строителя должен содержать пустой объект продукта """
        self._person = None
        self._reset()

    def _reset(self):
        self._person = Person()

    def add_name(self, name):
        self._person.with_name(name)
        return self

    def add_surname(self, surname):
        self._person.with_surname(surname)
        return self

    def add_age(self, age):
        self._person.with_age(age)
        return self

    def build(self):
        """ После возвращения клиенту конечного результата вызывается метод сброса объекта продукта """
        person = self._person
        self._reset()
        return person


class Director(object):
    """ Класс директор отвечает только за выполнения шагов строителя в определенной последовательности.
    Это полезно при производстве продуктов в определённом порядке или особой конфигурации.
    Класс Директор необязателен, так как клиент может напрямую управлять строителями.
    """
    def __init__(self):
        self._builder = None

    @property
    def builder(self):
        return self._builder

    @builder.setter
    def builder(self, builder):
        self._builder = builder

    def build_stranger(self):
        """ Метод строительства объекта продукта определенной конфигурации. """
        self._builder.add_name('John')
        self._builder.add_surname('Doe')
        self._builder.add_age(30)


if __name__ == '__main__':
    # with Director
    builder = PersonBuilder()
    director = Director()
    director.builder = builder
    director.build_stranger()
    person1 = builder.build()
    print(person1)
    print('')

    # without Director
    person2 = PersonBuilder().build()
    print(person2)
    print('')

    person3 = PersonBuilder().add_name('Paul').add_age(25).build()
    print(person3)
