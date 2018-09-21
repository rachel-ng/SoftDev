import csv, random

def randocc():
    occupations = []
    
    # reads csv file
    csvfile = open('data/occupations.csv', 'r')
    dictreader = csv.DictReader(csvfile)
    
    # looks at each row except for the last
    for row in dictreader:
        if (row['Job Class'] != 'Total'):
	    # fills list w. occupations frequency dependent on %
            i = 0
            while i < (float(row['Percentage'])*10):
                occupations.append(row['Job Class'])
                i+=1
    return random.choice(occupations)

def d():
    reader = csv.reader(open('data/occupations.csv', 'r'))
    return dict(reader)
