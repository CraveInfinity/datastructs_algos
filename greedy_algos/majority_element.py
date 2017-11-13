class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        majority = len(A) / 2

        d = {}

        for i in A:
            d.setdefault(i, 0)
            d[i] += 1

            if d[i] > majority:
                return i



A = [2, 1, 2]
print Solution().majorityElement(A)