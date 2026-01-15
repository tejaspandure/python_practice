import mysql.connector

def create_connection():

    config = {
        'user' : 'root',
        'password' : 'Tejas@8358',
        'host': 'localhost',
        'port' : 3306 
    }

    try:
        connection = mysql.connector.connect(**config)
        
        if connection.is_connected():
            print("Database is connected succesffuly")
            return connection
        else:
            print("database is not connected")
    except Exception as eobj:
        print("Unable to connect due to : ",eobj)

def create_database(connection,dName):

    try:
        cobj = connection.cursor()
        sql = f'create database if not exists {dName}'
        cobj.execute(sql)
        print("database created successfully")

    except Exception as eobj:
        print("Unable to create database due to : ",eobj)

def show_database(connection):

    try:
        cobj = connection.cursor()
        sql = f'show databases'
        cobj.execute(sql)

        for iCnt in cobj:
            print(iCnt)

    except Exception as eobj:
        print("Unable to show databse due to : ",eobj)

def create_table(connection):
    try:
        connection.database = 'spartan'
        cobj=connection.cursor()

        cobj.execute('drop table if exists student')
        sql = """
                create table student(
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(50),
                fees DOUBLE)"""
        
        cobj.execute(sql)
        print("Table create successfully")
    
    except Exception as eobj:
        print("unable to create table due to : ",eobj)


def insert_data(connection,name,fees):
    try:
        connection.database = 'spartan'
        cobj=connection.cursor()

        sql='insert into student(name,fees) value(%s,%s)'
        value = (name,fees)

        cobj.execute(sql,value)
        connection.commit()
        
        print(f"data inserted successfully j=>{name},{fees} ")
        print("last row id : ",cobj.lastrowid)

    except Exception as cobj:
        print("Unable to insert data due to : ",cobj)

def show_data(connection):
    try:
        connection.database='spartan'
        cobj = connection.cursor()

        sql = 'select * from student'
        cobj.execute(sql)

        rows = cobj.fetchall()
        print("data from database ")

        for iCnt in rows:
            print(iCnt)

    
    except Exception as eobj:
        print("unable to show data from table due to : ",eobj)
    

def main():
    Connection = create_connection()

    if Connection is None:
        return 
    
    
    create_database(Connection,'spartan')
    show_database(Connection)
    create_table(Connection)

    insert_data(Connection,"Tejas",4500)
    insert_data(Connection,"Rajul",44000)
    insert_data(Connection,"Raj",23000)

    show_data(Connection)

    Connection.close()
    print("connection gets colsed successfully")

if __name__ == "__main__":
    main()