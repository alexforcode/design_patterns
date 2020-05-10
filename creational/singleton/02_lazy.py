class Singleton(object):
    """ Класс с "ленивой инициализацией".
    Создает объект при первом вызове метода get_instance
    """
    _instance = None

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = Singleton()
            Singleton.__attrs = []
        return cls._instance

    def add_to_attrs(self, *args):
        if not Singleton._instance:
            return
        self.__attrs += list(args)

    def get_attrs(self):
        if not Singleton._instance:
            return
        return self.__attrs


if __name__ == '__main__':
    s1 = Singleton()
    s1.add_to_attrs(3, 5)
    print(s1.get_attrs())

    s2 = Singleton()
    s2 = s2.get_instance()
    s2.add_to_attrs(4, 2)

    s1 = s1.get_instance()
    print(s1.get_attrs())

    print(s1 == s2)