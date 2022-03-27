hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]
total_price  = 0

for price in prices:
    total_price += price

average_price = total_price / len(prices)
print("Average Haircut Price: ", average_price)
new_price = [price - 5 for price in prices]
print(new_price)
# Revenue
total_revenue = 0
for j in range(len(hairstyles)):
    total_revenue += prices[j] * last_week[j]
print("Total Revenue: ", total_revenue)
average_daily_revenue = total_revenue / 7
# Cuts UNDER 30
cuts_under_30 = [hairstyles[i]for i in range(len(new_price)-1) if new_price[i] < 30]
print(cuts_under_30)
