# Team RV -- Vincent Lin and Rachel Ng
# SoftDev1 pd7
# K16 -- No Trouble    or Treble
# 2018-10-04

# python db_builder.py; sqlite3 rv.db
# SELECT * FROM courses;
# SELECT * FROM peeps;

import sqlite3 # control sqlite db
import csv # csv I/O

import os
if os.path.isfile("rv.db"): # removes rv.db if it exists so we don't get 
    os.remove("rv.db") # 'sqlite3.OperationalError: table courses already exists'
else:
    pass # doesn't do anything if rv.db doesn't exist


pri = False

def p(nt): # turn printing messages on and off (diagnostics)
    if pri == True: 
        print (nt)


DB_FILE = "rv.db"

db = sqlite3.connect(DB_FILE) # opens or makes the file
c = db.cursor() 


# opens courses.csv and makes a dictionary (courses)
csv1 = open('courses.csv', 'r')
courses = csv.DictReader(csv1)

# opens peeps.csv and makes a dictionary (peeps)
csv2 = open('peeps.csv', 'r')
peeps = csv.DictReader(csv2)

# makes courses table in rv.db
command = "CREATE TABLE courses (code TEXT, id INTEGER, mark INTEGER);"
p("\n" + command) 
c.execute(command)

for row in courses: # adds code, id, and mark to courses
    adding = "INSERT INTO courses VALUES ('" + row['code'] + "', " + row['id'] + ", " + row['mark'] + ");"
    p(adding)
    c.execute(adding)

# makes peeps table in rv.db
command = "CREATE TABLE peeps (name TEXT, id INTEGER, age INTEGER);"
p("\n" + command)
c.execute(command)

for row in peeps: # adds name, id, and age to peeps
    adding = "INSERT INTO peeps VALUES ('" + row['name'] + "', " + row['id'] + ", " + row['age'] + ");"
    p(adding)
    c.execute(adding)


db.commit() # saves changes
db.close() # closes db


