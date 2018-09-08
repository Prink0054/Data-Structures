a = 5
if a>1:
    for i in range(2,a):
        if(a%2==0):
            print("number is not prime")
            break
        else:
            print("prime")

else:
    print("not prime")




lower = 2
upper = 100
count = 0
for num in range(lower,upper + 1):

   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           count += 1
print(count)