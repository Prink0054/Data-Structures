class Node:
    def __init__(self, value):
        self.value = value
        self.nextnode = None

class SLinkedList:
    def __init__(self):
        self.headvalue = None

    def listprint(self):
        node = self.headvalue
        while node != None:
            print (node.value)
            node = node.nextnode

    def begin(self,newdata):
        Newnode = Node(newdata)
        Newnode.nextnode = self.headvalue
        self.headvalue = Newnode


a = SLinkedList()
a.headvalue = Node("mon")
b = Node("Tue")
c = Node("Wed")

a.headvalue.nextnode = b
b.nextnode = c
a.begin("sun")
a.listprint()




