#create connections

import mysql.connector

def main():
    print("use configuration seperately")
    config = {
            'user' : 'root',
            'password' : 'Tejas@8358',
            'host' : 'localhost',
            'database': 'spartan',
            'port': 3306
        }
    
    try:
        connection = mysql.connector.connect(**config)
        if connection.is_connected():
            print("Connected successfully !!")
            #print("server version: ",connection.get_server_info())

    except Exception as obj1:
        print('unable to connect due to: ',obj1)

    print("Before close: ",connection.is_connected())
    connection.close()  
    print("Successfully closded")
    print("after connection: ",connection.is_connected())


if __name__ == "__main__":
    main()