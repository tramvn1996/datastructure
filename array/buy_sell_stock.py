#buy and sell stock once
#determine when to buy and sell would yield the largest profit
def buy_and_sell_stock(prices):
    min_price_sf, max_profit = float('inf'), 0.0
    for price in prices:
        max_profit_sell_today = price - min_price_sf
        max_profit = max (max_profit, max_profit_sell_today)
        min_price_sf = min(price, min_price_sf)
    return max_profit

A = [310, 315, 260, 290, 240, 255]
print(buy_and_sell_stock(A))
