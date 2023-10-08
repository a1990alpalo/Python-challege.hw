import os
import csv

#Creating path to the CSV file to be imported
csvpath= os. path.join(r'C:\Users\A1990\repository\Python-challege.hw\PyPoll\Resources', 'election_data.csv')

# Initialize variables
candidates = {}
total_votes = 0

# Open and read the CSV file
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        # Add to our vote counter
        total_votes += 1

        candidate_name = row[2]

        # If the candidate is not in our dictionary, add them with one vote
        if candidate_name not in candidates:
            candidates[candidate_name] = 1
        else:
            candidates[candidate_name] += 1

# Find the winning candidate
winning_candidate = max(candidates, key=candidates.get)

# Displaying results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {total_votes}")
print("--------------------------")
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    percentage = round(percentage, 3)
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("--------------------------")
print(f"Winner: {winning_candidate}")
print("--------------------------")

# Exporting to .txt file
output_filepath = os.path.join(r'C:\Users\A1990\repository\Python-challege.hw\PyPoll\analysis', 'analysis.txt')
with open("output.txt", "w") as output:
    output.write("Election Results\n")
    output.write("--------------------------\n")
    output.write(f"Total Votes: {total_votes}\n")
    output.write("--------------------------\n")
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        percentage = round(percentage, 3)
        output.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    output.write("--------------------------\n")
    output.write(f"Winner: {winning_candidate}\n")
    output.write("--------------------------\n")



