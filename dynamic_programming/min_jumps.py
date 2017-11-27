class Solution:
    # @param A : list of integers
    # @return an integer

    def __init__(self):
        self.dp = None

    def jump(self, A):
        self.dp = [-1] * len(A)

        l = self.jumps(A, 0, 0)

        if l == 10000000000000001:
            return -1
        else:
            return l

    def jumps(self, A, steps, index):

        min_steps = 100000000000
        current_val = A[0]
        if len(A) == 1:
            self.dp[index] = steps
            return self.dp[index]

        if current_val == 0:
            self.dp[index] = 10000000000000001
            return self.dp[index]

        if current_val >= len(A)-1:
            self.dp[index] = steps + 1
            return self.dp[index]

        else:
            for i in xrange(1, current_val+1):
                if not self.dp[index+i] == -1:
                    next_steps = self.dp[index+i]
                else:
                    next_steps = self.jumps(A[i:], steps, index+i)

                min_steps = min(min_steps, next_steps+1)

            self.dp[index] = min_steps
            return self.dp[index]


# A = [2, 0, 1, 1, 4]
A = [ 33, 21, 50, 0, 0, 46, 34, 3, 0, 12, 33, 0, 31, 37, 15, 17, 34, 18, 0, 4, 12, 41, 18, 35, 37, 34, 0, 47, 0, 39, 32, 49, 5, 41, 46, 26, 0, 2, 49, 35, 4, 19, 2, 27, 23, 49, 19, 38, 0, 33, 47, 1, 21, 36, 18, 33, 0, 1, 0, 39, 0, 22, 0, 9, 36, 45, 31, 4, 14, 48, 2, 33, 0, 39, 0, 37, 48, 44, 0, 11, 24, 16, 10, 23, 22, 41, 32, 14, 22, 16, 23, 38, 42, 16, 15, 0, 39, 23, 0, 42, 15, 25, 0, 41, 2, 48, 28 ]

print Solution().jump(A)




