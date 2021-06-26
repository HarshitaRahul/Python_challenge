import csv
import os

# Files to load 
csvpath = os.path.join("..", "PyBank", "Resources" ,"budget_data.csv")


# Read the csv and convert it into a list of dictionaries
with open(csvpath) as csvfile:
    reader = csv.reader(csvfile)
    

    # use of next to skip first title row in csv file
    header=next(reader) 
    revenue = []
    date = []
    change = []

    # in this loop I did sum of column 1 which is revenue in csv file and counted total months which is column 0 
    for row in reader:

        revenue.append(int(row[1]))
        date.append(row[0])

    print("Financial Analysis")
    print("-----------------------------------")
    print("Total Months:", len(date))
    print("Total : $", sum(revenue))


    #in this loop I did total of difference between all row of column "Revenue" and found total revnue change. Also found out max revenue change and min revenue change. 
    for i in range(1,len(revenue)):
        change.append(revenue[i] - revenue[i-1])   
        avg_change = sum(change)/len(change)

        max_change = max(change)

        min_change = min(change)

        max_change_date = str(date[change.index(max(change))])
        min_change_date = str(date[change.index(min(change))])


    print("Avereage Change: $", round(avg_change))
    print("Greatest Increase in Profits:", max_change_date,"($", max_change,")")
    print("Greatest Decrease in Profits:", min_change_date,"($", min_change,")")

#write file
output_path =os.path.join(".." , "Pybank" ,"Analysis" , "PyBank.txt")

with open(output_path, 'w') as text_file:
     #text_file = csv.writer(csvfile)
     text_file.write ("Financial Analysis: \n")
     text_file.write ("---------------------------------------\n")
     text_file.write (f"Total Months: {str(len(date))}\n")
     text_file.write (f"Average Change: ${str(avg_change)}\n")
     text_file.write (f"Greatest Increase in Profits: {str(max_change_date)} (${str(max_change)})\n")
     text_file.write (f"Greatest Decrease in Profits: {str(min_change_date)} (${str(min_change)})\n")



