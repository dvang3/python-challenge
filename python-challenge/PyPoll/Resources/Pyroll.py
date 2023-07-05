import os
import csv


Total_vote= 0
Percentage_of_vote= 0


election_data = os.path.join("..", "Resources", "election_data copy.csv")
print(election_data)
with open(election_data) as csv_file:
    csvreader= csv.reader(csv_file, delimiter= ",")
    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        print(row)
       
        Total_vote = Total_vote + 1
        print(Total_vote)
        
name= {}
candiate_name= "Charles Casper Stockham"

if candiate_name in name :
    name[candiate_name] = name[candiate_name] +1
else:
    name[candiate_name] = 1
print(name)


name= {}
candiate_name2= "Diana DeGette"
if candiate_name2 in name :
    name[candiate_name2]= name[candiate_name2] +1
else: 
    name[candiate_name2] = 1
print(name)

name= {}
candiate_name3 = "Raymon Anthony Doane"
if candiate_name3 in name:
    name[candiate_name3] = name[candiate_name3] +1
else: 
    name[candiate_name3] = 1
print(name)


