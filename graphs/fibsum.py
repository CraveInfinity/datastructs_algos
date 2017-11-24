class Solution:
    # @param A : integer
    # @return an integer
    def __init__(self):
        self.max_fib = None
        self.res = None

    def fibsum(self, number):
        self.max_fib = number
        fib_series = self.fibseries()
        # print fib_series
        return self.greedy_fib([s for s in fib_series if s <= number], number)

    def greedy_fib(self, series, number):
        if number == 0:
            return 0
        if len(series) == 0:
            return 0

        x = number - series[-1]
        return self.greedy_fib([s for s in series if s <= x], x) + 1

    def fibseries(self):
        res = [1, 1]
        n = True
        while n:
            res.append(res[-1] + res[-2])
            if res[-1] >= self.max_fib:
                n = False

        return res


print Solution().fibsum(1)
