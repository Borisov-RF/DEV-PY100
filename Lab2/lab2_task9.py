salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

# TODO Оформить решение

summ_ = spend

for i in range(2, months + 1):
    spend = spend * 1.03
    summ_ = summ_ + spend

print(round((summ_ - salary * months)))