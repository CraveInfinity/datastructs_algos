""" jujubi solution """

# class Solution:
#     # @param A : string
#     # @return an integer
#     def longestValidParentheses(self, A):
#         stack = []
#
#         count = 0
#
#         for i in A:
#             print stack
#             if i == '(':
#                 stack.append('(')
#                 count += 1
#             elif i == ')':
#                 if len(stack):
#                     count += 1
#                     stack.pop()
#
#         final = count - len(stack)
#
#         return final


""" Least valid solution """
class Solution:
    # @param A : string
    # @return an integer
    def longestValidParentheses(self, A):

        self.parethesis(A)


    def parethesis(self, start, end):
        if start == len(A)-1:
            return

        self.parethesis(start, end+1)
        self.parethesis(start+1, end)


A = ")()))(())((())))))())()(((((())())((()())(())((((())))())((()()))(()(((()()(()((()()))(())()))((("
A = "(()))()()()"

print Solution().longestValidParentheses(A)