#Modules
import os
import csv
from sys import call_tracing

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

# list of candidates
    candidate_votes = []
    for row in data:
        candidate_votes.append(row[2])

    unique_candidates = set(candidate_votes)
    for candidate in unique_candidates :
        candidates[candidate]=0

# total votes per candidate
    for vote in candidate_votes :
        candidates[vote]+=1
    print(candidates)

# Vote percentage for each andidate
    candidates_pct = {}
    for candidate in unique_candidates:
        vote_count = candidates[candidate]
        candidates_pct[candidate] = int(round(vote_count/total_votes * 100,0))
    print(candidates_pct)

# Winner (most votes)
    winner_name = ""
    winner_votes = 0
    winner_pct = 0
    for key , value in candidates.items() :
        if value > winner_votes:
            winner_votes = value
            winner_name = key
            winner_pct = candidates_pct[key]



    print("Election results")
    print("----------------------------")
    print(f"Total number of votes cast: {total_votes}")
    print("----------------------------")
    for w in sorted(candidates,key=candidates.get,reverse= True):
        print(f"{w}: {candidates_pct [w]}% ({candidates[w]})")

    print("-------------------------------")
    print(f"{winner_name} IS THE WINNER! ")

     

