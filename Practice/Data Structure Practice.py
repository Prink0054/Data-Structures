def compress(s):
    r = ""
    l = len(s)

    if l == 0:
        return ''
    if l == 1:
        return s + '1'

    last = s[0]
    cnt = 1
    i = 1

    while i < l :


        if s[i] == s[i-1]:

            cnt += 1

        else:
            r = r + s[i-1] + str(cnt)
            cnt = 1
        i += 1
    r = r + s[i - 1] + str(cnt)
    return r
    pass


print((compress('HHBBB')))




# class Node():
#     def __init__(self,value):
#         self.value = value
#         self.nextnode = None
#
#     def traverse(self):
#         node = self
#         while node != None:
#             print(node.value)
#             node = node.nextnode
#     #
#     # def duplicates(self):
#     #     els = []
#     #     node = self
    #     previous = None
    #     while node != None:
    #         if node.value in els:
    #             previous.nextnode = node.nextnode
    #         else:
    #             els.append(node.value)
    #         previous = node
    #         node = node.nextnode
    #
    # def lastnode(self, k):
    #     if k < 0:
    #         return None
    #     i = -1
    #     node = self
    #     p2 = self
    #     while node != None:
    #         node = node.nextnode
    #         if i < k:
    #             i += 1
    #         else:
    #             p2 = p2.nextnode
    #     if i == k:
    #         return p2.value
    #     else:
    #         return None
#
# a = Node(1)
# b = Node(2)
# c = Node(3)
# d = Node(2)
# e = Node(7)
#
# a.nextnode = b.
# b.nextnode = c
# c.nextnode = d
# a.duplicates()
# a.traverse()


# def data(s):
#     char = []
#     matches = {')':'(',']':'[','}':'{'}
#     for c in s:
#         # print(c)
#         if c in matches:
#             if char.pop() != matches[c]:
#                     return False
#             else:
#                 char.append(c)
#     return char == []
#     pass
# print(data("[()]"))
#
# def balance_check(s):
#     chars = []
#     matches = {')':'(',']':'[','}':'{'}
#     for c in s:
#         if c in matches:
#             print(matches[c])
#             if chars.pop() != matches[c]:
#                 return False
#         else:
#             chars.append(c)
# #             print(chars)
# #     # print(chars)
# #     return chars == []
# #     pass
#
#
# print(balance_check("([])"))
# # print(balance_check("[()]"))
#
#
#
#
#











# def balance_check(s):
#     chars = []
#     matches = {')':'(',']':'[','}':'{'}
#     for c in s:
#         if c in matches:
#             if chars.pop() != matches[c]:
#                 return False
#         else:
#             chars.append(c)
#     return chars == []
#     pass
#
#
# print(balance_check("[]"))
# print(balance_check("[()]"))




# from collections import deque
# queue = deque(["Ram", "Tarun", "Asif", "John"])
# print(queue)
# queue.append("Akbar")
# print(queue)
# print(queue.popleft())
# # print(queue.popleft())
# print(queue)




#
# class Node():
#     def kth_to_last(self,k):
#         if k < 0:
#             return None
#         p1 = self
#         p2 = self
#         i = -1
#         while p1 != None:
#             p1 = p1.next
#             if i < k:
#                 i += 1
#             else:
#                 p2 = p2.next
#         if i == k:
#             return p2.val
#         else:
#             return None
#
# if __name__ == "__main__":
#     node1 = Node(1)
#     node2 = Node(2)
#     node3 = Node(3)
#     node4 = Node(1)
#     node1.next = node2
#     node2.next = node3
#     node3.next = node4
#     print(node1.kth_to_last(2))
#     print(node1.kth_to_last(-10))
#
#





