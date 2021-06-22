#Modules
import os
import csv

csvpath = os.path.join("..", "PyPoll", "Resources" ,"election_data.csv")

# Open the csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter =',')
    len=0
# Total number of votes cast
    nextline = next(csvreader)
    for row in csvreader :
        len+=1
    print("Election results")
    print("----------------------------")
    print("Total number of votes cast:" + str(len))
    print("----------------------------")
