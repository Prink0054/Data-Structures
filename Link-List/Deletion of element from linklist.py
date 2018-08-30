class Node :
    def __init__(self,value):
        self.value = value
        self.nextnode = None

class SLinklist :
    def __init__(self):
        self.headvalue = None

    def RemoveNode(self, Removekey):

        HeadVal = self.headvalue

        if (HeadVal is not None):
            if (HeadVal.value == Removekey):
                self.headvalue = HeadVal.nextnode
                HeadVal = None
                return

        while (HeadVal is not None):
            if HeadVal.value == Removekey:
                break
            prev = HeadVal
            HeadVal = HeadVal.nextnode

        if (HeadVal == None):
            return

        prev.nextnode = HeadVal.nextnode

        HeadVal = None

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
a.RemoveNode("wed")
a.traverse()

