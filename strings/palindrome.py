class Solution:
    # @param A : string
    # @return a strings
    def longestPalindrome(self, A):
        i = 0
        m = ''

        x2 = ''
        x = ''
        while i < len(A):
            j = 0
            while j <= i:
                if i-j >= 0 and i + j < len(A):
                    x = A[(i - j):(i + j)+1]

                if i-j >= 0 and i + 1 + j < len(A):
                    x2 = A[(i - j):(i + j)+2]

                # print x
                # print x[::-1]

                if x == x[::-1]:
                    if len(x) > len(m):
                        m = x

                if x2 == x2[::-1]:
                    if len(x2) > len(m):
                        m = x2

                j += 1

            i += 1

        return m


print 'sol is {}'.format(Solution().longestPalindrome('abb'))

# fywehvgdhsaaaabaaabytsvahgcadgc