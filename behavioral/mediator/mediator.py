# Главное:
#    Паттерн Mediator позволяет уменьшить связанность множества классов между собой, благодаря перемещению этих связей
#    в один класс-посредник.
# Применение:
#    1. Когда сложно менять некоторые классы из-за того, что они имеют множество хаотичных связей с другими классами.
#    2. Когда нет возможности повторно использовать класс, поскольку он зависит от уймы других классов.
#    3. Когда приходится создавать множество подклассов компонентов, чтобы использовать одни и те же компоненты в
#    разных контекстах.
# Реализация:
#    1. Создать общий интерфейс посредников и описать в нём методы для взаимодействия с компонентами. В простейшем
#    случае достаточно одного метода для получения оповещений от компонентов. Интерфейс необходим, если нужно повторно
#    использовать классы компонентов для других задач. В этом случае всё, что нужно сделать — это создать новый класс
#    конкретного посредника.
#    2. Реализовать этот интерфейс в классе конкретного посредника. В нем должны присутствовать поля, которые будут
#    содержать ссылки на все объекты компонентов.
#    3. Можно пойти дальше и переместить код создания компонентов в класс посредника, после чего он может напоминать
#    фабрику или фасад.
#    4. Компоненты тоже должны иметь ссылку на объект посредника. Связь между ними удобнее всего установить, подавая
#    посредника в параметры конструктора компонентов.
#    6. Организовать код компонентов так, чтобы они вызывали метод оповещения посредника, вместо методов других
#    компонентов. С противоположной стороны, посредник должен вызывать методы нужного компонента, когда получает
#    оповещение от компонента.

from abc import ABCMeta, abstractmethod


class IChatMediator(metaclass=ABCMeta):
    """ Общий интерфейс посредников """
    @abstractmethod
    def notify(self, sender, message):
        pass


class ChatRoom(IChatMediator):
    """ Класс конкретного посредника """
    def __init__(self, contact1, contact2):
        self._contact1 = contact1
        self._contact1.chat_room = self
        self._contact2 = contact2
        self._contact2.chat_room = self

    def notify(self, sender, message):
        if sender == self._contact1:
            self._contact2.receive(message)
        else:
            self._contact1.receive(message)


class Contact:
    """ Класс компонента """
    def __init__(self, name):
        self._chat_room = None
        self._name = name

    @property
    def chat_room(self):
        return self._chat_room

    @chat_room.setter
    def chat_room(self, chat_room):
        self._chat_room = chat_room

    def send(self, message):
        print(f'{self._name} sends: {message}')
        self._chat_room.notify(self, message)

    def receive(self, message):
        print(f'{self._name} receive: {message}')


if __name__ == '__main__':
    john = Contact('John')
    paul = Contact('Paul')
    chat1 = ChatRoom(john, paul)

    george = Contact('George')
    ringo = Contact('Ringo')
    chat2 = ChatRoom(george, ringo)

    print('--- Chat Room 1 ---')
    john.send('Hello!')
    paul.send('Hi!')

    print('--- Chat Room 2 ---')
    george.send('Good Morning!')
    ringo.send('Howdy!')