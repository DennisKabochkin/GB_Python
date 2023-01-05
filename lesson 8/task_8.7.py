# Реализовать проект «Операции с комплексными числами». Создайте класс
# «Комплексное число». Реализуйте перегрузку методов сложения и умножения
# комплексных чисел. Проверьте работу проекта. Для этого создаёте экземпляры
# класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.z = 'a + bi'
    def __add__(self, other):
        #print(f'Сумма комплексных чисел z1+z2: ')
        return f' {self.a + other.a} {self.b + other.b}i'
    def __mul__(self, other):
        #print(f'Произведение комплексных чисел z1*z2: ')
        return f' {(self.a * other.a) - (self.b * other.b)} {self.a * other.b + self.b * other.a}i'
    def __str__(self):
        return f': {self.a} + {self.b}i'

z1 = ComplexNumber(-9, -7)
z2 = ComplexNumber(-1, 1)
print(f'Первое комплексное число z1', z1)
print(f'Второе комплексное число z2', z2)
print(f'Сумма комплексных чисел z1+z2=', z1 + z2)
print(f'Произведение комплексных чисел z1*z2=', z1 * z2)


