import mysql.connector
import os


def execute(query_string):
    conn = mysql.connector.connect(
        user='root', password=os.environ["PASSWORD"],
        host='127.0.0.1',
        database='accounts')
    cursor = conn.cursor()
    cursor.execute(query_string)
    rows = []
    for col in cursor:
        rows.append(col)
    cursor.close()
    conn.close()
    return rows


def retreive(query_string):
    conn = mysql.connector.connect(
        user='root', password=os.environ["PASSWORD"],
        host='127.0.0.1',
        database='accounts')
    cursor = conn.cursor()
    cursor.execute(query_string)
    conn.commit()
    cursor.close()
    conn.close()
