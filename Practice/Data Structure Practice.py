class Node():
    def __init__(self,value):
        self.value = value
        self.nextnode = None

    def traverse(self):
        node = self
        while node != None:
            print(node.value)
            node = node.nextnode

a = Node(1)
b = Node(2)
c = Node(3)
a.nextnode = b
b.nextnode = c
a.traverse()






    #
    # s = Node(1)
    # node1 = Node(1)
    # node2 = Node(2)
    # node3 = Node(3)
    # print("I")
    # node1.next = node2
    # node2.next = node3
    #
    # node1.traverse()




#
# class Node():
#     def __init__(self,val):
#         self.val = val
#         self.next = None
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
