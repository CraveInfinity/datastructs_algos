class Solution:
    # @param arr : list of integers
    # @return a list of integers
    def prevSmaller(self, arr):

        i = 1
        stack = [-1]

        while i < len(arr):
            j = i - 1

            stack.append(-1)

            while j >= 0:
                if arr[i] > arr[j]:
                    stack.pop()
                    stack.append(arr[j])

                    break
                j -= 1

            i += 1

        return stack


A= [ 34, 35, 27, 42, 5, 28, 39, 20, 28 ]
A = [2, 4]
A = [1, 1]

A = []
A = [1]
print Solution().prevSmaller(A)