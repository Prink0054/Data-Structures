# ========================================Insertion Sort===================================

def insertion_sort(mydata):
    for i in range(0,len(mydata)):

#         Get current position and current value
          position = i
          current_value = mydata[i]

          while position > 0 and   mydata[position-1]>current_value:
              mydata[position] = mydata[position - 1]
              position = position - 1
          mydata[position] = current_value



if __name__ == "__main__":
    data = [4,1,5,3,8,5,2,9]
    insertion_sort(data)
    print(data)


