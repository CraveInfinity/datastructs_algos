class Solution:
    # @param A : string
    # @return an integer
    def atoi(self, A):
        A = list(A.strip())

        if not (ord('0') <= ord(A[0]) <= ord('9') or ord(A[0]) == 45 or ord(A[0]) == 43):
            return 0

        i = 0

        if ord(A[0]) == 45:
            i += 1
        elif ord(A[0]) == 43:
            i += 1

        while i < len(A):
            if ord('0') <= ord(A[i]) <= ord('9'):
                pass
            else:
                break

            i += 1

        if ord(A[0]) == 45:
            x = ''.join(A[1:i])
            if x:
                x = -1*int(x)
            else:
                return 0
        elif ord(A[0]) == 43:
            x = ''.join(A[1:i])
            if x:
                x = int(x)
            else:
                return 0
        else:
            x = ''.join(A[:i])
            if x:
                x = int(x)
            else:
                return 0

        if x > 2147483647:
            return 2147483647
        elif x < -2147483648:
            return -2147483648
        else:
            return x


A = "+555555555555555555555555555555555555555555555 0 T7165 0128862 089 39 5"
print Solution().atoi(A)
