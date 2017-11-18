class Solution:
    # @param A : list of list of integers
    # @return an integer

    def __init__(self):
        self.arr = None

    def uniquePathsWithObstacles(self, A):
        self.m = len(A)-1
        self.n = len(A[0])-1
        self.arr = [[-10] * (self.n+1)] * (self.m+1)
        self.A = A

        val = self.path(0, 0)
        print self.arr

        return val

    def path(self, x, y):

        if x == self.m and y == self.n:
            return 1

        if x >= self.m or y >= self.n:
            return 0

        if x == self.m-1 and y == self.n-1:
            return 1

        if self.A[x][y] == 1:
            self.arr[x][y] = 0
            return 0

        if self.arr[x][y] != -10:
            return self.arr[x][y]

        self.arr[x][y] = self.path(x + 1, y) + self.path(x, y + 1)

        return self.arr[x][y]


A = [
  [0, 0, 0],
  [0, 0, 0]
]

print Solution().uniquePathsWithObstacles(A)