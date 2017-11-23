# Definition for a undirected graph node


class Queue(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, element):
        self.items.insert(0, element)

    def dequeue(self):
        self.items.pop()

    def front(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def list(self):
        return self.items


class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution(object):
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        q = Queue()
        label_dict = dict()
        q.enqueue(node)

        while not q.is_empty():
            current = q.front()
            q.dequeue()

            if current in label_dict:
                current_copy = label_dict[current]
            else:
                current_copy = UndirectedGraphNode(current.label)
                label_dict[current] = current_copy

            for node_x in current.neighbors:
                if node_x in label_dict.keys():
                    if label_dict[node_x] not in current_copy.neighbors:
                        current_copy.neighbors.append(label_dict[node_x])
                else:
                    label_dict[node_x] = UndirectedGraphNode(node_x.label)
                    current_copy.neighbors.append(label_dict[node_x])
                    q.enqueue(node_x)

        return label_dict[node]


a = UndirectedGraphNode(703)
b = UndirectedGraphNode(43)
c = UndirectedGraphNode(279)


a.neighbors.append(b)
a.neighbors.append(a)
a.neighbors.append(c)

b.neighbors.append(c)
b.neighbors.append(a)

c.neighbors.append(b)
c.neighbors.append(a)
c.neighbors.append(c)


h = Solution().cloneGraph(a)

print h.label
for n in h.neighbors:
    print n.label
    print "\n"
    for p in n.neighbors:
        print p.label

    print "\n\n"








