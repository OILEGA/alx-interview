#!/usr/bin/python3

"""Determines the fewest number of coins needed to meet a given
   amount total when given a pile of coins of different values.
"""

def makeChange(coins: list, total:int) -> int:
    sorted_coins = sorted(coins, reverse=True)
    used_coins = 0
    for coin in sorted_coins:
        if total == 0:  
            break
        used_coins += total // coin
        total = total % coin
        if total == 0:
            return used_coins
        return - 1

print(makeChange([1,2,25], 37))
print(makeChange([1256, 54, 48, 16, 102], 1453))  
