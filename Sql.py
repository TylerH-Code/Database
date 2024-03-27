from mysql.connector import connection
import os
conn = connection.MySQLConnection(
    user='root', password=os.environ["PASSWORD"],
    host='127.0.0.1',
    database='accounts')


def exucute(query_string):
    cursor=conn.cursor()
    cursor.execute(query_string)
    temp=[]
    for user in cursor:
        temp.append(user)
    cursor.close()
    conn.close()
    return temp
