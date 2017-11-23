class Solution:
    # @param A : integer
    # @return an integer
    def __init__(self):
        self.max_fib = None
        self.res = None
        self.final = dict()
        self.final[1000000] = []

    def fibsum(self, number):
        self.max_fib = number
        fib_series = self.fibseries()
        # print fib_series
        self.fib_sum(fib_series, number, [])

        # print self.final

        return min(self.final)

    def fib_sum(self, fib_series, number, g):
        # print g
        if sum(g) == self.max_fib:
            self.final[len(g)] = g
            return

        if len(fib_series) == 0:
            return

        if number <= 0:
            return

        for x in fib_series[::-1]:
            if x == number:
                g.append(x)
                self.final[len(g)] = g
                return
            else:
                if len(g)+1 < min(self.final):
                    self.fib_sum([fx for fx in fib_series if fx <= number-x], number-x, g+[x])
                else:
                    return

    def fibseries(self):
        res = [1, 1]
        n = True
        while n:
            res.append(res[-1] + res[-2])
            if res[-1] >= self.max_fib:
                n = False

        return res


print Solution().fibsum(1000)
