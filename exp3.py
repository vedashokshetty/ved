def lst():
    list = [1,2,3,4]

    list.append(5)

    print(f'Append funciton used: {list}')

    list.extend([7,8])

    print(f'List extended : {list}')

    list.remove(1)

    print(f'List remove function executed: {list}')

    list.insert(0,1)

    print(f'Insert function executed: {list}')
    popped_ele = list.pop()

    print(f'{popped_ele}, popped from {list}')

lst()

def tple():

    tuple = (1,2,3,4,5,5,5)

    arg1 = 4

    print(f'element {arg1} , has index value {tuple.index(arg1)}')

    arg2 = 5

    print(f'Count of {arg2} in tuple is: {tuple.count(arg2)}')

tple()

def set():
    set1 = {1,2,3,4,5,6}
    set1.add(8)

    print(f'element added in set : {set1}')

    set1.remove(3)
    print(f'Element removed : {set1}')

    ele = set1.pop()

    print(f'{ele} , popped from set {set1}')
print("------------------------------------------")
set()