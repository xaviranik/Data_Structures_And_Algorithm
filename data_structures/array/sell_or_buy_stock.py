def sell_or_buy(prices):
    if len(prices) < 2:
        return 0

    min_price = prices[0]
    max_profit = 0

    for price in prices:
        min_price = min(min_price, price)
    compare_profit = price - min_price
    max_profit = max(max_profit, compare_profit)
    return max_profit


prices = [252, 265, 252, 220, 221, 256, 247]
print(sell_or_buy(prices))
