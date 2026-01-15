#create database
#show database

import mysql.connector

def main():

    #configuration of database
    config = {
        'user' : 'root',
        'password' : 'Tejas@8358',
        'host' : 'localhost',
        'port' : 3306
    }

    #connection of database
    try:
        connection = mysql.connector.connect(**config)

        if connection.is_connected():
            print("Connected successfully")
        else:
            print("not connected")
    
    except Exception as eobj:
        print("Unable to connect due to : ",eobj)

    #creating connection to cursor()
    MyConnection = connection.cursor()

    #creating database 
    sql = 'create database pdb'

    #executing database
    MyConnection.execute(sql)
    print("database created succeffully")





    MyConnection.close()
    connection.close()

if __name__=="__main__":
    main()