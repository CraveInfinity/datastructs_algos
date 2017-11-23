# Definition for a  binary tree node


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    # @param A : head node of linked list
    # @return the root node in the tree
    def __init__(self):
        self.bst_arr = None

    def sortedListToBST(self, A):

        self.bst_arr = self.get_array(A)
        l = self.binary_tree(0, len(self.bst_arr))
        return l

    def binary_tree(self, start, end):
        if start == end:
            return None

        mid = start + (end-start)/2

        root = TreeNode(self.bst_arr[mid])

        root.left = self.binary_tree(start, mid)
        root.right = self.binary_tree(mid+1, end)

        return root

    @staticmethod
    def get_array(l_list):
        res = []
        l = l_list
        while l is not None:
            res.append(l.val)
            l = l.next

        return res


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
# d = ListNode(4)
a.next = b
b.next = c
# c.next = d
x = Solution().sortedListToBST(a)

print x.val
print x.left.val
print x.right.val
print x.left.left
print x.left.right

print x.right.left
print x.right.right


