def add_content ():
    f = open("word.txt",'w')
    sn = input("Enter content to add to file: ")
    f.write(sn)
    f.close()

def display_content():
    f = open("word.txt",'r')
    x = f.read()
    print('------------------------------------------------')
    print(x)
    print('------------------------------------------------')

def count():
    f = open('word.txt','r')
    x = f.read()
    upper = 0
    digit = 0

    for i in x:
        if i.isupper():
            upper+=1
        elif i.isdigit():
            digit+=1
    print('--------------------------------')
    print(f'Number of Uppercase letters = {upper}\n'
          f'Number of digits = {digit}')
    print('--------------------------------')

while True:
    print('''File Operations
    1.Add fresh content to file
    2. Display content of the file
    3. Display the counters
    4. Exit''')

    ch = int(input("Enter choice: "))

    if ch == 1:
        add_content()
    elif ch==2:
        display_content()

    elif ch ==3:
        count()
    elif ch == 4:
        break
    else:
        print("Invalid Choice!")


