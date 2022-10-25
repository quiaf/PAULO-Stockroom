import sqlite3
# Definicion de clases

class Person:
    def __init__(self, name, last_name, mobile, dni, role):
        self.name = name
        self.last_name = last_name
        self.mobile = mobile
        self.dni = dni
        self.role = role


class Manager(Person):
    pass


class Owner(Person):
    pass

    def ShowManager():
        conn = sqlite3.connect('db-oldfashionv2.db')
        c = conn.cursor()
        c.execute('SELECT * FROM manager')
        print(c.fetchall())
        conn.commit()
        conn.close()

Owner.ShowManager()
