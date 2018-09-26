# Team R (Rachel Ng, Raymond Wu)
# SoftDev1 pd7
# K10 -- Jinja Tuning
# 2018-09-25

from csv import reader
from random import choices

occupations = {}
weights = []

# POSTCONDITION: occupations dict is populated with occupation data
def csvToDict():
    csvFileObject = open('./data/occupations.csv', 'r')  # opens csv in 'read' mode
    readerObject = reader(csvFileObject)  # reads the csv

    for record in readerObject:
        if record[0] == "Job Class" or record[0] == "Total":  
            continue  # skips first and last records
        
        # record[0] = occupation (string), record[1] = percentage (string), record[2] = link (string)
        # converts percentage into floating point
        else:
            occupations[ record[0] ] = [ float( record[1] ) , record[2] ]
            # occupation : [ <percentage> , <link> ]
            
    csvFileObject.close()

# PRECONDITION: occupations dict cannot be empty (csvToDict must have ran first)
# POSTCONDITION: weights list is populated w/ weighted percentages of randomness
def dictWeights():
    listValues = list(occupations.values()) # list containing list of values in occupations dict
    # values in form [ <percentage> , <link> ]

    for listOfOccupationData in listValues:             # for each value in current list of occupation data
        weights.append( listOfOccupationData[0] )       # add percentage to list of weights

# these accessor methods are necessary b/c
# it doesn't make sense to keep reading the csv file & re-populate the occupations dict
# every time we want to access the data

# accessor methods so we don't need to reread csv file and repop occupations dict everytime we want to access the data
# POSTCONDITION (both functions): occupations{} and weights[] must be populated w/ data
def getOccupationsDict():
    return occupations

def getWeights():
    return weights

def getRandomOccupation():
    return choices( list(getOccupationsDict().keys()) , weights = getWeights() )[0]
# puts the keys to occupation dict in a list, choose randomly (weighted) from that list
# random.choices() returns a k-sized list (default=1) ... only concerned with first output

#choices( list(getOccupationsDict().keys()) , weights = getWeights() )[0]

