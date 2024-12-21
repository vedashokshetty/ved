import pickle
import os


def insert(filename): print("Inserting file.")


tdict = {}
tnum = int(input("Enter tnum: "))
source = input("Enter source: ")
dest = input("Enter destination: ")
cost = float(input("Enter cost: "))
tdict['Tnum:'] = tnum
tdict['Source:'] = source
tdict['Destination:'] = dest
tdict['Cost:'] = cost
with open(filename, 'ab') as fobj: pickle.dump(tdict, fobj)  # Inserting.


def displayall(filename): print("Displaying file.")


fobj = open(filename, 'rb')
try:
 while True:
  dat = pickle.load(fobj)  # Displaying.
print(dat) except EOFError:
print("End of file.") except FileNotFoundError:
print("File not found.")
fobj.close()


def search(filename, kTnum): print("Searching file...")


found = False
fobj = open(filename, 'rb')
try:
 while True:
  dat = pickle.load(fobj)
if dat['Tnum:'] == kTnum:  # Searching.
 found = True
 print(dat)
except FileNotFoundError: print("File not found.")
except EOFError:

if found == False:
 print("No results.")
else:
 print("Search concluded.")
 fobj.close()


def modify_withtemp(filename, kTnum): found = False


fobj = open(filename, 'rb')
tfobj = open('copy.dat', 'wb')  # Making copy. try:
while True:
 dat = pickle.load(fobj)
 if dat['Tnum:'] == kTnum:
  found = True
 print("Updating...")
 tdict = {}
source = input("Enter source: ")
dest = input("Enter destination: ")
cost = float(input("Enter cost: "))
tdict['Tnum:'] = kTnum
tdict['Source:'] = source
tdict['Destination:'] = dest
tdict['Cost:'] = cost
pickle.dump(tdict, tfobj)
else:
pickle.dump(dat, tfobj) except FileNotFoundError:
print("File not found.") except EOFError:
if found == False: print("No results.")
fobj.close()
tfobj.close()
os.remove(filename)
os.rename('copy.dat', filename)


def modify_withouttemp(filename, kTnum): found = False


fobj = open(filename, 'rb+')
try:
 while True:
  rpos = fobj.tell()

dat = pickle.load(fobj)
if dat['Tnum:'] == kTnum:
 found = True
 print("Updating...")
 tdict = {}
source = input("Enter source: ")
dest = input("Enter destination: ")
cost = float(input("Enter cost: "))
tdict['Tnum:'] = kTnum
tdict['Source:'] = source
tdict['Destination:'] = dest
tdict['Cost:'] = cost
fobj.seek(rpos)  # On-spot modification.
pickle.dump(tdict, fobj) except FileNotFoundError:
print("File not found.") except EOFError:
if found == False: print("No results.")
fobj.close()


def delete_withtemp(filename, kTnum): found = False


fobj = open(filename, 'rb')
tfobj = open('copy.dat', 'wb')
try:
 while True:
  dat = pickle.load(fobj)
if dat['Tnum:'] == kTnum:  # Skipping value.
 found = True
 print("Deleting...")
 pass
else:
 pickle.dump(dat, tfobj) except FileNotFoundError:
print("File not found.") except EOFError:
if found == False: print("No results.")
fobj.close()
tfobj.close()
os.remove(filename)
os.rename('copy.dat', filename)

print("Menu: \n1) Insert. \n2) View. \n3)Search. \n4) Temp-Modify. \n5) Modify. \n6) Delete. \n7) Exit.")
while True:
 uc = input("Enter user choice: ")
 if uc == '1':
  filename = input("Enter filename with .dat extension: ")
 insert(filename)
  elif uc == '2':
  filename = input("Enter filename with .dat extension: ")
  displayall(filename)
  elif uc == '3':
  filename = input("Enter filename with .dat extension: ")
  kTnum = int(input("Enter tnum: "))
  search(filename, kTnum) elif uc == '4':
  filename = input("Enter filename with .dat extension: ")
  kTnum = int(input("Enter tnum: "))
  modify_withtemp(filename, kTnum)
  elif uc == '5':
  filename = input("Enter filename with .dat extension: ")
  kTnum = int(input("Enter tnum: "))
  modify_withouttemp(filename, kTnum)
  elif uc == '6':
  filename = input("Enter filename with .dat extension: ")
  kTnum = int(input("Enter tnum: "))
  delete_withtemp(filename, kTnum)
  elif uc == '7':
  print("Exiting...")
  break
  else:
  print("Invalid input.")


