salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.05  # Ежемесячный рост цен

money_capital = 0
current_spend = spend

for _ in range(months):
    deficit = current_spend - salary
    if deficit > 0:
        money_capital += deficit
    current_spend *= (1 + increase)

money_capital = round(money_capital)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)