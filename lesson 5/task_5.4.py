#Создать (не программно) текстовый файл со следующим содержимым:
#One — 1
#Two — 2
#Three — 3
#Four — 4
#Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок
# строк должен записываться в новый текстовый файл.

dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('file_1.txt', encoding='utf=8') as a_obj:
    for line in a_obj:
        for key in dict.keys():
            line = line.replace(key, dict[key])
        print(line)
        with open('file_2.txt', 'a',) as a_rus:
            a_rus.write(f'\n {line}')