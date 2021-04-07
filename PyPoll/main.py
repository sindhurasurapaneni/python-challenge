


import os
import csv

election_csv = os.path.join( "Resources", "election_data.csv")

data = []
Khan = 0
Correy = 0
Li = 0
O_Tooley = 0
with open(election_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader: 
        data.append((row[0]))
        Total_Votes = len(data)

        if row[2] == 'Khan':
            Khan = Khan+1
        elif row[2] == 'Correy':
            Correy = Correy+1
        elif row[2] == "Li"
            Li = Li+1
        elif row[2] == "O'Tooley"
            O_Tooley = O_Tooley+1

print("Election Results")
print("---------------------------------")
print("Total Votes:" +str(Total_Votes))
print("---------------------------------")
print(Khan)