class SingletonMeta(type):
    """Проверяет, что создается один экземпляр класса"""
    _instance = None

    def __call__(cls):
        if not cls._instance:
            cls._instance = super().__call__()
        return cls._instance


class Singleton(metaclass=SingletonMeta):
    """Основная функциональность"""
    def __init__(self):
        self._attrs = []

    def add_to_attrs(self, *args):
        self._attrs += list(args)

    def get_attrs(self):
        return self._attrs


if __name__ == '__main__':
    s1 = Singleton()
    s2 = Singleton()
    print(s1 == s2)

    s1.add_to_attrs(4, 5, 6)
    print(s2.get_attrs())
