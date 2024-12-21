import csv

def Write_info ():
    with open("tourist.csv","a+",newline='') as f:
        r = csv.writer(f, delimiter = ",")
        slno = int(input("Enter serial number: "))
        tname = input("Enter tourist name: ")
        city = input("Enter city: ")
        r.writerow([slno,tname,city])


def read_info():
    f = open("tourist.csv",'r')
    r = csv.reader(f)
    for i in r:
        print(i)


with open("tourist.csv","w", newline='') as f:
    x = csv.writer(f, delimiter = ',')
    x.writerow(["SLNO.","Tourist_Name","City"])



while True:
    print('''1. Add details
    2.Display details
    3.Exit''')

    ch = int(input("Enter choice: "))

    if ch == 1:
        Write_info()

    elif ch == 2:
        read_info()

    elif ch == 3:
        break
    else:
        print("Invalid choice!")





