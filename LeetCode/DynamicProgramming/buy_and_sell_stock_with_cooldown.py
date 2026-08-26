"""
File: buy_and_sell_stock_with_cooldown.py
Author: Somnath
Date: 25/08/26
Description: 309. Best Time to Buy and Sell Stock with Cooldown
"""


def buy_and_sell_stock_with_cooldown(prices):
    dp = {}
    def dfs(i, buying):
        if i >= len(prices):
            return 0
        if (i, buying) in dp:
            return dp[(i, buying)]
        cooldown = dfs(i+1, buying)
        if buying:
            buy = dfs(i + 1, not buying) - prices[i]
            dp[(i, buying)] = max(buy, cooldown)
        else:
            sell = dfs(i+2, not buying) + prices[i]
            dp[(i, buying)] = max(sell, cooldown)
        return dp[(i, buying)]
    return dfs(0, True)

if __name__ == '__main__':
    prices = [1, 2, 3, 0, 2]
    result = buy_and_sell_stock_with_cooldown(prices)
    print("Result is:", result)
