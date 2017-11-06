class Solution:
    # # @param A : tuple of integers
    # # @param B : integer
    # # @return an integer
    def diffPossible(self, A, B):
        if len(A) <= 1:
            return 0

        G = dict()

        for i, k in enumerate(A):
            G[k] += 1

        i = 0
        while i < len(A):
            if (A[i] - B) in [k for idx, k in enumerate(A) if not idx == i]:
                return 1
            i += 1

        return 0

A = [1, 3, 5]
B = 2
print Solution().diffPossible(A, B)