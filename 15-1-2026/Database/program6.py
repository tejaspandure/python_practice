import mysql.connector



def main():

    config = {
        'user' : 'root',
        'password' : 'Tejas@8358',
        'host' : 'localhost',
        'port' : 3306
    }


    try:
        dConnection = mysql.connector.connect(**config)

        if(dConnection.is_connected()):
            print("database connected successfully")
            print("\n")

    except Exception as eobj:
        print("unable to connect to database due to : ",eobj)


    cobj= dConnection.cursor()
    sql = 'show databases'
    cobj.execute(sql)
    for iCnt in cobj:
        print(iCnt)

    cobj.close()
    dConnection.close()


if __name__ == "__main__":
    main()