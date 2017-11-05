class Solution:
    # @param A : string
    # @param B : integer
    # @return a strings
    def convert(self, A, B):

        if len(A) == 0:
            return ''
        if B <= 0:
            return A


        i = 0

        asc = True

        k = {i: '' for i in xrange(B)}
        k[0] += A[0]
        i += 1

        while i < len(A):

            if asc:
                j = 1
                while j < B and i < len(A):
                    k[j] += A[i]
                    j += 1
                    i += 1
            else:
                j = B-2
                while j >= 0 and i < len(A):
                    k[j] += A[i]
                    j -= 1
                    i += 1

            asc = not asc

        return reduce(lambda x,y : x+y, k.values())


print Solution().convert('PAYPALISHIRING', 3)


