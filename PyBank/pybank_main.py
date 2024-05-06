# Modules
import os
import csv  

# define variables
months = []
profit_losses_changes = []

count_months = 0
net_profit_loss = 0
previous_month_profit_loss = 0
current_month_profit_loss = 0
profit_loss_change = 0

# change the directory to the directory of the current python script
os.chdir(os.path.dirname(__file__))

# Path to collect data from the Resources folder
budget_data_csv_path = os.path.join('Resources', 'budget_data.csv')

# Read in the CSV file
with open(budget_data_csv_path, newline="") as csv_file:
    
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    # Read the header row first
    csv_header = next(csv_file)
    
    # print(f"Header: {csv_header}")
    # This prints: Header: Date, Profit/Losses
    
    # Initialize variables
    total_months = 0
    total_profit = 0
    total_change = 0
    prev_profit = 0
    greatest_increase = 0
    greatest_decrease = 0
    greatest_increase_month = ""
    greatest_decrease_month = ""
    # Read through each row of data after the header
    for row in csv_reader:
        # Calculate the total number of months included in the dataset
        total_months += 1
        # Calculate the net total amount of "Profit/Losses" over the entire period
        total_profit += int(row[1])
        # Calculate the average of the changes in "Profit/Losses" over the entire period
        if total_months > 1:
            change = int(row[1]) - prev_profit
            total_change += change
            if change > greatest_increase:
                greatest_increase = change
                greatest_increase_month = row[0]
            if change < greatest_decrease:
                greatest_decrease = change
                greatest_decrease_month = row[0]
        prev_profit = int(row[1])
    # Calculate the average of the changes in "Profit/Losses" over the entire period
    average_change = total_change / (total_months - 1)

# Print the analysis to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

# Write the analysis to the output.txt file 

budget_file = os.path.join("Analysis", "output.txt")
with open(budget_file, 'w') as outfile:
    outfile.write("Financial Analysis\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Months: {total_months}\n")
    outfile.write(f"Total: ${total_profit}\n")
    outfile.write(f"Average Change: ${average_change:.2f}\n")
    outfile.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
    outfile.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")



