import pandas as pd
df = pd.read_excel('население_и_площадь.xlsx')

price_rent = 5000
price_tarifs = 110
def count_profit(people, square, price_rent, price_tarifs):
    return (price_tarifs*people*1000 - price_rent*square)

d = {}
negative_profit = {}
city_with_worst_profit = city_with_best_profit = df.iloc[0, 0]
worst_profit = best_profit = count_profit(df.iloc[0, 1], df.iloc[0, 2], price_rent, price_tarifs)
d[city_with_best_profit] = best_profit

for i in range(1, df.shape[0]):
    profit = count_profit(df.iloc[i, 1], df.iloc[i, 2], price_rent, price_tarifs)
    d[df.iloc[i, 0]] = profit
    if profit >= 0:
        if profit < worst_profit:
            worst_profit = profit
            city_with_worst_profit = df.iloc[i, 0]
        if profit > best_profit:
            best_profit = profit
            city_with_best_profit = df.iloc[i, 0]
    else:
        negative_profit[df.iloc[i, 0]] = profit
print(f'Worst profit = {worst_profit} in {city_with_worst_profit}')
print(f'Negative profit = {negative_profit}')
print(f'Best profit = {best_profit} in {city_with_best_profit}')
print(dict(sorted(d.items(), key = lambda x: -x[1])))