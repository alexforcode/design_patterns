# Главное:
#    Паттерн State позволяет объектам менять поведение в зависимости от своего состояния. Извне создаётся впечатление,
#    что изменился класс объекта.
# Применение:
#    1. Когда есть объект, поведение которого меняется в зависимости от внутреннего состояния, причём типов состояний
#    много, и их код часто меняется.
#    2. Когда код класса содержит множество больших, похожих друг на друга, условных операторов, которые выбирают
#    поведения в зависимости от текущих значений полей класса.
#    3. Когда используется табличная машина состояний, построенная на условных операторах.
# Реализация:
#    1. Создать класс контекста.
#    2. Создать общий интерфейс состояний. Он должен описывать методы, общие для всех состояний. Не всё поведение
#    контекста нужно переносить в состояние, а только то, которое зависит от состояний.
#    3. Для каждого фактического состояния создать класс, реализующий интерфейс состояния. Все методы интерфейса
#    состояния должны быть реализованы во всех классах состояний. При переносе поведения из контекста можно столкнуться
#    с тем, что это поведение зависит от приватных полей или методов контекста, к которым нет доступа из объекта
#    состояния. Самый простой способ это обойти — оставить поведение внутри контекста, вызывая его из объекта состояния.
#    4. Создать в контексте поле для хранения объектов-состояний, а также публичный метод для изменения значения этого
#    поля.
#    5. Методы контекста, в которых находился зависимый от состояния код, заменить на вызовы соответствующих методов
#    объекта-состояния.
#    6. Разместить код, который переключает состояние контекста либо внутри контекста, либо внутри классов конкретных
#    состояний.


from abc import ABCMeta, abstractmethod


class IState(metaclass=ABCMeta):
    """ Абстрактный класс всех состояний """
    def __init__(self, player):
        self.player = player

    @abstractmethod
    def click_play(self):
        pass

    @abstractmethod
    def click_next(self, seconds=None):
        pass

    @abstractmethod
    def click_previous(self, seconds=None):
        pass


class ReadyState(IState):
    """ Конкретное состояние """
    def click_play(self):
        player.play()
        player.state = PlayState(player)

    def click_next(self, seconds=None):
        player.next()

    def click_previous(self, seconds=None):
        player.previous()

    def __str__(self):
        return 'Ready State'


class PlayState(IState):
    """ Конкретное состояние """
    def click_play(self):
        player.stop()
        player.state = ReadyState(player)

    def click_next(self, seconds=None):
        if seconds:
            player.forward(seconds)
        else:
            player.next()

    def click_previous(self, seconds=None):
        if seconds:
            player.rewind(seconds)
        else:
            player.previous()

    def __str__(self):
        return 'Play State'


class AudioPlayer(object):
    """ Класс контекста """
    def __init__(self):
        self._state = ReadyState(self)
        print(f'Initial state: {self._state}')

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        self._state = state
        print(f'Switch to {self._state}')

    # Методы UI
    def click_play(self):
        self._state.click_play()

    def click_next(self):
        self._state.click_next()

    def double_click_next(self):
        self._state.click_next(5)

    def click_previous(self):
        self._state.click_previous()

    def double_click_previous(self):
        self._state.click_previous(5)

    # Сервисные методы контекста, вызываются из состояний
    def play(self):
        print('Playing song')

    def stop(self):
        print('Stop song')

    def next(self):
        print('Next song')

    def previous(self):
        print('Previous song')

    def rewind(self, seconds):
        print(f'Rewind: {seconds} sec.')

    def forward(self, seconds):
        print(f'Fast forward: {seconds} sec.')


if __name__ == '__main__':
    player = AudioPlayer()

    player.click_next()
    player.click_play()
    player.double_click_next()
    player.click_play()
    player.click_previous()
    player.click_play()
    player.double_click_previous()
    player.click_play()
