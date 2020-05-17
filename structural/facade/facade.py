# Главное:
#    Паттерн Facade предоставляет простой интерфейс к сложной подсистеме классов, библиотеке или фреймворку.
# Применение:
#    Необходимо предоставить простой или урезанный интерфейс к сложной подсистеме, либо разложить эту подсистему на
#    отдльные слои функциональности.
# Реализация:
#    1. Определить какая функциональность сложной подсистемы необходима клиенту.
#    2. Создать класс фасада, который должен переадресовывать вызовы клиента нужным объектам подсистемы.
#    Фасад должен будет позаботиться о том, чтобы правильно инициализировать объекты подсистемы.
#    3. Полезно, если клиент будет работать только с фасадом. В этом случае изменения в подсистеме будут затрагивать
#    только код фасада, а клиентский код останется рабочим.


class Waiter(object):
    """ Класс сложной подсистемы 1 """
    def write_order(self):
        print('Waiter writes client\'s order')

    def send_to_kitchen(self):
        print('Send order to kitchen')

    def serve_customer(self):
        print('Customer is served!')


class Kitchen(object):
    """ Класс сложной подсистемы 2 """
    def prepare_food(self):
        print('Cook food')

    def call_waiter(self):
        print('Call Waiter')

    def wash_dishes(self):
        print('Wash the dishes')


class Order(object):
    """ Класс Фасада """
    def __init__(self, waiter=None, kitchen=None):
        """ Можно предоставить существующие объекты подсистемы или создать их самостоятельно. """
        self._waiter = waiter or Waiter()
        self._kitchen = kitchen or Kitchen()

    def order_food(self):
        self._waiter.write_order()
        self._waiter.send_to_kitchen()
        self._kitchen.prepare_food()
        self._kitchen.call_waiter()
        self._waiter.serve_customer()
        self._kitchen.wash_dishes()


if __name__ == '__main__':
    order = Order()
    order.order_food()
