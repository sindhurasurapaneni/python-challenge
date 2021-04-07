import os
import csv

Budget_csv = os.path.join( "Resources", "budget_data.csv")



with open(Budget_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    # data = list(csvfile)
    # row_count = len(data)
    # print ("Total Months:" + str(row_count))
    #Total_Months = len(list(csvfile))
    #print(Total_Months)
    Months = []
    Profit = []
    Profit_change = []

    for row in csvreader:
        # Add Profit
        Months.append(row[0])
        Profit.append(int(row[1]))
        Months_total = len(Months)
        sum_total = sum(Profit)
    #print(Months_total)
    #print(sum_total)
    
    for x in (1,len(Profit)-1):
    
        Profit_change.append((Profit[x] - Profit[x-1]))
    max_profit = max(Profit_change) 
    min_profit = min(Profit_change) 
    max_date = Months[Profit_change.index(max_profit)]
    min_date = Months[Profit_change.index(min_profit)]
print("Financial Analysis")
print("------------------------------")
print("Total Months:" + str(Months_total))
print("Total: $" + str(sum_total))
print("Average  Change: $" + str(round(sum(Profit_change)/len(Profit_change))))
#print(Profit_change)
print("Greatest Increase in Profits:"  + str(max_date) + "(" + str(max_profit) + ")")
print("Greatest Decrease in Profits:"  + str(min_date) + "(" + str(min_profit) + ")")
#print(min_profit)
#print(max_date)
#print(min_date)






