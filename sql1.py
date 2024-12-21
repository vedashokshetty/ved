import mysql.connector

db = mysql.connector.connect(host='122.166.153.34',username="wbilz", password="$ProjectI2020",database = 'dbset2')

if db.is_connected():
    print("Successful")

def print_rows(dept=None):
    cs = db.cursor()
    q1 = 'select * from staff'
    if dept is not None:
        q1 = f'select * from staff where dept = \'{dept}\''
    cs.execute(q1)
    res = cs.fetchall()
    print(f'Staff From {dept}')
    for i in res:
        print(i)

# print_rows("Before Update")


# q2 = 'update staff set salary = salary*1.05'
# cs = db.cursor()
# cs.execute(q2)
# db.commit()
#
# print_rows("After Update")
# db.close()
print_rows()

dept = input("Enter department: ")
print_rows(dept)

