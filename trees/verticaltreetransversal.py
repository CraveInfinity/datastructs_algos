# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def verticalOrderTraversal(self, A):
        self.d = {}

        self.get_nodes(A, 0)

    def get_nodes(self, A, n):

        if A is None:
            return

        if self.d.has_key(n):
            self.d[n].append(A.val)
        else:
            self.d[n] = [A.val]
        self.get_nodes(A.left, n + 1)
        self.get_nodes(A.right, n - 1)


print Solution().verticalOrderTraversal()




