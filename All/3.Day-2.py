meal_cost = float(input())

tip_percent = int(input())

tax_percent = int(input())

totalCost = meal_cost + (meal_cost*(tip_percent/100)) + (meal_cost*(tax_percent/100))

print(round(totalCost))