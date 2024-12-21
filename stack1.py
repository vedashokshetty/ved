MAX_ITEMS = 5
top = None
stack = []


def accept():
    id = int(input("ENter id: "))
    name = input("Enter name: ")
    dpt = input("Enter department name: ")
    fee = float(input("Enter fee: "))
    return [id, name, dpt, fee]

def is_empty():
    if len(stack) == 0:
        return True
    else:
        return False

def push(item):
    if len(stack) == MAX_ITEMS:
        return "overflow"
    else:
        stack.append(item)
        top = len(stack) - 1

def pop():
    if is_empty():
        return "Stack underflow"
    else:
        x = stack.pop()
        top = len(stack)-1
        return x

def display():
    if is_empty():
        print("Stack is empty")
    else:
        top = len(stack)-1
        for i in range(top,-1,-1):
            print(stack[i])

def display_top():
    if is_empty():
        print("Underflow")
    else:
        top = len(stack)-1
        print("top element of the stack is ",stack[top])




while True:
    print('''Stack operations
    1. Push
    2. Pop
    3. Display
    4. Display Top Element
    5. Exit''')

    ch = int(input("Enter choice:"))
    if ch == 1:
        item = accept()
        push(item)
    elif ch == 2:
        x = pop()
        print(x)
    elif ch == 3:
        display()
    elif ch == 4:
        display_top()
    elif ch == 5:
        break
        







