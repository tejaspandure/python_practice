import mysql.connector

def connection_db():
    print("\n")
    print("---------------------------------------------")
    print("-------------connection of db----------------")
    print("---------------------------------------------")

    config = {
        'user' : 'root',
        'password' : 'Tejas@8358',
        'host' : 'localhost',
        'port' : 3306

    }
    try:
        connection = mysql.connector.connect(**config)

        if connection.is_connected():

            print("database connected")
            print("\n")
            return connection
        
        else:
            print("not connected")

    except Exception as eobj:
        print("Unable to connect due to : ",eobj)

    

def create_database(connection,dName):
    print("\n")
    print("---------------------------------------------")
    print("-------------creating the db----------------")
    print("---------------------------------------------")

    try:
        cobj = connection.cursor()
        sql = f'create database if not exists {dName}'
        cobj.execute(sql)
        print("databse created successfully ")
    except Exception as eobj:
        print("unable to create database: ",eobj)

def show_databases(connection):
    print("\n")
    print("---------------------------------------------")
    print("-------------showing the db----------------")
    print("---------------------------------------------")

    try:
        cobj = connection.cursor()
        sql = f'show databases'
        cobj.execute(sql)
        for iCnt in cobj:
            print(iCnt)

    except Exception as eobj:
        print("unable to show databases due to : ",eobj)

def create_table(connection,dName):
    print("\n")
    print("---------------------------------------------")
    print("-------------creating table into db----------------")
    print("---------------------------------------------")

    try:
        connection.database = dName
        cobj = connection.cursor()
        sql = """
                create table if not exists students(
                id INT Auto_INCREMENT PRIMARY KEY,
                name VARCHAR(50),
                fees INT)

                """
        cobj.execute(sql)
        print("Table student is crated successfully: \n")

    except Exception as eobj:
        print("unable to create database due to : ",eobj)




def main():
    connection = connection_db()
    if connection is None:
        return
    
    create_database(connection,'spartan')
    show_databases(connection)

    create_table(connection,'spartan')


    connection.close()
    print("connection closed successfully")


if __name__ == "__main__":
    main()