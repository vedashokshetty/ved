import mysql.connector

db = mysql.connector.connect(host='122.166.153.34',username="wbilz", password="$ProjectI2020",database = 'dbset2')

if db.is_connected():
    print("Successful")



def print_books():
    cs = db.cursor()
    cs.execute("select * from BOOKS;")
    books = cs.fetchall()
    for book in books:
        print(book)
    cs.close()
def delete_book(code):
    code = int(input("Enter book code:"))
    cs = db.cursor()
    cs.execute(f'delete from BOOKS where code ={code} ')
    db.commit()
    cs.close()
    print_books()






print_books()

delete_book(code)





