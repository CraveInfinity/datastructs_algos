class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):

        if A:
            max_profit = 0

            present_val = A[0]

            i = 1
            while i < len(A):
                if A[i] > present_val:
                    max_profit += A[i] - present_val
                    present_val = A[i]
                else:
                    present_val = A[i]

                i += 1

            return max_profit
        else:
            return 0


A = [1, 2, 3, 6]

print Solution().maxProfit(A)


