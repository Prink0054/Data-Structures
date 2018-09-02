stack1 = []
stack2 = []

def enqueue(elemrnt):
    stack1.append(elemrnt)

def dequeue():
    if len(stack2) == 0:
        if len(stack1) == 0:
            return "empty queue"

        while len(stack1) > 0:
            p = stack1.pop()
            stack2.append(p)
    return stack2.pop()

enqueue('a')
enqueue('b')
enqueue('c')
print(dequeue())