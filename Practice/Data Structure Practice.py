def insertion_sort(aryy):
    for i in range(0,len(aryy)):

        currentvalue = aryy[i]
        position = i

        while position>0 and aryy[position-1]>currentvalue:
            aryy[position] = aryy[position-1]
            position = position - 1


        aryy[position] = currentvalue


ary = [3,5,8,10,23,32,2,98]
insertion_sort(ary)



# j = [1,2,3,4 ]
# print(j[2][1])
# j.append(


# for i in range(0,4):
#     for j in range(0,4):
#         print("*",end="")
#     print()
#


# for i in range(0,4):
#     for j in range(0,i):
#         print("*",end=" ")
#     print()
#
# for i in range(0,4):
#     for j in range(i,4):
#         print("*",end= " ")
#     print()

# for i in range(0,4):
#     for j in range(i,4-1):
#         print("_",end=" ")
#     for k in range(0,i+1):
#         print("*",end=" ")
#
#     print()

# for i in range(0,4):
#     for j in range(j,4-1):
#         print("_",end= " "):
#     for k in range(k,)


