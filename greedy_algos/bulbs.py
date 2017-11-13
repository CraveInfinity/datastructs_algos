class Solution:
    # @param A : list of integers
    # @return an integer
    def bulbs(self, A):
        A = [bool(x) for x in A]

        i = 0
        count = 0
        n = 1
        while i < len(A):
            if A[i] == n:
                pass
            else:
                count += 1
                if A[i] == 1:
                    n = 1
                else:
                    n = 0
            i += 1

        return count





A = [0, 1, 0, 1]
print Solution().bulbs(A)