# a = Node(1)
# b = Node(2)
# c = Node(3)
#
# a.nextnode = b
# b.nextnode = c
# a.traverse()
# b.traverse()
# c.traverse()
#
#
#
#
#
# # isthis is the best thing i had ever seen in my life o occupy the system to demonstrate the source of
# # print(destination)
# while print(hghjg):
#     p)
#
# class Data:
#     if a = 10:
#         print("print")
#     else:
#         print("hello")
#
#     ellipsis:
#         print("hi how are you?")
# class Node:
#
#     def __init__(self, value):
#         self.value = value
#         self.nextnode  = None
# a = Node(1)
# b = Node(2)
# c = Node(3)
# d = Node(4)
# e = Node(5)
#
# a.nextnode = b
# b.nextnode = c
# c.nextnode = d
# d.nextnode = e
#
# # This would return the node d with a value of 4, because its the 2nd to last node.
# target_node = nth_to_last_node(2, a)
#
#
#      def nth_to_last_node(n, head):
#         left_pointer = head
#         right_pointer = head
#
#         # Set right pointer at n nodes away from head
#         for i in xrange(n - 1):
#
#             # Check for edge case of not having enough nodes!
#             if not right_pointer.nextnode:
#                 raise LookupError('Error: n is larger than the linked list.')
#
#             # Otherwise, we can set the block
#             right_pointer = right_pointer.nextnode
#
#         # Move the block down the linked list
#         while right_pointer.nextnode:
#             left_pointer = left_pointer.nextnode
#             right_pointer = right_pointer.nextnode
#
#         # Now return left pointer, its at the nth to last element!
#         return left_pointer
#
#
#


# # Node class
# class Node:
#
#     # Constructor to initialize the node object
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# class LinkedList:
#
#     # Function to initialize head
#     def __init__(self):
#         self.head = None
#
#     # Function to insert a new node at the beginning
#     def push(self, new_data):
#         new_node = Node(new_data)
#         new_node.next = self.head
#         self.head = new_node
#
#     def printNthFromLast(self, n):
#         main_ptr = self.head
#         ref_ptr = self.head
#
#         count = 0
#         if (self.head is not None):
#             while (count < n):
#                 if (ref_ptr is None):
#                     print
#                     "%d is greater than the no. pf \
#                             nodes in list" % (n)
#                     return
#
#                 ref_ptr = ref_ptr.next
#                 count += 1
#
#         while (ref_ptr is not None):
#             main_ptr = main_ptr.next
#             ref_ptr = ref_ptr.next
#
#         print
#         "Node no. %d from last is %d " % (n, main_ptr.data)
#
#
# # Driver program to test above function
# llist = LinkedList()
# llist.push(20)
# llist.push(4)
# llist.push(15)
# llist.push(35)
#
# llist.printNthFromLast(4)
#
# # This code is contributed by Nikhil Kumar Singh(nickzuck_007)
#
#
#
#
#
# # # quick sort
# #
# # def partition(myList, start, end):
# #     pivot = myList[start]
# #     left = start+1
# #     # Start outside the area to be partitioned
# #     right = end
# #     done = False
# #     while not done:
# #         while left <= right and myList[left] <= pivot:
# #             left = left + 1
# #         while myList[right] >= pivot and right >=left:
# #             right = right -1
# #         if right < left:
# #
# #             this is the best practice of the market to overall the system to use the system to ensure
# #             with lambda to getattr()
# #             done= True
# #             d
# #
# #         else:
# #             # swap places
# #
# #             temp=myList[left]
# #
# #             myList[left]=myList[right]
# #             myList[right]=temp
# #     # swap start with myList[right]
# #
# #     temp=myList[start]
# #     myList[start]=myList[right]
# #
# #     myList[right]=temp
# #     return right
# #
# #
# # def quicksort(myList, start, end):
# #     if start < end:
# #         # partition the list
# #         split = partition(myList, start, end)
# #         # sort both halves
# #
# #         quicksort(myList, start, split-1)
# #         quicksort(myList, split+1, end)
# #     return myList
# #
# #
# #
# # if __name__ == "__main__":
# #     myList = [7,2,5,1,29,6,4,19,11]
# #     print("hii")
# #     sortedList = quicksort(myList,0,len(myList)-1)
# #     print(sortedList)
# #     this is the best to sorted("this is the besy")
# #
# #
# #
# #
# #
# #
#
#
#
# # for i in range(0,4):
# #     for j in range(0,4):
# #         print("*",end="")
# #     print()
# #
#
#
# # for i in range(0,4):
# #     for j in range(0,i):
# #         print("*",end=" ")
# #     print()
#
#
# #
# # for i in range(0,4):
# #     for j in range(i,4):
# #         print("*",end= " ")
# #     print()
#
# # for i in range(0,4):
# #     for j in range(i,4-1):
# #         print("_",end=" ")
# #     for k in range(0,i+1):
# #         print("*",end=" ")
# #
# #     print()
#
# # for i in range(0,4):
# #     for j in range(j,4-1):
# #         print("_",end= " "):
# #     for k in range(k,)
#
#
