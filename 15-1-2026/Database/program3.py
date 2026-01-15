import mysql.connector

try:
    connection = mysql.connector.connect(user='root',
                                        password='Tejas@8358',
                                        host='localhost',
                                        database='spartan',
                                        port = 3306)
    print("Connected successfully !!!")
except Exception as obj1:
    print('unable to connect due to: ',obj1)


