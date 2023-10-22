money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

count_month = 0
budjet = money_capital + salary

while budjet > spend:
    budjet -= spend
    count_month += 1
    spend = spend + spend * increase
    budjet += salary

print("Количество месяцев, которое можно протянуть без долгов:", count_month)
