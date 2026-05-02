from typing import List

class Solution:
    @staticmethod
    def maximumProfit(prices: List[int], k: int) -> int:
        NEG = float("-inf")
        # initialzie free, long, and short array
        free = [0] + [NEG] * k
        long = [NEG] * (k + 1)
        short = [NEG] * (k + 1)
        print(f'original free: {free}')
        print(f'original long: {long}')
        print(f'original short: {short}')
        for price in prices:
            new_free = free[:]
            new_long = long[:]
            new_short = short[:]

            for t in range(k + 1):
                # start normal buy, replace the long transaction with the max profit
                new_long[t] = max(new_long[t], free[t] - price)

                # start short sell, replace the short transaction with the max profit 
                new_short[t] = max(new_short[t], free[t] + price)

                if t < k:
                    # finish normal transaction
                    new_free[t + 1] = max(new_free[t + 1], long[t] + price)

                    # finish short transaction
                    new_free[t + 1] = max(new_free[t + 1], short[t] - price)
            print(f'free: {free}')
            print(f'long: {long}')
            print(f'short: {short}')
            free, long, short = new_free, new_long, new_short

        return max(free)

if __name__ == "__main__":
    import math
    import random  
    prices = [random.randint(1, 10000) for _ in range(1000)]
    Solution.maximumProfit(prices=prices, k=3)