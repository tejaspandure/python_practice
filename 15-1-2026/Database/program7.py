import mysql.connector


def connect_db():
    config = {
        'user' : 'root',
        'password' : 'Tejas@8358',
        'host' : 'localhost',
        'port' : 3306
    }

    try:
        connection = mysql.connector.connect(**config)

        if connection.is_connected():
            print("database connected successfully ")
            return connection
        
    except Exception as eobj:
        print("unable to connect due to : ",eobj)

def create_database(connection,db_name):
    try:
        cursor = connection.cursor()
        sql = f"create database if not exists {db_name}"
        cursor.execute(sql)
        print("databse created successfully \n")
    
    except Exception as eobj:
        print("Unable to create database: ",eobj)


def show_database(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("show databases")
        print('avalilable databases : \n')

        for iCnt in cursor:
            print(iCnt)
        print()

    except Exception as eobj:
        print("unable to fetch databse: ",eobj)


def main():
    Connection = connect_db()
    if Connection is None:
        return
    
    create_database(Connection,'spartan')
    show_database(Connection)

    Connection.close()
    print("connection close")

if __name__ == "__main__":
    main()