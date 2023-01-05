# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем. При вводе нуля в
# качестве делителя программа должна корректно обработать эту ситуацию и не
# завершиться с ошибкой.

class DivisionByZero:
    def __init__(self, numerator, denominator):
        self.numenator = numerator
        self.denominator = denominator
    @staticmethod
    def divide_by_zero(numerator, denominator):
        try:
            return (numerator / denominator)
        except:
            return (f'Делить на ноль нельзя')

print(DivisionByZero.divide_by_zero(10, 0))
print(DivisionByZero.divide_by_zero(10, 0.1))
division = DivisionByZero(0, 1)
print(division.divide_by_zero(0, 100))