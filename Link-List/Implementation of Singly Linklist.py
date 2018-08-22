# ========================Singly Linklist Implementation===================

class Node:
    def __init__(self, value):
        self.value = value
        self.nextnode = None


class SLinkedList:
    def __init__(self):
        self.headvalue = None


a = SLinkedList()
a.headvalue = Node("Mon")
b = Node("tue")
c = Node("wed")
a.headvalue.nextnode = b
b.nextnode = c
a.linklist()