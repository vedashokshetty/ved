
import
import subprocess

# This will install terminaltables.
try:
    import terminaltables as tt
except ImportError:
    subprocess.run(["pip", "install", "terminaltables"])
    import terminaltables as tt

# Connecting to the database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="dpsbn"
)

if (not db.is_connected()):
    print("ERROR CONNECTING TO DATABASE")

cursor = db.cursor()


def createDatabase():
    # Creates the database if it does not exist
    cursor.execute("create database if not exists emplmanagementdb")


def createTable():
    # Creates the tables if they do not exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS EMP (
            ID CHAR(4) PRIMARY KEY,
            NAME VARCHAR(200) NOT NULL,
            JOB VARCHAR(100),
            JOB_DESCRIPTION VARCHAR(1000),
            LOCATION CHAR(3) NOT NULL DEFAULT "BLR",
            SALARY INT CHECK( SALARY > 0 )
        )
        """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS TASKS (
            ID CHAR(4) NOT NULL,
            TASK VARCHAR(1000),
            ASSIGNED_BY VARCHAR(255),
            FOREIGN KEY (ID) REFERENCES EMP(ID) 
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS MEDICAL (
            ID CHAR(4) NOT NULL,
            MEDICAL_CONDITION VARCHAR(100),
            TREATMENT_GIVEN VARCHAR(255),
            DOCTOR VARCHAR(255) NOT NULL,
            FOREIGN KEY (ID) REFERENCES EMP(ID)
        )
    """)


def selectDatabase():
    # Use the database
    cursor.execute("use emplmanagementdb")


def insertDefaultValues():
    # Inserts some default values incase the table does not have any values

    # Default values for emp
    cursor.execute("""
    INSERT INTO emp (ID, NAME, JOB, JOB_DESCRIPTION, LOCATION, SALARY)
    VALUES
    ('E001', 'Rajesh Patel', 'Manager', 'Manages the team', 'Mum', 75000),
    ('E002', 'Priya Sharma', 'Developer', 'Develops new software', 'Del', 80000),
    ('E003', 'Vikram Singh', 'Salesperson', 'Sells products', 'Blr', 65000),
    ('E004', 'Nisha Patel', 'Designer', 'Designs graphics and layouts', 'Che', 70000),
    ('E005', 'Anil Kumar', 'Accountant', 'Manages financial records', 'Mum', 65000),
    ('E006', 'Sonia Gandhi', 'HR Manager', 'Manages human resources', 'Del', 75000),
    ('E007', 'Amit Shah', 'Marketing Manager', 'Manages marketing campaigns', 'Blr', 80000),
    ('E008', 'Rajesh Kumar', 'Content Writer', 'Writes website content', 'Che', 65000),
    ('E009', 'Pooja Sharma', 'IT Manager', 'Manages the IT department', 'Mum', 75000),
    ('E010', 'Vikas Singh', 'Project Manager', 'Manages projects', 'Del', 80000)
    """)

    # Default values for tasks
    cursor.execute("""
    INSERT INTO Tasks (id, task, assigned_by)
    VALUES
    ('E001', 'Handle new team', 'HR DEPARTMENT'),
    ('E001', 'Instruct new joinees to follow protocol', 'MEDICAL DEPARTMENT'),
    ('E003', 'Create ad for company', 'HR DEPARTMENT'),
    ('E003', 'Presentation on sales', 'HR DEPARTMENT'),
    ('E002', 'Create new user interface', 'MEDICAL DEPARTMENT'),
    ('E009', 'Send PPT to admin room next week', 'ADMIN'),
    ('E006', 'Create new rule list', 'HR DEPARTMENT'),
    ('E009', 'Teach interns about company software', 'ADMISSIONS DEPARTMENT'),
    ('E005', 'Calculate balance sheet', 'ADMISSIONS DEPARTMENT'),
    ('E010', 'Last week project not yet recieved, need tomorrow without fail', 'ADMIN')
    """)

    # Default values for medical
    cursor.execute("""

    INSERT INTO MEDICAL (id, medical_condition, treatment_given, doctor)
    VALUES
    ('E001', 'Flu', 'Antibiotics', 'Dr. Sharma'),
    ('E002', 'Cold', 'Painkillers', 'Dr. Patel'),
    ('E001', 'Allergy', 'Antihistamines', 'Dr. Kumar'),
    ('E005', 'Gastroenteritis', 'Rehydration solution', 'Dr. Gandhi'),
    ('E009', 'Headache', 'Ibuprofen', 'Dr. Shah'),
    ('E010', 'Back pain', 'Ibuprofen', 'Dr. Patel'),
    ('E007', 'Sore throat', 'Painkillers', 'Dr. Kumar'),
    ('E005', 'Ear infection', 'Antibiotics', 'Dr. Gandhi'),
    ('E003', 'Toothache', 'Painkillers', 'Dr. Shah'),
    ('E010', 'Sprain', 'Painkillers', 'Dr. Patel')
    """)

    db.commit()


