class Node(object):
    def __init__(self):
        self.val = None
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, A):
        self.A = A
        self.root = Node()

    def construct(self):
        for a in self.A:
            pass

    def insert(self, element):
        current_node = self.root
        insert_node = Node()
        insert_node.val = element
        while True:
            if current_node.val is None:
                current_node.val = element
            else:
                if current_node.val < element:
                    if current_node.left is None:
                        current_node.left = insert_node
                        break
                    else:
                        current_node = current_node.left
                else:
                    if current_node.right is None:
                        current_node.right = insert_node
                        break
                    else:
                        current_node = current_node.right

class Solution:
    # @param A : integer
    # @return an integer
    def numTrees(self, A):

        c = self.trees(list(xrange(1, A+1)))
        return c

    def trees(self, arr):

        if len(arr) == 0:
            return 0

        if len(arr) == 1:
            return 1

        count = 0
        for i, a in enumerate(arr):
            left = arr[:i]
            right = arr[i+1:]

            count += self.trees(left)
            count += self.trees(right)

        return count



print Solution().numTrees(6)