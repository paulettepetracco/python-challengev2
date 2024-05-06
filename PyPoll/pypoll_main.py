# Modules
import os
import csv  

# define variables
TotalVotes = 0
candidateNames = []
winner = {}

# change the directory to the directory of the current python script
os.chdir(os.path.dirname(__file__))

# Path to collect data from the Resources folder
election_data_csv_path = os.path.join('Resources', 'election_data.csv')

# Read in the CSV file
with open(election_data_csv_path, newline="") as csv_file:
    
    election_data_csv = csv.reader(csv_file, delimiter=',')
    
    # read the header row first 
    csv_header = next(csv_file)
    
    print(f"Header: {csv_header}")
    # This prints: Header: Voter ID, County, Candidate
    
    # find the total number of votes with loop
    for row in election_data_csv:
        
        # total number of votes included in data
        if row[0] == "Ballot ID": continue
        TotalVotes += 1
        candidateNames.append(row[2])
    # list of candidates who received votes 
    candidates = list(set(candidateNames))
    candidates.sort()
    
    for candidate in candidates:
        name = candidate
        candidateVotes = candidateNames.count(candidate)
        percentage = round((candidateVotes / TotalVotes) * 100, 3)
        
        if not winner:
            winner["name"] = name
            winner["votes"] = candidateVotes
        elif candidateVotes > winner["votes"]: winner.update({"name": name,
        "votes": candidateVotes})
        else: continue 

# print analysis to terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {TotalVotes}")
print("-------------------------")
for candidate in candidates:
    print(f"{candidate}: {round((candidateNames.count(candidate) / TotalVotes) * 100, 3)}% ({candidateNames.count(candidate)})")    
print("-------------------------")
print(f"Winner: {winner['name']}")

# define the output file path
directory = "Analysis"
if not os.path.exists(directory):
    os.makedirs(directory)

# Write the analysis to the text file
election_file = os.path.join("Analysis", "output.txt")
with open(election_file, 'w') as outfile: 
    outfile.write("Election Results\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Total Votes: {TotalVotes}\n")
    outfile.write("-------------------------\n")
    for candidate in candidates:
        outfile.write(f"{candidate}: {round((candidateNames.count(candidate) / TotalVotes) * 100, 3)}% ({candidateNames.count(candidate)})\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Winner: {winner['name']}\n")