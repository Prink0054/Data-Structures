class Node :
    def __init__(self,value):
        self.value = value
        self.nextnode = None

class SLinklist :
    def __init__(self):
        self.headvalue = None

    def lastnode(self, k):
        if k < 0:
            return None
        i = -1
        node = self.headvalue
        p2 = self.headvalue
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

    def traverse(self):
        node = self.headvalue
        while node != None:
            print(node.value)
            node = node.nextnode


a = SLinklist()
a.headvalue = Node("Mon")
b = Node("TUE")
c = Node("wed")

a.headvalue.nextnode = b
b.nextnode = c
# a.Inbetween(a.headvalue,"hiii")
# a.RemoveNode("wed")
a.traverse()
print(a.lastnode(0))




