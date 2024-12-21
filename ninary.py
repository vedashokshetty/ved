import pickle
def add_employees():
    with open("EMP.dat",'wb') as file:
        employees = [         {'empno':1,'ename':'Ashok','salary': 2334213} ,
                              {'empno': 2, 'ename': 'ved', 'salary': 23553213},
                              {'empno': 3, 'ename': 'anil', 'salary': 23327813},
                              {'empno': 4, 'ename': 'veena', 'salary': 23321433},
                              {'empno': 5, 'ename': 'vanshika', 'salary': 233287613},
                              ]
        pickle.dump(employees,file)

def display_employees():
    with open('EMP.dat','rb') as file:
        employees =pickle.load(file)
        for employee in employees:
            print(employee)



