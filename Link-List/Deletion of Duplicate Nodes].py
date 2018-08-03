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



a = Node(1)
b = Node(2)
c = Node(3)
d = Node(1)
a.nextnode = b
b.nextnode = c
c.nextnode = d
a.duplicates()
a.traverse()

