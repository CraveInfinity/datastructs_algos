# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def front(self):
        return self.items[-1]


class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def levelOrder(self, A):
        res = {}

        if A is None:
            return

        q = Queue()
        q.enqueue((0, A))

        while not q.isEmpty():
            d, current = q.front()
            if res.has_key(d):
                res[d].append(current.val)
            else:
                res[d] = [current.val]

            if current.left is not None:
                q.enqueue((d + 1, current.left))
            if current.right is not None:
                q.enqueue((d + 1, current.right))

            q.dequeue()

        return res.values()