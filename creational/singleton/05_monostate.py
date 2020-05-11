# Паттерн Monostate позволяет создавать экземпляры класса, имеющий доступ к одному и тому же состоянию.


class MonoState(object):
    """ Присваивает переменную __dict__ переменной класса __shared_state,
    что позволяет экземплярам класса иметь доступ к одному и тому же состоянию.
    """
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state
        self.shared = True


if __name__ == '__main__':
    cl1 = MonoState()
    cl1.foo = 'bar'
    print(cl1.__dict__)

    cl2 = MonoState()
    print(cl2.__dict__)
    cl2.foo = 'spam'
    cl2.changed = True

    print(cl1.__dict__)
    print(cl2.__dict__)
    print(cl1 == cl2)

