# import csv

# Khan = []
# Correy = []
# Li = []
# O_Tooley = []

# with open('C:\\Users\\sindh\\Desktop\\GitLab\\python-challenge\\PyPoll\\Resources\\election_data.csv') as datafile:
#     Poll_data = csv.reader(datafile,delimiter= ",")
#     csv_header = next(datafile)
#     data = list(datafile)
#     row_count = len(data)
#     print ("Total Votes:" + str(row_count))

#     for row in datafile:
#      print (datafile)



import os
import csv

election_csv = os.path.join( "Resources", "election_data.csv")

# Lists to store data
# title = []
# price = []
# subscribers = []
# reviews = []
# review_percent = []
# length = []
Khan = []
# Use encoding for Windows
# with open(udemy_csv, newline='', encoding='utf-8') as csvfile:
with open(election_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        # Add title
        Khan.append(row[1])
        print(len(Khan))