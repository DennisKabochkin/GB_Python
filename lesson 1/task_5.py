# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма.
# Например, прибыль — выручка больше издержек,
# или убыток — издержки больше выручки. Выведите соответствующее сообщение.
# 6. Если фирма отработала с прибылью, вычислите рентабельность выручки.
# Это отношение прибыли к выручке.
# Далее запросите численность сотрудников фирмы и определите прибыль
# фирмы в расчёте на одного сотрудника.
profit = int(input("Введите выручку фирмы: "))
costs = int(input("Введите издержки фирмы: "))
number = int(input("Введите численность сотрудников фирмы: "))
val = profit - costs
if val > 0:
    ren = val / profit
    val_number = val / number
    print(f"Финансовый результат работы фирмы - прибыль: {val}")
    print(f"Вычисление рентабельности выручки, (отношение прибыли к выручке): {ren}")
    print(f"Прибыль фирмы в расчёте на одного сотрудника: {val_number}")
elif val < 0:
    print(f"Финансовый результат работы фирмы - убыток: {val}")
else:
    print("Выручка равна издержкам")