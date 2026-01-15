import mysql.connector

connection = mysql.connector.connect(user='root',
                                     password='Tejas@8358',
                                     host='localhost',
                                     database='spartan',
                                     port = 3306)

print("connected !!")
