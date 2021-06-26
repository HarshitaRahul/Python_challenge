# Python_challenge
 
 PyBank data
 - The data which was provided gave us the details about months with their respective profit/losses. We were asked to find the total number of months with average with which I started to find the path of data , read the file using csv reader and move the titles to the next header and found the length of the data (no. of months).

 We need to append each of the column because the csv reader can read the file only once inside the loop and if we need to perform operations on the data. Sum fn. is used on the appended data .

 Subtracting the next month data  with the previous data and storing the data in change{} listwhich is used to perfoem sum of change /len. of change. Finding the max and min. in the changed{} list with index i.e., month

 Writing the file into analysis folder is important in txt format, writing into PyBank txt file and using text_file.write .

 PyPoll data
 - Similarly to Pydata ,PyPoll has info. about the candidates,voter_id and County. We need to read the file where data is and move the titles to the next header.

 No.of votes can be found using the length of data and candidates using set() value which returns unique values and iterating the corresponding votes to find the votes of individual candidates.

 Candidates percent by using no.of votes of individual candidates/ len of data *100. Using a for loop to read all the computed data and reverse = true , so that the data is in descending order 

 Writing the data into txt file using text_file.write().