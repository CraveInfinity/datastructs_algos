# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def isBalanced(self, A):

        self.l = -1
        self.r = -1

        self.hello = 1

        self.subtree(A)

        return self.hello

    def subtree(self, tree):
        if tree is None:
            return 0

        l = self.subtree(tree.left)
        r = self.subtree(tree.right)

        if abs(l - r) > 1:
            self.hello = 0

        return max(l, r) + 1
