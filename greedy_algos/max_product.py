class Solution:
    # @param A : list of integers
    # @return an integer
    def maxp3(self, A):
        def product(j):
            return reduce(lambda x, y: x * y, j)

        A.sort()
        max_pos = A[-3:]
        pos_val = reduce(lambda x,y: x*y, max_pos)

        # print A

        if A[0] < 0 and A[1] < 0:
            max_abs = A[0] * A[1]
        else:
            max_abs = 0


        if max_abs:
            final = max_abs*max_pos[-1]

            if final > pos_val:
                return final
            else:
                return pos_val
        else:
            return pos_val

A = [0, -1, 3, 100, 70, 50]
A = [ 1, 3, 5, 2, 8, 0, -1, -3 ]


print Solution().maxp3(A)