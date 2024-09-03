class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        res = [price, 1]
        while self.stack and price >= self.stack[-1][0]:
            prev_price = self.stack.pop()
            res[1] += prev_price[1]
        self.stack.append(res)
        return res[1]
