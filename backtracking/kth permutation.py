class Solution:
    # @param n : integer
    # @param k : integer
    # @return a strings

    def do_factorial_search(self, k):
        i = 1
        n = 1
        while True:
            n *= i
            if n >= k:
                return i

            i += 1

    def getPermutation(self, n, k):

        self.count = 0

        m = self.do_factorial_search(k)
        lm = n - m

        if lm:
            init = ''.join([str(x) for x in xrange(1, lm + 1)])
        else:
            init = ''

        self.k = k
        A = list(xrange(1, n + 1))[lm:]
        self.A = A

        self.xpermute([], A)
        z = ''.join([str(e) for e in self.hero])
        return init + z

    def xpermute(self, res, m):

        if len(res) == len(self.A):
            self.count += 1
            if self.count == self.k:
                self.hero = res
            return

        i = 0
        while i < len(m):
            if self.count == self.k:
                break
            tres = res + [m[i]]
            l = [m[k] for k in xrange(len(m)) if not k == i]
            self.xpermute(tres, l)
            i += 1