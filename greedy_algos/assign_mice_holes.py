class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def mice(self, A, B):
        A.sort()
        B.sort()


        # l_dist = abs(A[0] - B[0])
        #
        # r_dist = abs(A[-1] - B[-1])
        #
        # if l_dist > r_dist:
        #     return l_dist
        # else:
        #     return r_dist

        i = 0
        r = None
        while i < len(A):
            x = abs(A[i] - B[i])
            if i == 0:
                r = x
            else:
                if r < x:
                    r = x

            i += 1

        return r





A = [4, -4, 2]
B = [4, 0, 5]

A = [ -49, 58, 72, -78, 9, 65, -42, -3 ]
B = [ 30, -13, -70, 58, -34, 79, -36, 27 ]

print Solution().mice(A, B)