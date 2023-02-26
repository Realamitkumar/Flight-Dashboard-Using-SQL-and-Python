# BASICS How can work with SQL
# Using Python

import mysql.connector

# connect to the database server
try :
    conn = mysql.connector.connect(
    host = '127.0.0.1',
    user='root',
    password = '2180@amit',
    database = 'indigo')
    
    mycursor = conn.cursor()
    print("connection established")
except:
    print("Connection error")

# create a database on the db server
#mycursor.execute("CREATE DATABASE indigo")
#conn.commit()

# Create a table
# airport -> airport_id | code | name

#mycursor.execute("""
#CREATE TABLE airport(
#    aiport_id INTEGER PRIMARY KEY,
#    code VARCHAR(10) NOT NULL,
#    city VARCHAR(50) NOT NULL,
#    name VARCHAR(255) NOT NULL        
#)
#""")
#conn.commit()


# Insert data into table

#mycursor.execute("""
#    INSERT INTO airport VALUES
#    (1,'DEL','New Del','IGIA'),
#    (2,'CCU','Kolkata','NSCA'),
#    (3,'BOM','Mumbai','CSMA')
#""")
#conn.commit()

# search / retrieve
mycursor.execute('SELECT * FROM airport WHERE aiport_id > 1')
data = mycursor.fetchall() # fetchall(): for mutiple rows 
print(data)

for i in data:
    print(i[3])

# Update

#mycursor.execute("""
#UPDATE airport
#SET city = 'Bombay'
#WHERE aiport_id = 3
#""")
#conn.commit()

mycursor.execute("SELECT * FROM airport")
data = mycursor.fetchall()
print(data)

# Delete 

#mycursor.execute("DELETE FROM airport WHERE aiport_id = 3")
#conn.commit()

mycursor.execute("SELECT * FROM airport")
data = mycursor.fetchall()
print(data)
