def linearSearch(myItem,myList):
    found = False
    position = 0
    while position < len(myList) and not found:
        if myList[position] == myItem:
            found = True
        position = position + 1
    return found


if __name__ == "__main__":
    shopping = ["apples","bananas","chocolate","pasta"]
    item = input("What item you want to search" + "\n")
    isitFound = linearSearch(item,shopping)
    if isitFound:
        print("Your item is in the list")
    else:
        print("Your item is not in the list")
