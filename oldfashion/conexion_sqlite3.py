# DB Connection SQLite3

import sqlite3

# Open DB, If it doesn't exist, create a new one.
conn = sqlite3.connect('db-oldfashion.db')

# Create a cursor
c = conn.cursor()

# Create a table

c.execute("""CREATE TABLE location (
    country varchar(255),
    state varchar(255),
    neighborhood varchar(255)
)""");

c.execute("""CREATE TABLE device (
    model varchar(255),
    manufacturer varchar(255),
    atype varchar(255)
)""");

c.execute("""CREATE TABLE stockroom (
    name varchar(255),
    address varchar(255)
)""");

c.execute("""CREATE TABLE person (
    name varchar(255),
    last_name varchar(255),
    mobile int,
    dni int,
    password varchar(255),
    role varchar(255)
)""");

c.execute("""CREATE TABLE devicestockroom (
    quantity int,
    stockroom varchar(255),
    device varchar(255)
)""");

# seguir mirando https://www.youtube.com/watch?v=byHcYRpMgI4

