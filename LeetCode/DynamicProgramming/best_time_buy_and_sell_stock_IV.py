"""
File: best_time_buy_and_sell_stock_IV.py
Author: Somnath
Date: 25/08/26
Description: 188. Best Time to Buy and Sell Stock IV
"""


def best_time_buy_and_sell_stock_IV(prices, k):
    buy = [float('-inf')] * (k + 1)
    profit = [0] * (k + 1)

    for price in prices:
        for transaction in range(1, k + 1):
            buy[transaction] = max(
                buy[transaction],
                profit[transaction - 1] - price
            )

            profit[transaction] = max(
                profit[transaction],
                buy[transaction] + price
            )

    return profit[k]


if __name__ == '__main__':
    prices = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0]
    k = 4
    result = best_time_buy_and_sell_stock_IV(prices, k)
    print("Result is:", result)
