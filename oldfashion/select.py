# setup intellij with python
# https://www.youtube.com/watch?v=OV6k33GH2Vk

# DB Connection SQLite3

import sqlite3

# Open DB, If it doesn't exist, create a new one.
from sqlite3 import Cursor

conn = sqlite3.connect('db-oldfashion.db')

# Create a cursor
c = conn.cursor()

# Select a table

c.execute("select * from location")
print(c.fetchall())

conn.commit()
conn.close()


# seguir mirando https://www.youtube.com/watch?v=byHcYRpMgI4

