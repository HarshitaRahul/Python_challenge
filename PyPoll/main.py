#Modules
import os
import csv

csvpath = os.path.join("..", "PyPoll", "Resources" ,"election_data.csv")


# Open the csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter =',')
    
# Total number of votes cast
    header = next(csvreader)
    data = [row for row in csvreader]
    candidates ={}
     
 # Total
    total_votes = len(data)
    print(total_votes)

    # print("Election results")
    # print("----------------------------")
    # print("Total number of votes cast:" + str(len))
    # print("----------------------------")

     

