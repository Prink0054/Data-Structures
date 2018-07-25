# ===================================Bubble-Sort===========================================

def bubble(mydata):
     found = True
     while found:
        found = False
        for i in range(0,len(mydata)-1):
            if mydata[i] > mydata[i + 1]:
                found = True
                t = mydata[i]
                mydata[i] = mydata[i+1]
                mydata[i+1] = t
     return mydata


if __name__ == "__main__":
    data = [2,13,15,4,23,76,5]
    isitfound = bubble(data)
    print(isitfound)