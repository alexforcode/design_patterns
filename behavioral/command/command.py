# Главное:
#    Паттерн Command превращает запросы в объекты, позволяя передавать их как аргументы при вызове методов, ставить
#    запросы в очередь, логировать их, а также поддерживать отмену операций.
# Применение:
#    1. Когда нужно параметризовать объекты выполняемым действием. Команда превращает операции в объекты. А объекты
#    можно передавать, хранить и взаимозаменять внутри других объектов.
#    2. Когда нужно ставить операции в очередь, выполнять их по расписанию или передавать по сети.
#    3. Когда нужна операция отмены. Чтобы иметь возможность отмены операций нужно реализовать хранение истории.
#    История команд выглядит как стек, в который попадают все выполненные объекты команд. Каждая команда перед
#    выполнением операции сохраняет текущее состояние объекта, с которым она будет работать. После выполнения операции
#    копия команды попадает в стек истории, все ещё неся в себе сохранённое состояние объекта. Если потребуется отмена,
#    программа возьмёт последнюю команду из истории и возобновит сохранённое в ней состояние.
# Реализация:
#    1. Создать интерфейс команд и определить в нем метод запуска.
#    2. Создать классы конкретных команд. В них могут присутствовать (получены через конструктор): поле для хранения
#    ссылки на один или несколько объектов-получателей, которым команда будет перенаправлять основную работу;
#    поля для хранения параметров, которые нужны при вызове методов получателя. Также нужно реализовать метод запуска,
#    вызывая в нем методы получателя.
#    3. Создать классы отправителей команд. В них должны присутствовать поля для хранения объектов команд (которые
#    полученны через конструктор, или метод-сеттер.


from abc import ABCMeta, abstractmethod


class ICommand(metaclass=ABCMeta):
    """ Абстрактный метод команды с методом запуска """
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class LightOnCommand(ICommand):
    """ Конкретная команда """
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.on()

    def undo(self):
        self.receiver.off()


class LightOffCommand(ICommand):
    """ Конкретная команда """
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.off()

    def undo(self):
        self.receiver.on()


class Light(object):
    """ Получатель команд """
    def __init__(self, place):
        self.place = place

    def on(self):
        print(f'Light in {self.place} is On')

    def off(self):
        print(f'Light in {self.place} is Off')


class RemoteControl(object):
    """ Отправитель команд """
    def __init__(self):
        self.command = None
        self.undo_command = None

    def set_command(self, command):
        self.command = command

    def press_button(self):
        self.command.execute()
        self.undo_command = self.command

    def undo(self):
        self.undo_command.undo()


if __name__ == '__main__':
    light = Light('living room')
    remote = RemoteControl()

    remote.set_command(LightOnCommand(light))
    remote.press_button()
    remote.undo()

    remote.set_command(LightOffCommand(light))
    remote.press_button()
    remote.undo()
