# Team Where's Perry? -- Puneet Johal, Rachel Ng
# SoftDev1 pd7
# K17 -- Average
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


pri = True

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
#p("\n" + command) 
c.execute(command)

for row in courses: # adds code, id, and mark to courses
    adding = "INSERT INTO courses VALUES ('" + row['code'] + "', " + row['id'] + ", " + row['mark'] + ");"
    #p(adding)
    c.execute(adding)

# makes peeps table in rv.db
command = "CREATE TABLE peeps (name TEXT, id INTEGER, age INTEGER);"
#p("\n" + command)
c.execute(command)

for row in peeps: # adds name, id, and age to peeps
    adding = "INSERT INTO peeps VALUES ('" + row['name'] + "', " + row['id'] + ", " + row['age'] + ");"
    #p(adding)
    c.execute(adding)



peeps_avg = {} # id : avg
peeps_grades = {} # id : list grades
peeps_names = {} # id : name

c.execute("SELECT name, id FROM peeps") # get ids from peeps
for student in c.fetchall(): # make dictionaries
    peeps_avg[student[1]] = [] # for avg
    peeps_grades[student[1]] = [] # for list of grades
    peeps_names[student[1]] = student[0] # id : name 
#p(peeps_avg)
#p(peeps_grades)
#p(peeps_names)
    
c.execute("SELECT id, mark FROM courses;") # get ids and grades from courses
for g in c.fetchall(): # add list of grades to peeps_grades
    peeps_grades[g[0]].append(g[1])
p(peeps_grades)

for s in peeps_grades:
    grade = 0.0
    div = 0
    for m in peeps_grades[s]:
        grade += m
        div += 1
    p(s)
    peeps_avg[s] = [grade / div, div] # [average, num classes]
    
p(peeps_avg)    
p(peeps_names)

for peep in peeps_names:
    print "student #" + str(peep) + ", " + peeps_names[peep] + ": " + str(peeps_avg[peep][0])
    
# makes peeps_avg table in rv.db
command = "CREATE TABLE peeps_avg (id INTEGER, avg INTEGER);"
p("\n" + command)
c.execute(command)

for peep in peeps_grades:
    p("peep")
    p(peep)
    adding = "INSERT INTO peeps_avg (" + str(peep) + ", " + str(peeps_avg[peep]) + ");"
    p(adding)
    c.execute(adding)


db.commit() # saves changes
db.close() # closes db