def getColumns(table):
    # Gets the names of all columns of a table and puts it in a list.
    cursor.execute("desc " + table)
    allColumns = cursor.fetchall()
    columns = []
    for column in allColumns:
        columns.append(column[0])
    return columns


def getAllEmployees():
    # Get all employees in a table
    cursor.execute("select * from emp")
    results = cursor.fetchall()

    tableLayout = [
        getColumns('emp'),
    ]

    for row in results:
        tableLayout.append(row)

    allempltable = tt.DoubleTable(tableLayout)
    print(allempltable.table)


def addEmployee():
    # Add an employee to the table
    id = input("Enter id\n")
    name = input("Enter name\n")
    job = input("Enter job\n")
    jobdescription = input("Enter job description\n")
    location = input("Enter location\n")
    salary = int(input("Enter salary\n"))

    cursor.execute(
        "insert into emp values ('" + id + "','" + name + "','" + job + "','" + jobdescription + "','" + location + "','" + str(
            salary) + "')")
    db.commit()
    cursor.fetchall()


def removeEmployee():
    # Remove an employee based on their ID
    id = input("Enter employee id of employee to remove\n")
    cursor.execute("delete from emp where id = '" + id + "'")
    db.commit()
    print("Employee was removed")


def removeAll(table):
    # Remove all rows from a table
    cursor.execute("delete from " + table)
    db.commit()
    print("All values removed from", table)


def increaseSalary():
    # Increase the salary of an employee
    id = input("Enter the id of the employee whose salary you want to update\n")
    salary = input("How much would you like to increase the salary by\n")
    cursor.execute('update emp set salary = salary + ' + salary + ' where id = "' + id + '"')
    print("Updated salary")


def decreaseSalary():
    # Decrease the salary of an employee
    id = input("Enter the id of the employee whose salary you want to update\n")
    salary = input("How much would you like to decrease the salary by\n")
    cursor.execute('update emp set salary = salary - ' + salary + ' where id = "' + id + '"')
    print("Updated salary")


def changeLocation():
    # Change the location of an employee
    id = input("Enter id of the employee")
    location = input("Enter new location")
    location = location[:3].upper()  # Makes it only the first 3 characters and converts it to uppercase
    cursor.execute("update emp set location = '" + location + "' where id = '" + id + "'")
    print("Location changed to", location)


def showTasks():
    # Show all tasks from the tasks table
    cursor.execute("select * from tasks")
    tasks = cursor.fetchall()

    taskLayout = [
        getColumns('tasks'),
    ]

    for task in tasks:
        taskLayout.append(task)

    allTasks = tt.DoubleTable(taskLayout)
    print(allTasks.table)


def showTasksForSpecificEmployee():
    # Show all tasks from the tasks table where the employee id matches
    id = input("Enter employee id\n")
    cursor.execute("select * from tasks where id = '" + id + "'")
    tasks = cursor.fetchall()

    taskLayout = [
        getColumns('tasks'),
    ]

    for task in tasks:
        taskLayout.append(task)

    allTasks = tt.DoubleTable(taskLayout)
    print(allTasks.table)


def createTask():
    # Create a new task
    id = input("Enter id of employee\n")
    task = input("What is the task?\n")
    assignedby = input("Who is assigning the task?\n")
    cursor.execute("insert into tasks values ( '" + id + "','" + task + "','" + assignedby + "' )")
    print("Task created")


def removeTask():
    # Remove a task
    id = input("Enter id of employee\n")
    assignedby = input("Who assigned the task?\n")
    cursor.execute("delete from tasks where id = '" + id + "' and assigned_by = '" + assignedby + "'")
    print("Task removed")


def showTasksByAssigner():
    # Show tasks grouped by assigner
    cursor.execute("select distinct assigned_by from tasks")
    assigners = cursor.fetchall()
    taskLayout = [
        ["All tasks by assigner"],
    ]
    for assigner in assigners:
        taskLayout.extend([[], assigner, []])
        cursor.execute("select task from tasks where assigned_by = '" + assigner[0] + "'")
        tasks = cursor.fetchall()
        for task in tasks:
            taskLayout.append(task)
    tasktable = tt.DoubleTable(taskLayout)
    print(tasktable.table)


def seeAllMedicalRecords():
    # Show all medical records
    cursor.execute("select * from medical")
    records = cursor.fetchall()
    medicalLayout = [
        ["All medical records"],
        getColumns("medical")
    ]
    for record in records:
        medicalLayout.append(record)
    medicalTable = tt.DoubleTable(medicalLayout)
    print(medicalTable.table)


def seeMedicalRecordsForEmployee():
    # Show all medical records for a specific employee
    id = input("Enter id of employee\n")
    cursor.execute("select * from medical where id = '" + id + "'")
    records = cursor.fetchall()
    medicalLayout = [
        ["All medical records for " + id],
        getColumns("medical")
    ]
    for record in records:
        medicalLayout.append(record)
    medicalTable = tt.DoubleTable(medicalLayout)
    print(medicalTable.table)


