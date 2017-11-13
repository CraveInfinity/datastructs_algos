class Solution:
    # @param A : list of integers
    # @return an integer
    def maxp3(self, A):
        def product(j):
            return reduce(lambda x, y: x * y, j)

        A.sort()
        i = 3
        j = [A[0], A[1], A[2]]

        p = product(j)
        replace = None

        while i < len(A):
            print j
            print A[i]
            l = 0
            z = []
            while l < len(j):
                temp = [k for k in j]

                temp[l] = A[i]
                print temp
                t = product(temp)

                if p < t:
                    replace = l

                l += 1

            if replace:
                j[replace] = A[i]

            i += 1

        return product(j)

A = [0, -1, 3, 100, 70, 50]

print Solution().maxp3(A)