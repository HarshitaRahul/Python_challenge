#Modules
import os
import csv

csvpath = os.path.join("..", "PyPoll", "Resources" ,"election_data.csv")
voterid=0
cy=0
Candidate=0

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

#complete list of candidates who received votes
    for row in csvreader:
        voterid.append(int(row[0]))
        cy.append(int(row[1]))
        Candidate.append(int(row[2]))
     
    if ((Candidate)== "Khan"):
        len[Candidate]+=1
    print("Khan :" , ([Candidate]))

    #     candidate = row.split(",") [-1].strip()
    #     len[candidate]+=1 
    # print("candidate:", + str(len[candidate]))
