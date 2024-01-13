import mysql.connector

# connection with database
Info = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    db="movies"
)
cursor = Info.cursor()

def registerUser(data):
    try:
        cursor.execute('INSERT INTO `users` (`username`, `password`) VALUES (%s, %s)', data)
        Info.commit()
        return True
    except Exception as e:
        print(e)
        return False
    

def loginUser(data):
    try:
        cursor.execute('SELECT * FROM `users` WHERE `username` = %s AND `password` = %s', data)
        return cursor.fetchone()
    except Exception as e:
        print(e)
        return False