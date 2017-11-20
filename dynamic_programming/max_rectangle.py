class Solution:
    # @param A : list of list of integers
    # @return an integer
    def maximalRectangle(self, A):
        if len(A) == 0:
            return 0

        self.rect = A
        self.finals = [0]
        i = self.rectangle(0, 0, len(A) - 1, len(A[0]) - 1)
        return max(self.finals)

    def one_count(self, i,j,k,l):
        count = 0
        for r in xrange(i, k+1):
            for c in xrange(j, l+1):
                if self.rect[r][c] == 1:
                    count += 1
        return count

    def rectangle(self, i, j, k, l):
        if k < i or l < j:
            return 0

        arr_size = (k-i+1)*(l-j+1)
        # print 'array size:   ', arr_size

        if arr_size <= max(self.finals):
            return 0

        if arr_size == 1:
            if self.rect[i][j] == 1:
                self.finals.append(1)
                return 0
            else:
                return 0

        ones_count = self.one_count(i, j, k, l)
        # print 'ones counts:  ', ones_count
        if arr_size == self.one_count(i, j, k, l):
            self.finals.append(arr_size)
            return ones_count
        else:
            self.rectangle(i+1, j, k, l),
            self.rectangle(i, j+1, k, l)
            self.rectangle(i, j, k-1, l)
            self.rectangle(i, j, k, l-1)
        return 0


A = [[1]]
A = [[1, 1], [1, 0], [1, 1]]
print Solution().maximalRectangle(A)