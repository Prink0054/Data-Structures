class Node:
    def __init__(self, value):
        self.value = value
        self.nextnode = None


class SLinkedList:
    def __init__(self):
        self.headvalue = None

    def reverse(self,head):
        cur = head
        pre, nxt = None, None
        while cur:  # watch out
            nxt = cur.nextnode
            cur.nextnode = pre
            pre = cur
            cur = nxt
        return pre  # watch out
        pass

    def linklist(self):
        node = self.headvalue
        while node != None:
            print(node.value)
            node = node.nextnode


a = SLinkedList()
a.headvalue = Node("Mon")
b = Node("tue")
c = Node("wed")
a.headvalue.nextnode = b
b.nextnode = c
a.reverse(a.headvalue)
# a.linklist()
print(c.value)
print (c.nextnode.value)
print (b.nextnode.value)
# print (a.nextnode.value)


