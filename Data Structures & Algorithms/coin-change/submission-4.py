class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        n = len(coins)
        INF = 10**9
        prev = [0]*(amount+1)
        curr = [0]*(amount+1)

        for T in range(amount+1):
            if T%coins[0] == 0:
                prev[T] = T//coins[0]
            else:
                prev[T] = INF
            
        for i in range(1,n):
            for T in range(amount+1):
                not_take = prev[T]
                take = INF

                if coins[i] <= T:
                    take = 1 + curr[T-coins[i]]
                curr[T] = min(take,not_take)
            prev = curr.copy()
        return prev[amount] if prev[amount] != INF else -1
                
        
        
