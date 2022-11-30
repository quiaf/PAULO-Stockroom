# DB Connection SQLite3

import sqlite3

# Open DB, If it doesn't exist, create a new one.
conn = sqlite3.connect('db-oldfashionv2.db')

# Create a cursor
c = conn.cursor()


# Drop all tables if they exists, then we will recreate them.
# DROP TABLE IF EXISTS schema-name . table-name

c.execute("""
DROP TABLE IF EXISTS DEVICE
""")
conn.commit()

c.execute("""
DROP TABLE IF EXISTS STOCKROOM
""")
conn.commit()

c.execute("""
DROP TABLE IF EXISTS OWNER
""")
conn.commit()

c.execute("""
DROP TABLE IF EXISTS MANAGER
""")
conn.commit()

c.execute("""
DROP TABLE IF EXISTS DEVICEINSTOCK
""")
conn.commit()

# Create a table
c.execute("""
CREATE TABLE DEVICE (
	ID INT PRIMARY KEY,
	MODEL VARCHAR_IGNORECASE(255) NOT NULL,
	MANUFACTURER VARCHAR_IGNORECASE(255) NOT NULL,
	ATYPE VARCHAR_IGNORECASE(255) NOT NULL)
""")
conn.commit()

c.execute("""
CREATE TABLE STOCKROOM (
	ID INT PRIMARY KEY,
	NAME VARCHAR_IGNORECASE(255) NOT NULL,
	ADDRESS VARCHAR_IGNORECASE(255) NOT NULL,
	MANAGER_DNI INTEGER NOT NULL,
	COUNTRY VARCHAR_IGNORECASE(255) NOT NULL,
	STATE VARCHAR_IGNORECASE(255) NOT NULL,
	NEIGHBORHOOD VARCHAR_IGNORECASE(255) NOT NULL,
	CONSTRAINT STOCKROOM_FK FOREIGN KEY (MANAGER_DNI) REFERENCES MANAGER(DNI))
""")
conn.commit()

c.execute("""
CREATE TABLE OWNER (
	NAME VARCHAR_IGNORECASE(255) NOT NULL,
	LAST_NAME VARCHAR_IGNORECASE(255) NOT NULL,
	MOBILE INTEGER NOT NULL,
	DNI INTEGER NOT NULL,
	CONSTRAINT PERSON_PK PRIMARY KEY (DNI))
""")
conn.commit()

c.execute("""
CREATE TABLE MANAGER (
	NAME VARCHAR_IGNORECASE(255) NOT NULL,
	LAST_NAME VARCHAR_IGNORECASE(255) NOT NULL,
	MOBILE INTEGER NOT NULL,
	DNI INTEGER NOT NULL,
	CONSTRAINT PERSON_PK PRIMARY KEY (DNI))
""")
conn.commit()

c.execute("""
CREATE TABLE DEVICEINSTOCK (
	ID INT PRIMARY KEY,
	QUANTITY INTEGER NOT NULL,
	STOCKROOM VARCHAR_IGNORECASE(32) NOT NULL,
	DEVICE VARCHAR_IGNORECASE(32) NOT NULL)
""")
conn.commit()

# Insert data

# Insert into Owner - Name/LastName/Mobile/DNI
c.execute("INSERT INTO owner VALUES ('Pepe', 'Argento', '1162234545','12000001')")
conn.commit()

# Select to test previous insert
c.execute("select * from owner")
print(c.fetchall())
conn.commit()

# Insert into Manager - Name/LastName/Mobile/DNI
c.execute("INSERT INTO manager VALUES ('Bart', 'Simpson', '1131199545','33000003')")
conn.commit()

c.execute("INSERT INTO manager VALUES ('Homero', 'Zinmson', '1145556666','44000004')")
conn.commit()

# Select to test previous insert
c.execute("select * from manager")
print(c.fetchall())
conn.commit()

# Insert into Device - ID/Model/Manufacturer/Atype
c.execute("INSERT INTO device VALUES ('1', 'A1', 'Samsung', 'Cable')")
conn.commit()

c.execute("INSERT INTO device VALUES ('2', 'A1', 'Samsung', 'Skin')")
conn.commit()

c.execute("INSERT INTO device VALUES ('3', 'i11', 'Apple', 'Cable')")
conn.commit()

c.execute("INSERT INTO device VALUES ('4', 'i11', 'Apple', 'Skin')")
conn.commit()

# Select to test previous insert
c.execute("select * from device")
print(c.fetchall())
conn.commit()

# Insert into stockroom - ID/Name/Address/ManagerDNI/Country/State/Neighborhood
c.execute("INSERT INTO stockroom VALUES ('1', 'TodoCel', 'Loyola150', '33000003', 'Argentina', 'CABA', 'VillaCrespo')")
conn.commit()
c.execute("INSERT INTO stockroom VALUES ('2', 'TutuCel', 'Lavalle2543', '44000004', 'Argentina', 'CABA', 'ElEleven')")
conn.commit()

# Select to test previous insert
c.execute("select * from stockroom")
print(c.fetchall())
conn.commit()

conn.close()
