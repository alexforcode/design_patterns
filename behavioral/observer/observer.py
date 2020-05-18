# Главное:
#    Паттерн Observer создаёт механизм подписки, позволяющий одним объектам следить и реагировать на события,
#    происходящие в других объектах.
# Применение:
#    1. Когда после изменения состояния одного объекта требуется что-то сделать в других, но неизвестно,
#    какие именно объекты должны отреагировать.
#    2. Когда одни объекты должны наблюдать за другими, но только в определённых случаях.
# Реализация:
#    1. Создать интерфейс подписчиков. В нём достаточно определить единственный метод оповещения.
#    2. Создать интерфейс издателей и описать в нём операции управления подпиской.
#    3. Создать классы конкретных издателей. После каждого изменения состояния они должны отправлять оповещения всем
#    своим подписчикам.
#    4. Реализовать метод оповещения у конкретных подписчиков.
#    5. Клиент должен создавать необходимое количество объектов подписчиков и подписывать их у издателей.


from abc import ABCMeta, abstractmethod


class IReader(metaclass=ABCMeta):
    """ Абстрактный класс подписчика с методом оповещения """
    @abstractmethod
    def update(self, msg):
        """ Получение оповещения от издателя """
        pass


class Reader(IReader):
    """ Конкретный класс подписчика """
    def __init__(self, name):
        self.name = name

    def update(self, msg):
        print(f'New article for {self.name}: {msg}')


class INewsFeed(metaclass=ABCMeta):
    """ Абстрактный класс издателя """
    @abstractmethod
    def subscribe(self, news_type, reader):
        """ Подписка на новости определенной темы """
        pass

    @abstractmethod
    def unsubscribe(self, news_type, reader):
        """ Отписка от новостей определенной темы """
        pass

    @abstractmethod
    def _notify(self, news_type, title):
        """ Оповещение подписчиков """
        pass


class NewsFeed(INewsFeed):
    """ Конкретный класс издателя """
    def __init__(self):
        self._subscribers = {
            'sport': set(),
            'music': set(),
            'humor': set(),
        }
        self.news = []

    def subscribe(self, news_type, reader):
        print(f'NewsFeed: new subscriber for {news_type}: {reader.name}')
        self._subscribers[news_type].add(reader)

    def unsubscribe(self, news_type, reader):
        print(f'NewsFeed: unsubscribed from {news_type}: {reader.name}')
        self._subscribers[news_type].discard(reader)

    def _notify(self, news_type, title):
        print('NewsFeed: Notifying subscribers...')
        for subscriber in self._subscribers[news_type]:
            subscriber.update(title)

    def add_news(self, news_type, title):
        self.news.append((news_type, title))
        self._notify(news_type, title)


if __name__ == '__main__':
    news = NewsFeed()

    john = Reader('John')
    george = Reader('George')
    paul = Reader('Paul')
    ringo = Reader('Ringo')

    news.subscribe('humor', john)
    news.subscribe('sport', paul)
    news.subscribe('music', george)
    news.subscribe('humor', ringo)

    news.add_news('sport', 'Sport article')
    news.add_news('music', 'Music article')
    news.add_news('humor', 'Humor article')

    news.unsubscribe('humor', ringo)