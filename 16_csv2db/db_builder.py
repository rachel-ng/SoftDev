# Team RV -- Vincent Lin and Rachel Ng
# SoftDev1 pd7
# K16 -- No Trouble    or Treble
# 2018-10-04

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O



pri = True

def p(nt): # turn printing messages on and off (diagnostics)
    if pri == True: 
        print (nt)

# rm rv.db; python db_builder.py; sqlite3 rv.db
# sqlite3 rv.db
# SELECT * FROM courses;
# SELECT * FROM peeps;



DB_FILE="rv.db"

db = sqlite3.connect(DB_FILE)
c = db.cursor()



# opens courses.csv and makes a dictionary
csv1 = open('courses.csv', 'r')
courses = csv.DictReader(csv1)
#for row in courses:
    # print (row)

# opens peeps.csv and makes a dictionary
csv2 = open('peeps.csv', 'r')
peeps = csv.DictReader(csv2)
#for row in peeps:
    # print(row)



# makes courses table in rv.db
command = "CREATE TABLE courses (code TEXT, id INTEGER, mark INTEGER);"
p("\n" + command) 
c.execute(command)

for row in courses: # adds code, id, and mark
    adding = "INSERT INTO courses VALUES ('" + row['code'] + "', " + row['id'] + ", " + row['mark'] + ");"
    p(adding)
    c.execute(adding)

# makes peeps table in rv.db
command = "CREATE TABLE peeps (name TEXT, id INTEGER, age INTEGER);"
p("\n" + command)
c.execute(command)

for row in peeps: # adds name, id, and age
    adding = "INSERT INTO peeps VALUES ('" + row['name'] + "', " + row['id'] + ", " + row['age'] + ");"
    p(adding)
    c.execute(adding)

db.commit()
db.close()


