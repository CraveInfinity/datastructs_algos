# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def maxPathSum(self, A):
        self.res = float('-inf')
        self.findmaxutils(A)
        return self.res

    def findmaxutils(self, root):

        if root is None:
            return 0

        l = self.findmaxutils(root.left)
        r = self.findmaxutils(root.right)

        single = max(max(l, r) + root.val, root.val)

        top = max(single, l + r + root.val)
        self.res = max(self.res, top)
        return single

root = TreeNode(10)
root.left = TreeNode(2)
root.right   = TreeNode(10);
root.left.left  = TreeNode(20);
root.left.right = TreeNode(1);
root.right.right = TreeNode(-25);
root.right.right.left   = TreeNode(3);
root.right.right.right  = TreeNode(4);

print "Max path sum is " ,Solution().maxPathSum(A=root)