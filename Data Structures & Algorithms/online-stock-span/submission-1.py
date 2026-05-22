class StockSpanner:

    def __init__(self):
        self.stack = [] # pair: [price,span]
        
    
    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1] <= price:
            span+=1
            self.stack.pop()
        
        self.stack.append(price)
        return span



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)