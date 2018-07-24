# ========================================Binary-Search Using For loop=================================s
def binarySearch(mydata,myitem):
    found = False
    bottom = 0
    top = len(mydata)-1
    for i in range(0,len(mydata)):
        mid = int((bottom + top)/2)
        if mydata[mid] == myitem :
            found = True
        elif mydata[mid] < myitem:
            bottom = mid + 1
        else:
            top = mid - 1
    return found


if __name__ == "__main__":
    data = [2,4,5,6,12,16,20,30,45]
    item = int(input("Enter number you want to search") )
    isitfound = binarySearch(data,item)
    if isitfound:
        print("ITEM FOUND ")
    else:
        print("not found")
