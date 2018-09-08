s = 0
for i in range(0,5):
    for j in range(i,5-1):
        print("_",end=" ")
    # print()

    for k in range(0,2*i+1):
        if (k%2==0):
            print("_",end=" ")
        else:
            print("*",end=" ")
    print()