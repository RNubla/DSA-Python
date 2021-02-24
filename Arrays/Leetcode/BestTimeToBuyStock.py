from typing import List
import sys


def maxProfit(prices: List[int]):
    minPrice = sys.maxsize
    result = 0
    for x in range(len(prices)):
        if prices[x] < minPrice:
            minPrice = prices[x]
        elif (prices[x] - minPrice) > result:
            result = prices[x] - minPrice
    return result


if __name__ == '__main__':
    s1 = [7, 1, 5, 3, 6, 4]
    # s1 = [7, 6, 4, 3, 1]
    # s1 = [2, 4, 1]

    print(maxProfit(s1))
