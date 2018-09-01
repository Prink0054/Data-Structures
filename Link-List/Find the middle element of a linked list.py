class node:
    def __init__(self,value):
        self.value = value
        self.nextnode = None

class slinklist:
    def __init__(self):
        self.headvalue = None


    def end(self,newnode,mid):
        Newnode = node(newnode)
        Newnode.nextnode = mid.nextnode
        mid.nextnode = Newnode

    def last(self):
       fast = self.headvalue
       slow = self.headvalue
       while fast.nextnode is not None and fast.nextnode.nextnode is not None:
           fast = fast.nextnode.nextnode
           slow = slow.nextnode
       print(slow.value)


    def traverse(self):
        node = self.headvalue
        while node is not None:
            print(node.value)
            node = node.nextnode


a = slinklist()
a.headvalue = node("mon")
b = node("tues")
c = node("wed")
d = node("thu")
e = node("fri")
f = node("sat")
g = node("sun")
a.headvalue.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e
e.nextnode = f
f.nextnode = g



# print(a)
# a.traverse()


a.last()
