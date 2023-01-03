#  Реализовать проект расчёта суммарного расхода ткани на производство одежды.
#  Основная сущность (класс) этого проекта — одежда, которая может иметь
#  определённое название. К типам одежды в этом проекте относятся пальто и костюм.
#  У этих типов одежды существуют параметры: размер (для пальто) и рост
#  (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
#  для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих
#  методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на
#  этом уроке знания: реализовать абстрактные классы для основных классов
#  проекта, проверить на практике работу декоратора @property.

class Clothes:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def get_square_coat(self):
        return self.width / 6.5 + 0.5
    def get_square_costume(self):
        return self.height * 2 + 0.3
    @property
    def get_square_full(self):
        return str(f'Общий расход ткани \n' 
        f' {(self.width / 6.5 + 0.5) + (self.height * 2 + 0.3)}')
class Coat(Clothes):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_coat = round(self.width / 6.5 + 0.5)
    def __str__(self):
        return f'расход ткани для пальто {self.square_coat}'

class Costume(Clothes):
     def __init__(self, width, height):
        super().__init__(width, height)
        self.square_costume = round(self.height * 2 + 0.3)


     def __str__(self):
        return f'расход ткани для костюма {self.square_costume}'

coat = Coat(2, 3)
costume = Costume(3, 4)
print(coat)
print(costume)
print(coat.get_square_full)
print(costume.get_square_full)
print(costume.get_square_coat())
print(costume.get_square_costume())