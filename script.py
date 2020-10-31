#pip3 install mysql-connector-python or pip install mysql-connector-python-rf
import mysql.connector

'''
this function will require hostname, username, password and database name as argument
'''

def sqlfunc(host,user,password,database):
    # connecting to database
    try:
        # enter your credentials
        db = mysql.connector.connect(
        host="localhost",
        user="yourusername",
        password="yourpassword",
        database="mydatabase"
        )
        print("Connection to DB successful.")
    except Exception as e:
        print(f"Can't connect to DB due to {e}")
        raise e
    cursor = db.cursor()
    try:
        # enter your query
        query = "SELECT * FROM mytable"
        cursor.execute(query) 
        result = cursor.fetchall()
    except Exception as e:
        print(f"Can't execute query due to {e}")
        raise e
    return result

