import pickle
import os
def insert(filename):
    tdict ={}
    tnum = int(input("Enter ticket num: "))
    source = input("Enter source: ")
    dst = input("Enter destination: ")
    cost = float(input("Enter cost:"))
    tdict['Tnum'] = tnum
    tdict['Source'] = source
    tdict['Destination'] = dst
    tdict['Cost'] = cost
    with open(filename,"ab") as x:
        pickle.dump(tdict,x)

def displayall(filename):
    print("Displaying file.")
    fobj=open(filename,'rb')
    try:
      while True:
         dat=pickle.load(fobj) #Displaying.
         print(dat)
    except EOFError:
     print("End of file.")
    except FileNotFoundError:
     print("File not found.")
     fobj.close()

f = open('ticket1.dat')
insert(f)




