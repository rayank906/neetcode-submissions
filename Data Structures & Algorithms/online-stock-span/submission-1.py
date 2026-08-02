class StockSpanner:
    stock = []

    def __init__(self):
        self.stock = []

    def next(self, price: int) -> int:
        self.stock.append(price)
        count = 0
        for i in range(len(self.stock) - 1, -1, -1):
            if self.stock[i] <= price:
                count += 1
            else:
                return count
        return count
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)