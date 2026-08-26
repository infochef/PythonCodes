"""
File: best_time_to_buy_sell_stock_III.py
Author: Somnath
Date: 24/08/26
Description: 123. Best Time to Buy and Sell Stock III
"""


def best_time_to_buy_sell_stock_III(prices):
    buy_price1 = float('inf')
    profit1 = 0
    buy_price2 = float('inf')
    profit2 = 0

    for price in prices:
        buy_price1 = min(buy_price1, price)
        profit1 = max(profit1, price - buy_price1)

        buy_price2 = min(buy_price2, price - profit1)
        profit2 = max(profit2, price - buy_price2)
    return profit2



if __name__ == '__main__':
    prices = [3,3,5,0,0,3,1,4]
    result = best_time_to_buy_sell_stock_III(prices)
    print("Result is:", result)
