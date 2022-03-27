# Your code below:
toppings = ["pepperoni","pinapple","cheese","sausage","olives","anchovies","mushrooms"]
price = [2, 6, 1, 3, 2, 7, 2]
num_two_dollar_slices = price.count(2)
num_pizzas = len(toppings)
print(f"We sell {num_pizzas} different kinds of pizza!")
pizza_and_prices = [[2, "pepperoni"], [6, "pinapple"],[1, "cheese"],[3, "sausage"],[2, "olives"], [7,"anchovies"],[2,"mushrooms"]]
print(pizza_and_prices)

# Sorting and slicing pizzas
increasing_price = sorted(pizza_and_prices)
# print(increasing_price)
cheapest_pizza = increasing_price[0]
priciest_pizza = increasing_price[-1]
last_pizza_expensive = increasing_price.pop(-1)
# print(increasing_price)
increasing_price.insert(3, [2.5, "peppers"])
# print(increasing_price)
three_cheapest = increasing_price[:3]
print(three_cheapest)