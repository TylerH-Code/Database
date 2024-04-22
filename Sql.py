import mysql.connector
import os


def execute(query_string):
    # Establish a connection to the MySQL database
    conn = mysql.connector.connect(
        user='root', password=os.environ["PASSWORD"],
        host='127.0.0.1',
        database='accounts')
    
    # Create a cursor to execute the query
    cursor = conn.cursor()
    cursor.execute(query_string)
    
    # Fetch all rows from the result set
    rows = []
    for col in cursor:
        rows.append(col)
    
    # Close the cursor and connection
    cursor.close()
    conn.close()
    
    # Return the resulting rows
    return rows


def retreive(query_string):
    # Establish a connection to the MySQL database
    conn = mysql.connector.connect(
        user='root', password=os.environ["PASSWORD"],
        host='127.0.0.1',
        database='accounts')
    
    # Create a cursor to execute the query
    cursor = conn.cursor()
    cursor.execute(query_string)
    
    # Commit the changes to the database
    conn.commit()
    
    # Close the cursor and connection
    cursor.close()
    conn.close()