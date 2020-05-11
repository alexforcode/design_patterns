from threading import Lock, Thread


class SingletonMeta(type):
    """ Потокобезопасная реализация Singleton.
    Релизует синхронизацию потоков во время первого создания экземпляра класса
    с помощью объекта-блокировки _lock
    """
    _instance = None
    _lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if not cls._instance:
                cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class Singleton(metaclass=SingletonMeta):
    def __init__(self):
        self._attrs = []

    def add_to_attrs(self, *args):
        self._attrs += list(args)

    def get_attrs(self):
        return self._attrs


def create_singleton(res, index):
    res[index] = Singleton()


if __name__ == '__main__':
    results = [None] * 3
    threads = []
    for i in range(3):
        process = Thread(target=create_singleton, args=[results, i])
        process.start()
        threads.append(process)

    for process in threads:
        process.join()

    s1, s2, s3 = results

    print(s1 == s2 == s3)

    s1.add_to_attrs('added from s1')
    s2.add_to_attrs('added from s2')
    print(s3.get_attrs())
