#Modules
import os
import csv

csvpath = os.path.join("..", "PyBank", "Resources" ,"budget_data.csv")
len=0
total=0

# Open the csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter =',')

# loop through to check for number of months
# to find the net total amount of profit/losses

    nextline=next(csvreader)
    for row in csvreader:
        len+=1
        total+=int(row[1])
    print("Financial Analysis")
    print("-----------------------------")
    print("Totalmonths :" + str(len))
    print("Total :" + "$" + str(total))

    # Average of the changes in Profit/Losses
    #the list used to store all the average changes
    change=[]
    for i in range(1,len(csvreader)):
        #month[i]=month[i]-month[i-1]
        change.append(row[i] - row[i-1])
        avg_chng = round(sum(change)/len(change),2)
    print(avg_chng)
    # for month in avg_change:
    #     print(month[i])





    





