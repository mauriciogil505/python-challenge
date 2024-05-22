import csv
import os

# First, I want to define the file path for the csv file
csv_path = os.path.join("Resources", "election_data.csv")

# Next, I need to initialize the variables
total_votes = 0
candidate_votes = {}
candidates = []

# In this step, I need code to read the CSV file
with open(csv_path, mode='r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)  # Skip the header row
    
    # Next, code to process each row
    for row in csvreader:
        total_votes += 1
        candidate = row[2]
        
        if candidate not in candidates:
            candidates.append(candidate)
            candidate_votes[candidate] = 0
        candidate_votes[candidate] += 1

# Then, code to calculate percentages and find the winner of the election poll
winner = ""
max_votes = 0
results = []

for candidate in candidate_votes:
    votes = candidate_votes[candidate]
    percentage = (votes / total_votes) * 100
    results.append(f"{candidate}: {percentage:.3f}% ({votes})")
    
    if votes > max_votes:
        max_votes = votes
        winner = candidate

# In this step, I need to print the results
output = (
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n"
    f"{results[0]}\n"
    f"{results[1]}\n"
    f"{results[2]}\n"
    f"-------------------------\n"
    f"Winner: {winner}\n"
    f"-------------------------"
)

print(output)

# And finally save the results to a text file
output_path = os.path.join("analysis", "election_results.txt")

with open(output_path, mode='w') as file:
    file.write(output)

os.getcwd()
