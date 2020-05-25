# Главное:
#    Паттерн Decorator позволяет динамически добавлять объектам новую функциональность, оборачивая их в полезные
#    «обёртки».
# Применение:
#    1. Когда нужно добавлять обязанности объектам на лету, незаметно для кода, который их использует.
#    2. Когда нельзя расширить обязанности объекта с помощью наследования.
# Реализация:
#    1. В коде должен присутствовать основной компонент и несколько опциональных надстроек над ним. Создать интерфейс
#    компонента, который описывал бы общие методы как для основного компонента, так и для его дополнений.
#    2. Создать класс конкретного компонента и поместите в него основную бизнес-логику.
#    3. Создать базовый класс декораторов. Он должен иметь поле для хранения ссылки на вложенный объект-компонент. Все
#    методы базового декоратора должны делегировать действие вложенному объекту. И конкретный компонент, и базовый
#    декоратор должны следовать одному и тому же интерфейсу компонента.
#    4. Создать классы конкретных декораторов, наследуя их от базового декоратора. Конкретный декоратор должен
#    выполнять свою добавочную функцию, а затем (или перед этим) вызывать эту же операцию обёрнутого объекта.
#    5. Клиент берёт на себя ответственность за конфигурацию и порядок обёртывания объектов.


from abc import ABCMeta, abstractmethod


class INotifier(metaclass=ABCMeta):
    """ Абстрактный класс для рассылки уведомлений """
    @abstractmethod
    def send(self, message):
        pass


class EmailNotifier(INotifier):
    """ Конкретный класс рассылки уведомлений через email (базовая рассылка) """
    def send(self, message):
        print(f'Email: {message}')


class NotifierDecorator(INotifier):
    """ Базовый класс декораторов для рассылки уведомлений другими способами """
    def __init__(self, component):
        self._component = component

    @property
    def component(self):
        return self._component

    def send(self, message):
        return self._component.send(message)


class SMSNotifierDecorator(NotifierDecorator):
    """ Рассылка уведомлений через sms """
    def send(self, message):
        self.component.send(message)
        print(f'SMS: {message}')


class VKNotifierDecorator(NotifierDecorator):
    """ Рассылка уведомлений через vk """
    def send(self, message):
        self.component.send(message)
        print(f'VK: {message}')


class FacebookNotifierDecorator(NotifierDecorator):
    """ Рассылка уведомлений через facebook """
    def send(self, message):
        self.component.send(message)
        print(f'Facebook: {message}')


def send_notifications(component, message):
    component.send(message)


if __name__ == '__main__':
    notification = EmailNotifier()
    print('-- Simple notification --')
    send_notifications(notification, 'LO')

    notification = FacebookNotifierDecorator(notification)
    notification = VKNotifierDecorator(notification)
    notification = SMSNotifierDecorator(notification)
    print('-- Notification with decorators --')
    # Уведомления рассылаются в порядке обертывания компонентов
    # Email -> Facebook -> VK -> SMS
    send_notifications(notification, 'LO')
