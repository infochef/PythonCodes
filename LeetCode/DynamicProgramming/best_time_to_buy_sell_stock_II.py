"""
File: best_time_to_buy_sell_stock_II.py
Author: Somnath
Date: 24/08/26
Description: 122. Best Time to Buy and Sell Stock II
"""


def best_time_to_buy_sell_stock_II(prices):
    profit = 0
    for i in range(len(prices) - 1):
        if prices[i] < prices[i + 1]:
            profitgain = prices[i + 1] - prices[i]
            profit += profitgain
    return profit


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    result = best_time_to_buy_sell_stock_II(prices)
    print("Result is:", result)
