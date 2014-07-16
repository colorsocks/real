# Create SQL database and table

# inmport the sqllite lib
import sqlite3

# create a new database if the database doesn't already exist
conn = sqlite3.connect("new.db")

# get a cursor object used to execute SQL commands
cursor = conn.cursor()

# create a table
cursor.execute("""CREATE TABLE population(city TEXT, state TEXT, population INT)""")

# close the datebase connection

conn.close()