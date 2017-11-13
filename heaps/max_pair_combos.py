class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):

        l = len(A)

        res = []

        A = sorted(A, reverse=True)
        B = sorted(B, reverse=True)

        print A
        print B


        for a in A:
            res.append(B[0] + a)
        for i, b in enumerate(B):
            if i > 0:
                res.append(A[0] + b)

        return sorted(res, reverse=True)[:l]



A = [ 3, 1, 3, 1 ]
B = [ 1, 4, 1, 4 ]

print Solution().solve(A, B)