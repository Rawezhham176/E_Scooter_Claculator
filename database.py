import mysql.connector

def connect_databse():
    global mydb
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Dracula$&*12345"
    )
    global mycursor
    mycursor = mydb.cursor()


def show_databses():
    sql = "SHOW DATABASES"
    mycursor.execute(sql)
    for x in mycursor:
        print(x)


def create_databse(name):
    sql = "CREATE DATABSE {}"
    mycursor.execute(sql.format(name))


def create_table(name):
    sql = "CREATE TABLE {} (price int, destination int)"
    mycursor.execute(sql.format(name))

def alter_table(tableName, columnName):
    sql = "ALTER TABLE {} ADD COLUMN {} int"
    mycursor.execute(sql.format(tableName, columnName))
    mydb.commit()

def show_tables():
    sql = "SHOW TABLES"
    mycursor.execute(sql)

def select_from_table(name):
    sql = "SELECT * FROM {}"
    mycursor.execute(sql.format(name))
    results = mycursor.fetchall()
    for x in results:
        print(x)

def insert_table_employee(id, name, birthday, employeeNumber, password):
    sql = "INSERT INTO employee (id, name, birthday, employeeNumber, password) values (%s, %s)"
    values = (id, name, birthday, employeeNumber, password)
    mycursor.execute(sql.format(name), values)
    mydb.commit()




