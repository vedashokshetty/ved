def binary_search(list,target):

    if len(list)==0:
         print("Empty list")
    else:
        midpoint = len(list)//2
        if list[midpoint]>target:
            return binary_search(list[:midpoint],target)
        elif list[midpoint]<target:
            return binary_search(list[midpoint:],target)
        elif list[midpoint]==target:
            print("Target Found")





lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

binary_search(lst,12)
