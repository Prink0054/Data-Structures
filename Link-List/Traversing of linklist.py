class Node():
    def __init__(self,value):
        self.value = value
        self.nextnode = None

    def traverse(self):
        node = self
        while node != None:
            print(node.value)
            node = node.nextnode

a = Node(1)
b = Node(2)
c = Node(3)
a.nextnode = b
b.nextnode = c
a.traverse()