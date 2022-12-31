#Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.

count_lines = 0
count_words = 0

with open('У лукоморья дуб зелёный (отрывок из поэмы «Руслан и Людмила»).txt',
          'r', encoding='utf-8') as obj:
    for line in obj:
        print(line.replace('\n', ''))
        for n in line:
            if n == ' ':
                count_words += 1
        count_lines += 1
        print(f'Количество слов в строке {count_lines} = {count_words} \n')
        count_words = 1
    print(f'В тексте {count_lines} строк(и)')