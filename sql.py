# sql.py - Create a SQLite3 table and populate it with data
import sqlite3

# create a new database if the database doesn't already exist
with sqlite3.connect('sample.db') as connection:

    # get a cursor object used to execute SQL commands
    c = connection.cursor()

    # delete existing table since id and author_id columns are missing
    # modified on 07/10/2014 SUHAN
    c.execute('DROP TABLE IF EXISTS posts')

    # create the table
    c.execute('CREATE TABLE posts(id INTEGER, title TEXT, description TEXT, author_id INTEGER)')

    # insert dummy data into the table
    c.execute('INSERT INTO posts VALUES(1, "Good", "I\'m good.", 1001)')
    c.execute('INSERT INTO posts VALUES(2, "Well", "I\'m well.", 1002)')
    c.execute('INSERT INTO posts VALUES(3, "Excellent", "I\'m excellent.", 1003)')
    c.execute('INSERT INTO posts VALUES(4, "Okay", "I\'m okay.", 1004)')

# Save (commit) the changes
connection.commit()