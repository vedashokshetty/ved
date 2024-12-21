lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18.19,20]

found = False
target =20
first = 0
last = len(lst)-2

midpoint = first+last//2
while found == False:

     if midpoint == target:
        print("Target found at ", midpoint,lst[midpoint])
        found = True
        break

     elif midpoint < target:
         first = midpoint
         midpoint = 0
         midpoint = (last + first) // 2


     elif target<midpoint:
         midpoint = (first + midpoint)//2

























