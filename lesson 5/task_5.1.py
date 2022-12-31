#Создать программный файл в текстовом формате, записать в него построчно
# данные, вводимые пользователем. Об окончании ввода данных будет
# свидетельствовать пустая строка.


obj = open('file.txt', 'w', encoding='utf-8')
lines = []
while True:
    line = input('Введите текст или "Enter" для завершения: ')
    if line != '':
        lines.append(line + '\n')
    else:
        break
obj.writelines(lines)

with open('file.txt', 'r', encoding='utf=8') as obj:
    for line in obj:
       print(line)