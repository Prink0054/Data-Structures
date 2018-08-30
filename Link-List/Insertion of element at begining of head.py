#===========================Insertion of linklist in the begining of linklist====================

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



#===========================Insertion of linklist at the end of linklist====================


class Node :
    def __init__(self,value):
        self.value = value
        self.nextnode = None

class SLinklist :
    def __init__(self):
        self.headvalue = None


    def begining(self,newnode):
        Newnode = Node(newnode)
        # if self.headvalue is None:
        #     self.headvalue = Newnode
        #     # return

        last = self.headvalue

        while last.nextnode != None:
            last = last.nextnode

        last.nextnode = Newnode


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
a.begining("sun")
a.traverse()

#===========================Insertion of linklist in the begining of linklist====================


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





