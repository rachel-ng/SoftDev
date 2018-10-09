# Team Where's Perry? -- Puneet Johal, Rachel Ng
# SoftDev1 pd7
# K17 -- Average
# 2018-10-04

# python stu_mean.py; sqlite3 rip.db
# SELECT * FROM courses;
# SELECT * FROM peeps;
# SELECT * FROM peeps_avg;


import sqlite3 # control sqlite db
import csv # csv I/O

import os
if os.path.isfile("rip.db"): # removes rip.db if it exists so we don't get 
    os.remove("rip.db") # 'sqlite3.OperationalError: table courses already exists'
else:
    pass # doesn't do anything if rip.db doesn't exist


pri = True

def p(nt): # turn printing messages on and off (diagnostics)
    if pri == True: 
        print (nt)


DB_FILE = "rip.db"

db = sqlite3.connect(DB_FILE) # opens or makes the file
c = db.cursor() 



# opens courses.csv and makes a dictionary (courses)
csv1 = open('courses.csv', 'r')
courses = csv.DictReader(csv1)

# makes courses table in rip.db
command = "CREATE TABLE courses (code TEXT, id INTEGER, mark INTEGER);"
#p("\n" + command) 
c.execute(command)

for row in courses: # adds code, id, and mark to courses    
    params = (row['code'], row['id'], row['mark'])
    c.execute("INSERT INTO courses VALUES (?,?,?)", params)


# opens peeps.csv and makes a dictionary (peeps)
csv2 = open('peeps.csv', 'r')
peeps = csv.DictReader(csv2)

# makes peeps table in rip.db
command = "CREATE TABLE peeps (name TEXT, id INTEGER, age INTEGER);"
#p("\n" + command)
c.execute(command)

for row in peeps: # adds name, id, and age to peeps
    params = (row['name'], row['id'], row['age'])
    c.execute("INSERT INTO peeps VALUES (?,?,?)", params)



# (re)calculates averages
def calcAvg(): 
    for s in peeps_grades: # gets avg and puts in peeps_avg
        grade = 0.0
        div = 0
        for m in peeps_grades[s]:
            grade += m
            div += 1
        peeps_avg[s] = [grade / div, div] # [average, num classes]
    #p(peeps_avg)    
    #p(peeps_names)


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
#p(peeps_grades)

    
# makes peeps _avg table in rip.db
command = "CREATE TABLE peeps_avg (id INTEGER, avg INTEGER);"
#p("\n" + command)
c.execute(command)

calcAvg() # (re)calculates avgs
for s in peeps_avg: # adds id, name to peeps_avg
    params = (s,peeps_avg[s][0])
    c.execute("INSERT INTO peeps_avg VALUES (?,?)", params)

    
# prints peeps id name avg
for peep in peeps_names:
    print str(peep) + "\t" + peeps_names[peep] + ": " + str(peeps_avg[peep][0])


db.commit() # saves changes
db.close() # closes db


