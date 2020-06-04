# Главное:
#    Паттерн Composite позволяет сгруппировать множество объектов в древовидную структуру, а затем работать с ней так,
#    как будто это единичный объект.
# Применение:
#    1. Когда нужно представить древовидную структуру объектов.
#    2. Когда клиенты должны единообразно трактовать простые и составные объекты.
# Реализация:
#    0. Определить возможность представления бизнес-логики как древовидной структуры. Разбить её на простые компоненты
#    и контейнеры. Контейнеры могут содержать как простые компоненты, так и другие вложенные контейнеры.
#    1. Создать общий интерфейс компонентов, который объединит операции контейнеров и простых компонентов дерева.
#    Интерфейс будет удачным, если можно использовать его, чтобы взаимозаменять простые и составные компоненты без
#    потери смысла.
#    2. Создать класс компонентов-листьев, не имеющих дальнейших ответвлений. Программа может содержать несколько таких
#    классов.
#    3. Создать класс компонентов-контейнеров и добавить в него массив для хранения ссылок на вложенные компоненты.
#    Этот массив должен быть способен содержать как простые, так и составные компоненты.
#    4. Реализовать в контейнере методы интерфейса компонентов, контейнеры должны делегировать основную работу своим
#    дочерним компонентам.
#    5. Добавить операции добавления и удаления дочерних компонентов в класс контейнеров. Методы добавления/удаления
#    дочерних компонентов можно поместить и в интерфейс компонентов. Да, это нарушит принцип разделения интерфейса,
#    так как реализации методов будут пустыми в компонентах-листьях. Но зато все компоненты дерева станут действительно
#    одинаковыми для клиента.


from abc import ABCMeta, abstractmethod


class IShape(metaclass=ABCMeta):
    """ Общий интерфейс компонентов """
    @abstractmethod
    def draw(self):
        pass


class Rectangle(IShape):
    """ Класс компонента-'листа' """
    def __init__(self, n, x, y, h, w):
        self.num = n
        self.x = x
        self.y = y
        self.height = h
        self.width = w

    def draw(self):
        """ Основная бизнес-логика компонента-'листа' """
        print(f'Draw rectangle {self.num} in point ({self.x}, {self.y}) with '
              f'height {self.height} and width {self.width}')

    def __str__(self):
        return f'Rectangle {self.num}'


class Circle(IShape):
    """ Класс компонента-'листа' """
    def __init__(self, n, x, y, r):
        self.num = n
        self.x = x
        self.y = y
        self.radius = r

    def draw(self):
        """ Основная бизнес-логика компонента-'листа' """
        print(f'Draw circle {self.num} in point ({self.x}, {self.y}) with radius {self.radius}')

    def __str__(self):
        return f'Circle {self.num}'


class ShapeCompound(IShape):
    """ Класс компонента-'контейнера' """
    def __init__(self, n):
        self.num = n
        self._shapes = []

    def add(self, *args):
        """ Добавление дочернего компонента """
        for shape in args:
            self._shapes.append(shape)
            print(f'{shape} added to compound {self.num}')

    def remove(self, shape):
        """ Удаление дочернего компонента """
        if shape in self._shapes:
            self._shapes.remove(shape)
            print(f'{shape} removed from compound {self.num}')
        else:
            print(f'Can\'t find {shape} in compound {self.num}')

    def draw(self):
        """ Класс-'контейнер' делегирует выполнение бизнес-логики дочерним компонентам """
        for shape in self._shapes:
            shape.draw()

    def __str__(self):
        return f'Compound {self.num} with shapes'


if __name__ == '__main__':
    circle1 = Circle(1, 50, 70, 10)
    circle2 = Circle(2, 100, 50, 20)
    circle3 = Circle(3, 25, 100, 15)

    rectangle1 = Rectangle(1, 15, 30, 15, 35)
    rectangle2 = Rectangle(2, 70, 55, 50, 25)

    compound1 = ShapeCompound(1)
    compound1.add(circle1, rectangle1, rectangle2)
    compound1.remove(rectangle2)

    compound2 = ShapeCompound(2)
    compound2.add(circle2, rectangle2)
    compound2.remove(circle3)

    draw_manager = ShapeCompound(3)
    draw_manager.add(compound1, compound2, circle3)
    print('\nDrawing...')
    draw_manager.draw()
