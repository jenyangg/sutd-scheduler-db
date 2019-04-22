"""
This is a util script that will help to move sqlite data to the algorithm
INPUTS: Course Name, Assigned Professors, Cohorts Involved, Location, Pillar, Number of Hours, Lesson Type
OUTPUTS: Course Name, Assigned Professors, Cohorts Involved , Location, Day, Start, End
"""
import sqlite3
import csv

class db_helper:
    
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = self.create_connection()
        self.cursor = self.conn.cursor()

    def read_db(self, sqlite):
        pass
    
    def print_all_columns(self,table_name):
        c = self.cursor
        #if "\" in 
        c.execute(f'SELECT * FROM {table_name}')
        print(list(map(lambda x: x[0], c.description)))

    def get_columns(self,list_of_columns,table_name):
        c = self.cursor
        a = ""
        for i in list_of_columns:
            a += i + ","
            print(i)
        a = a[0:len(a)-1]
        c.execute(f"SELECT {a} FROM {table_name}") 
        return c.fetchall()

    def make_input():
        pass

    def get_input():
        pass

    def create_connection(self):
        try:
            conn = sqlite3.connect(self.db_file)
            return conn
        except Error as e:
            print(e)
        return None

'''
dbh = db_helper("db.sqlite3")
a = dbh.get_columns(["id","title","assigned_professors","class_related","location","pillar","duration","type"],"users_class")
print(a)
'''

