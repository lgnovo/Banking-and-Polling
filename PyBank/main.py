#Dependencies
import os
import csv

#get csv from Resources file
budget_data_csv = os.path.join("Resources","budget_data.csv")

#initialize variables for analysis, (0 indicates the starting pt to accumulate values)
total_months = 0
total_profit_loss = 0
prev_profit_loss = None
changes = []
greatest_increase = 0
greatest_increase_date = ""
greatest_decrease = 0
greatest_decrease_date = ""
formatted_avg_change = 0

#open csv above in read-mode for use
with open(budget_data_csv, 'r') as budget_csv:
    csv_reader = csv.reader(budget_csv)
    row_header = next(csv_reader, None) #note the header for the first row

    #iterate a calculation from the rest of the rows
    for row in csv_reader: 
        #Totalling months in the dataset
        total_months +=1
    
    #Net Total Profit/Losses within timeframe
        profit_loss = int(row[1])
        total_profit_loss += profit_loss
    #format to string
        Net = "${:.0f}".format(total_profit_loss)

    #Changes in "Profit/Losses" within timeframe
        current_profit_loss = int(row[1])
        if prev_profit_loss is not None:
            change = current_profit_loss - prev_profit_loss
            changes.append(change)

    #Greatest Profit Increase (date and amount) w/in Period
            if change > greatest_increase:
                greatest_increase = change
                greatest_increase_date = row[0]

    #Greatest Profit Decrease (date and amount) w/in Period
            elif change < greatest_decrease:            
                greatest_decrease = change
                greatest_decrease_date = row[0]

        prev_profit_loss = current_profit_loss

#Average of changes
    average_change = sum(changes) / len(changes) if len(changes) > 0 else 0
    formatted_avg_change = "${:.2f}".format(average_change)

#Print information
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: {Net}")
print(f"Average Change: {formatted_avg_change}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

# Output results to a text file named "Financial Analysis"
output_file_path = "Financial Analysis.txt"

with open(output_file_path, 'w') as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("----------------------------\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Total: {Net}\n")
    output_file.write(f"Average Change: {formatted_avg_change}\n")
    output_file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    output_file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")