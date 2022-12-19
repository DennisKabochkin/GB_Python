#6. Реализовать функцию int_func(), принимающую слова из маленьких латинских
# букв и возвращающую их же, но с прописной первой буквой. Например,
# print(int_func(‘text’)) -> Text.

def int_func(string):
    return string.title()

print(int_func("text"))


def int_func (*args):
    word = input("Input word: ")
    print(word.title())
    return
int_func()