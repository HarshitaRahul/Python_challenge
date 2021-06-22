#Modules
import os
import csv

csvpath = os.path.join("..", "PyPoll", "Resources" ,"election_data.csv")
voterid=0
cy=0
candidate=0
votes=0

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
        candidate.append(int(row[2]))
     
        for i in range(1,len):
            if ([candidate]== "Khan"):
                len[candidate]+=1
                print("Khan :" + int[candidate])
            elif([candidate]=="Coorey"):
                len[candidate]+=1
                print("Coorey :" + int[candidate])
            elif([candidate]=="Li"):
                len[candidate]+=1
                print("Li :" + int[candidate])
            else:
                len[candidate]+=1
                print("O'Tooley :" + int[candidate])

     

