# Team RKade -- Karen Li and Rachel Ng
# SoftDev1 pd7
# K06 -- StI/O: Divine your Destiny!
# 2018-09-13

import csv, random

occupationList = []

def fillList():
	#reads csv file
	csvFileObject = open( 'occupations.csv', 'r')
	dictionaryReader = csv.DictReader( csvFileObject)
	
	#looks at each row except for the last
	for row in dictionaryReader:
		if (row['Job Class'] != 'Total'):
		
			#fills occupationList with occupations with frequency dependent on percentage
			i = 0
			while i < (float(row['Percentage'])*10):
				occupationList.append(row['Job Class'])
				i+=1

#returns a randomly selected occupation from the weighted occupationList
def randomOccupation():
	return random.choice(occupationList)
				
fillList()
print(randomOccupation())
