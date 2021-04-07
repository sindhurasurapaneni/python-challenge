


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
        elif row[2] == 'Li':
            Li = Li+1
        elif row[2] == "O'Tooley":
            O_Tooley = O_Tooley+1
Percent_Khan = round((Khan / Total_Votes)*100 ,0)
Percent_Correy = round((Correy / Total_Votes)*100,0)
Percent_Li = round((Li / Total_Votes)*100,0)
Percent_O_Tooley = round((O_Tooley / Total_Votes)*100,0)

print("Election Results")
print("---------------------------------")
print("Total Votes:" +str(Total_Votes))
print("---------------------------------")
print("Khan:"  + str(Percent_Khan) + "%"+ "(" + str(Khan) + ")")
print("Correy:"  + str(Percent_Correy) + "%"+ "(" + str(Khan) + ")")
print("Li:"  + str(Percent_Li) + "%"+ "(" + str(Khan) + ")")
print("O_Tooley:"  + str(Percent_O_Tooley) + "%"+ "(" + str(Khan) + ")")