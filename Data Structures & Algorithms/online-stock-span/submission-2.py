class StockSpanner:

    def __init__(self):
        self.stock = []

    def next(self, price: int) -> int:
        curr_span = 1
        while self.stock and self.stock[-1][0] <= price:
            curr_span += self.stock[-1][1]
            self.stock.pop()
        self.stock.append([price, curr_span])
        return curr_span


"""
    1. make a monotonic stack of pair [stock, span]
    2. for each element, check the top of the stack
         to maintain its relative order, if the top of the stack is <=
         an element, add its span to curr span, pop and check next
        until an element >= or not stack
    3. append element and span pair to stack
    4. return span
"""
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)