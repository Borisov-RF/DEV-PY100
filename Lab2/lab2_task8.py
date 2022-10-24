money_capital = 10000
salary = 5000 # ежемесячная зарплата
spend = 6000 # расходы на проживание
increase = 0.05 # увеличение роста цен

month = 0  # количество месяцев, которое можно прожить

# TODO Оформить решение

while money_capital >= spend:
    money_capital = money_capital + salary - spend
    spend = spend * increase + spend
    month = month + 1



print(month)


