class Node :
    def __init__(self,value):
        self.value = value
        self.nextnode = None

class SLinklist :
    def __init__(self):
        self.headvalue = None

    def Inbetween(self, middle_node, newdata):
        # if middle_node is None:
        #     print("The mentioned node is absent")
        #     return

        NewNode = Node(newdata)
        NewNode.nextnode = middle_node.nextnode
        middle_node.nextnode = NewNode

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
a.Inbetween(a.headvalue,"hiii")
a.traverse()

