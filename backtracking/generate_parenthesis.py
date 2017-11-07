# class Solution:
#     # @param A : integer
#     # @return a list of strings
#     def generateParenthesis(self, A):
#
#         self.A = A
#
#         self.final = []
#
#         self.parenthesis('', 1, False, False, 0)
#
#         return sorted(list(set(self.final)))
#
#     def parenthesis(self, i, j, conc, r, rc):
#         if conc:
#             if rc == 1:
#                 m = len(i) - 1
#                 while m >= 0:
#                     if i[m] == '(':
#                         i = i[:m + 1] + '()' + i[m + 1:]
#                         break
#                     m -= 1
#             elif rc == 2:
#                 m = 0
#                 while m < len(i):
#                     if i[m] == ')':
#                         i = i[:m] + '()' + i[m:]
#                         break
#
#                     m += 1
#
#             elif rc == 3:
#                 i = '({})'.format(i)
#
#         else:
#             if r:
#                 i = '{}()'.format(i)
#             else:
#                 i = '(){}'.format(i)
#
#         if j == self.A:
#             self.final.append(i)
#             return
#
#         # self.parenthesis(i, j + 1, True, True, 1)
#         # self.parenthesis(i, j + 1, True, True, 2)
#         self.parenthesis(i, j + 1, True, True, 3)
#         self.parenthesis(i, j + 1, False, True, 0)
#         self.parenthesis(i, j + 1, False, False, 0)
#
#
# j = Solution().generateParenthesis(6)
#
# print j
# print len(j)




""" Solution approach -- recursion tree"""


class Solution:
    # @param A : integer
    # @return a list of strings
    def generateParenthesis(self, A):

        self.A = A
        self.final = []
        self.parenthesis('', '(')

        return sorted(set(self.final))

    def val_brackets(self, a):
        i = 0
        k = []

        # print a

        while i < len(a):
            if a[i] == ')':
                if len(k):
                    # print k
                    k.pop()
                else:
                    return False
            else:
                k.append(a[i])
            i += 1

        return len(k) == 0

    def parenthesis(self, i, x):

        i += x

        if len(i) == 2 * self.A:
            # print 'hell'
            # print self.val_brackets(i)
            if self.val_brackets(i):
                self.final.append(i)
            return

        self.parenthesis(i, '(')
        self.parenthesis(i, ')')



j = Solution().generateParenthesis(6)

print j
print len(j)


