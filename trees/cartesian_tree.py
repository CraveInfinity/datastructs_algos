"""
    Cartesian tree : is a heap ordered binary tree, where the root is greater than all the elements in the subtree
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # @param A : list of integers
    # @return the root node in the tree
    def __int__(self):
        self.tree = None

    def buildTree(self, A):
        if len(A) == 0 :
            return None
        val = max(A)
        i = A.index(val)

        tree = TreeNode(val)

        tree.left = self.buildTree(A[:i])
        tree.right = self.buildTree(A[i+1:])

        return tree