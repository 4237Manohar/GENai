import sqlite3

## Connectt to SQlite
connection=sqlite3.connect("student_db")

# Create a cursor object to insert record,create table

cursor=connection.cursor()

## create the table
table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT);

"""
cursor.execute(table_info)

## Insert Some more records

cursor.execute('''Insert Into STUDENT values('Ajay','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Manohar','Data Science','B',100)''')
cursor.execute('''Insert Into STUDENT values('Nikhil','Blockchain','A',87)''')
cursor.execute('''Insert Into STUDENT values('Sohel','DEVOPS','B',52)''')
cursor.execute('''Insert Into STUDENT values('Deva','DEVOPS','A',48)''')

## Disspaly ALl the records

print("The isnerted records are")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

## Commit your changes int he databse
connection.commit()
connection.close()