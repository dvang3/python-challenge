import os
import csv

Total_count= 0
Total_profit= 0
Average_Change = 0


budget_data_csv= os.path.join( "Resources", "budget_data.csv")
print(budget_data_csv)
with open(budget_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    print(csv_reader)

    csv_header= next(csv_reader)
    print(f"Header:{csv_header}")

    for row in csv_reader:
        print(row)
        Total_profit = Total_profit + int(row[1])
        Total_count = Total_count + 1
    print(Total_count)
    print(Total_profit)

    Average_Change= Total_count / Total_profit
    print(Average_Change)



