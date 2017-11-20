""" inefficient approach """

# class Solution:
#     # @param A : list of list of integers
#     # @return an integer
#     def adjacent(self, A):
#         self.dp = [-1]*len(A[0])
#         a = self.get_max(0, A)
#         return a
#
#     def get_max(self, index, A):
#
#         if len(A[0]) == 0 and len(A[1]) == 0:
#             return 0
#         if len(A[0]) == 1 and len(A[1]) == 1:
#             return max(A[0][0], A[1][0])
#         if len(A[0]) == 2:
#             return max(max(A[0]), max(A[1]))
#
#         i = index
#         prev = 0
#         while i < len(A[0]):
#             rem_A = [A[0][i+2:], A[1][i+2:]]
#             print rem_A
#             if self.dp[i] != -1:
#                 nxt_max = self.dp[i]
#             else:
#                 self.dp[i] = self.get_max(i+2, rem_A)
#                 nxt_max = self.dp[i]
#             prev = max(prev, A[0][i] + nxt_max, A[1][i] + nxt_max)
#             print prev
#             i += 1
#         return prev


class Solution(object):

    def adjacent(self, A):
        self.A = [max(A[0][i], A[1][i]) for i in xrange(len(A[0]))]
        self.dp = [-1] * len(self.A)
        return max(self.max_sum(0, False), self.max_sum(0, True))

    def max_sum(self, i, include):
        if i == len(self.A):
            return 0

        if not include:
            return max(self.max_sum(i+1, False), self.max_sum(i+1, True))
        else:
            return self.max_sum(i+1, False) + self.A[i]


A = [[1, 2, 3, 4], [2, 3, 4, 5]]


A = [[74, 37, 82, 1], [66, 38, 16, 1]]


A = [[16, 5, 54, 55, 36, 82, 61, 77, 66, 61], [31, 30, 36, 70, 9, 37, 1, 11, 68, 14]]

print Solution().adjacent(A)