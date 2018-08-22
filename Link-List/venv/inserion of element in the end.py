class Node():
    def __init__(self,value):
        self.value = value
        self.nextnode = None


class Slinklist():
    def __init__(self):
        self.headvalue = None

    def insert(self,value):
       Newnode = Node(5)
       if self.headvalue is None:
            self.headvalue = Newnode
            return

       last = self.headvalue
       while(last.nextnode):
            last = last.nextnode
       last.nextnode = Newnode



    def traverse(self):
        node = self.headvalue
        while node!= None:
            print(node.value)
            node = node.nextnode

a = Slinklist()
a.headvalue = Node(1)
b = Node(2)
c = Node(3)

a.headvalue.nextnode = b
b.nextnode = c
a.insert(5)
a.traverse()
