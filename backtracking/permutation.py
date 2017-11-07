class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):

        self.A = A
        self.final = []

        self.xpermute([], A)
        return self.final

    def xpermute(self, res, m):

        if len(res) == len(self.A):
            self.final.append(res)
            return

        i = 0
        while i < len(m):
            tres = res + [m[i]]
            # print tres
            l = [m[k] for k in xrange(len(m)) if not k == i]
            self.xpermute(tres, l)
            i += 1



print Solution().permute([1, 2, 3, 4])