def seeTreatmentsByDoctor():
    # Show medical history grouped by doctor
    cursor.execute("select distinct doctor from medical")
    doctors = cursor.fetchall()
    medicalLayout = [
        ["MEDICAL CONDITION", 'TREATMENT']
    ]
    for doctor in doctors:
        medicalLayout.extend([[], list(doctor), []])
        cursor.execute("select medical_condition, treatment_given from medical where doctor = '" + doctor[0] + "'")
        records = cursor.fetchall()
        for record in records:
            medicalLayout.append(list(record))
    medicaltable = tt.DoubleTable(medicalLayout)
    commandtable.inner_column_border = False
    commandtable.inner_row_border = False
    print(medicaltable.table)


def seeMedicalRecordsOnCondition():
    # Show medical history where condition matches
    conditions = input("Enter the medical condition\n")
    cursor.execute("select * from medical where medical_condition = '" + condition + "'")
    medicalLayout = [
        ["All records for condition " + condition],
        getColumns("medical")
    ]
    for condition in conditions:
        medicalLayout.append(condition)
    medicaltable = tt.DoubleTable(medicalLayout)
    print(medicaltable.table)


def createMedicalRecord():
    # Creates a medical record
    id = input("Enter employee id\n")
    medicalCondition = input("Enter medical condition\n")
    treatmentGiven = input("Enter treatment given\n")
    doctor = input("Enter name of doctor\n")
    cursor.execute("insert into medical values ( '" + id + "','" + medicalCondition,
                   + "','" + treatmentGiven + "','" + doctor + "' )")
    print("Created medical record")


def removeMedicalRecord():
    # Removes a medical record
    id = input("Enter employee id\n")
    medicalCondition = input("Enter medical condition\n")
    cursor.execute("delete from medical where medical_condition = '" + medicalCondition + "' and id = '" + id + "'")
    print("Removed medical record")


commandlist = (
    ["ALL COMMANDS:"],
    [''],
    ["EMPLOYEE MANAGER"],
    [''],
    ["1:", "Show all employees"],
    ["2:", "Add an employee"],
    ["3:", "Remove an employee"],
    ["4:", "Remove all employees"],
    ["5:", "Increase salary"],
    ["6:", "Decrease salary"],
    ["7:", "Change location"],
    [''],
    ["EMPLOYEE TASK MANAGER"],
    [''],
    ["8:", "Show all tasks"],
    ["9:", "Create new task"],
    ["10:", "Remove task"],
    ["11:", "Remove all tasks"],
    ["12:", "Show task for specific employee"],
    ["13:", "Show all tasks based on task assigner"],
    [''],
    ["EMPLOYEE MEDICAL HISTORY"],
    [''],
    ["14:", "See all recent medical records"],
    ["15:", "See medical records of a specific employee"],
    ["16:", "See all treatments grouped by doctors"],
    ["17:", "See medical records based on condition"],
    ["18:", "Create new medical record"],
    ["19:", "Remove medical record"],
    [''],
    ["20:", "Exit"],
    ['Enter a command number to execute the function.']
)

commandtable = tt.DoubleTable(commandlist)
commandtable.inner_column_border = False
commandtable.inner_row_border = False
commandtable.inner_footing_row_border = True

# MAIN CODE

createDatabase()
selectDatabase()

# Only run if you want to remove all the data everytime you start
removeAll('tasks')
removeAll('medical')
removeAll('emp')

# Only run if table is not yet created
createTable()
# Only run if there are no values in the table
insertDefaultValues()

# MAIN LOOP

while True:

    print("Welcome to the advanced-tek employee management system!")

    print(commandtable.table)

    command = int(input("Enter a command\n> "))

    if command > 20 or command < 1:
        print("invalid command")
        continue

    if command == 1:
        getAllEmployees()
    elif command == 2:
        addEmployee()
    elif command == 3:
        removeEmployee()
    elif command == 4:
        removeAll('emp')
    elif command == 5:
        increaseSalary()
    elif command == 6:
        decreaseSalary()
    elif command == 7:
        changeLocation()
    elif command == 8:
        showTasks()
    elif command == 9:
        createTask()
    elif command == 10:
        removeTask()
    elif command == 11:
        removeAll('tasks')
    elif command == 12:
        showTasksForSpecificEmployee()
    elif command == 13:
        showTasksByAssigner()
    elif command == 14:
        seeAllMedicalRecords()
    elif command == 15:
        seeMedicalRecordsForEmployee()
    elif command == 16:
        seeTreatmentsByDoctor()
    elif command == 17:
        seeMedicalRecordsOnCondition()
    elif command == 18:
        createMedicalRecord()
    elif command == 19:
        removeMedicalRecord()
    elif command == 20:
        exit(






