# 2. Выполнить функцию, которая принимает несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры как
# именованные аргументы. Осуществить вывод данных о пользователе одной строкой.


def my_func(name, surname, year, city, email, telephone):
    return ' '.join([name, surname, year, city, email, telephone])


print(my_func(surname='Кабочкин', name='Денис', year='1983',
              city='Гомель', email='denis@kabochkin.by',
              telephone='+375291111111'))
