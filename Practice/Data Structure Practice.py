from collections import deque
queue = deque(["rahul","er"])
print(queue)
queue.append("mn")
print(queue)
queue.append("mk")
print(queue)
queue.popleft()
print(queue)
queue.pop()
print(queue)
queue.pop()
print(queue)



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
