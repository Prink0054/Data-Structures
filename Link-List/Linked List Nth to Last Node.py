#========================== Linked List Nth to Last Node=======================
class Node():
    def __init__(self,value):
        self.value = value
        self.nextnode = None

    def traverse(self):
        node = self
        while node != None:
            print(node.value)
            node = node.nextnode

    def duplicates(self):
        els = []
        node = self
        previous = None
        while node != None:
            if node.value in els:
                previous.nextnode = node.nextnode
            else:
                els.append(node.value)
            previous = node
            node = node.nextnode

    def lastnode(self,k):
        if k < 0:
            return None
        i = -1
        node = self
        p2 = self
        while node != None:
            node = node.nextnode
            if i < k:
                i += 1
            else:
                p2 = p2.nextnode
        if i == k:
            return p2.value
        else:
            return None



a = Node(3)
b = Node(4)
c = Node(5)
d = Node(6)
a.nextnode = b
b.nextnode = c
c.nextnode = d
a.duplicates()


a.traverse()

print(a.lastnode(3))