"""
File: best_time_to_buy_sell_stock.py
Author: Somnath
Date: 17/08/26
Description: 121. Best Time to Buy and Sell Stock
"""


def best_time_to_buy_sell_stock(prices):
    min_price = float('inf')
    max_profit = 0
    size = len(prices)

    for i in range(size):
        min_price = min(min_price, prices[i])
        max_profit = max(max_profit, prices[i] - min_price)
    return max_profit

if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    result = best_time_to_buy_sell_stock(prices)
    print("Result is:", result)
