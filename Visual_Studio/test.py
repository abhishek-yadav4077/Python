import psycopg2
def table():
    conn = psycopg2.connect(dbname = "postgres", user = "postgres", password="Yadav@2005", host = "localhost", port = "5432")

    cursor = conn.cursor()   #to see vertical line blinking
    cursor.execute('''create table employees(Name Text, ID int, Age int);''')  # to execute the command lines inside triple quotes, BASICALLY syntax of STRUCTURED QUERY LANGUAGE (SQL) inside triple quotes, ... inside those quotes we have basically QUERY
    print('Table created successfully')

    conn.commit() #to commit the changes
    conn.close()

def data():
    conn = psycopg2.connect(dbname = "postgres", user = "postgres", password="Yadav@2005", host = "localhost", port = "5432")

    cursor = conn.cursor() 

    name = input('Enter name: ')
    id = input('Enter id: ') 
    age = input('Enter age: ') 
    query = '''insert into employees(Name, ID, Age) values(%s, %s, %s);'''
    cursor.execute(query, (name, id, age))

    # cursor.execute('''insert into employees(Name, ID, Age) values('SAM', 01, 30);''') 
    print('Data added successfully')

    conn.commit() 
    conn.close()


def extract():
    conn = psycopg2.connect(dbname = "postgres", user = "postgres", password="Yadav@2005", host = "localhost", port = "5432")

    cursor = conn.cursor() 

    cursor.execute('''select * from employees;''') 
    show = cursor.fetchone()
    print(show[0])
    # print('Data added successfully')

    conn.commit() 
    conn.close()

data()



