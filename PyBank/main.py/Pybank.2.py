import os
import csv


#Creating path to the CSV file to be imported
csvpath= os. path.join(r'C:\Users\A1990\repository\Python-challege.hw\PyBank\Resources','budget_data.csv')

# Create a list to store data
budget_data = []

# Open the CSV
with open(csvpath) as csvfile:
    reader = csv.DictReader(csvfile)

    # Loop through the data to store it in a dictionary
    for row in reader:
        budget_data.append({"month": row["Date"], "amount": int(row["Profit/Losses"]), "change": 0})

# Calculate the total number of months
total_months = len(budget_data)

# Calculate the changes between months
previous_amount = budget_data[0]["amount"]
for i in range(total_months):
    budget_data[i]["change"] = budget_data[i]["amount"] - previous_amount
    previous_amount = budget_data[i]["amount"]

# Calculate the total amount
total_amount = sum(row['amount'] for row in budget_data)

# Calculate the average of amount changes
total_change = sum(row['change'] for row in budget_data)
average = round(total_change / (total_months - 1), 2)

# Find the greatest increase and decrease from the changes
get_increase = max(budget_data, key=lambda x: x['change'])
get_decrease = min(budget_data, key=lambda x: x['change'])

# Print the final analysis
print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {total_months}')
print(f'Total: ${total_amount}')
print(f'Average Change: ${average}')
print(f'Greatest Increase in Profits: {get_increase["month"]} (${get_increase["change"]})')
print(f'Greatest Decrease in Profits: {get_decrease["month"]} (${get_decrease["change"]})')

# Print and export results to a text file
output_filepath = os.path.join(r'C:\Users\A1990\repository\Python-challege.hw\PyBank', 'analysis.txt')
with open(output_filepath, "w") as text_file:
    print('Financial Analysis', file=text_file)
    print('----------------------------', file=text_file)
    print(f'Total Months: {total_months}', file=text_file)
    print(f'Total: ${total_amount}', file=text_file)
    print(f'Average Change: ${average}', file=text_file)
    print(f'Greatest Increase in Profits: {get_increase["month"]} (${get_increase["change"]})', file=text_file)
    print(f'Greatest Decrease in Profits: {get_decrease["month"]} (${get_decrease["change"]})', file=text_file)


 
   
 
    
    
