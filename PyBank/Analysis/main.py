import os
import csv
'Cited Sources: XPert Learning Assistant, Classroom Recordings, Previous Class Activities'

# Define the path to the CSV file
csv_path = os.path.join('Resources', 'budget_data.csv')

# Initialize variables
total_months = 0
net_total = 0
previous_profit_loss = 0
changes = []
dates = []

# Read the CSV file
with open(csv_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)  # Skip the header row

    for row in csvreader:
        # Extract date and profit/loss
        date = row[0]
        profit_loss = int(row[1])

        # Count the total number of months
        total_months += 1

        # Calculate the net total amount of "Profit/Losses"
        net_total += profit_loss

        # Calculate the changes in "Profit/Losses"
        if total_months > 1:
            change = profit_loss - previous_profit_loss
            changes.append(change)
            dates.append(date)

        previous_profit_loss = profit_loss

# Calculate average change
average_change = sum(changes) / len(changes)

# Find greatest increase and decrease in profits
greatest_increase = max(changes)
greatest_decrease = min(changes)
greatest_increase_date = dates[changes.index(greatest_increase)]
greatest_decrease_date = dates[changes.index(greatest_decrease)]

# Print the analysis to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

# Export the results to a text file
output_path = os.path.join('analysis', 'financial_analysis.txt')

with open(output_path, 'w') as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${net_total}\n")
    txtfile.write(f"Average Change: ${average_change:.2f}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")
