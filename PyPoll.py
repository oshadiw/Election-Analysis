import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources/election_results.csv")
# Create a filename variable to a direct or indeirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize a total vote counter.
total_votes=0
# Candidate Options and votes
candidate_options = []
candidate_votes= {}
# Winning Candidate and Winning Count Tracker
winning_candidate= ""
winning_count= 0
winning_percentage= 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
# Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    
    # Read the header row.
    headers = next(file_reader)
    
    # Print each row in the CSV file.
    for row in file_reader:
            total_votes +=1
            candidate_name = row[2]
    # If candidate name does match any existing candidate...
            if candidate_name not in candidate_options:
                candidate_options.append(candidate_name)
                candidate_votes[candidate_name]=0
            candidate_votes[candidate_name] +=1
for candidate in candidate_votes:
    votes = candidate_votes[candidate]
    vote_percentage = float(votes)/float(total_votes)*100
    if (votes>winning_count) and (vote_percentage > winning_percentage):
        winning_count=votes
        winning_percentage=vote_percentage
        winning_candidate=candidate
winning_candidate_summary=(
    f"----------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"----------------------\n")
print(winning_candidate_summary)