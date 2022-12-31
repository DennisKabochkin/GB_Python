#Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделённых пробелами. Программа должна подсчитывать сумму чисел в файле и
# выводить её на экран.

def summary():
    try:
        with open('task_5.5.1.txt', 'w', encoding='utf=8') as file:
            line = input('Введите числа через пробел: ')
            file.writelines(line)
            number = line.split()
            print(sum(map(int, number)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Не правильно введены числа!')
summary()