# 
# SoftDev1 pd7
# SQLITE3 BASICS
# 2018-10-04

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


#DB_FILE="discobandit.db"

#db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
#c = db.cursor()               #facilitate db ops

csv1 = open('courses.csv', 'r')
courses = csv.DictReader(csv1)
for row in courses:
    print(row)

csv2 = open('peeps.csv', 'r')
peeps = csv.DictReader(csv2)
for row in peeps:
    print(row)

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE


#command = ""          #build SQL stmt, save as string
#c.execute(command)    #run SQL statement

#==========================================================

#db.commit() #save changes
#db.close()  #close database


