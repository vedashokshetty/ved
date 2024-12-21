import recbin as bin
def linear_search(target,list):

    for i in list:
        if i == target:

            print(i)
    else:
        print("Value not found")

lst = [1,2,3,2,434,2,1,3,34,2311]

target  = 77

linear_search(target,lst)






