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
# County Options and Votes
county_options =[]
county_votes = {}
winning_county= ""
winning_countyCount= 0
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
            county_name = row[1]
    # If candidate/ county name does match any existing candidate/ county...
            if candidate_name not in candidate_options:
                candidate_options.append(candidate_name)
                candidate_votes[candidate_name]=0
            candidate_votes[candidate_name] +=1
            if county_name not in county_options:
                county_options.append(county_name)
                county_votes[county_name] =0 
            county_votes[county_name] +=1
# Save results to the text file
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to terminal and text file
    election_results= (
        f"\nElection Results\n"
        f"----------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"----------------------\n"
        f"County Votes:\n")
    print(election_results, end="")
    txt_file.write(election_results)

# Retrieve county vote count and percentage and print to terminal and text file

    for county in county_votes:
        countyVotes = county_votes[county]
        countyVotesPercentage = float(countyVotes)/float(total_votes)*100
        county_results= (
            f"{county}: {countyVotesPercentage:.1f}% ({countyVotes:,})\n")
        print(county_results)
        txt_file.write(county_results)
    
# Print largest county turnout to terminal and text file
           
        if (countyVotes>winning_countyCount):
            winning_countyCount= countyVotes
            winning_county = county
            LargestCountyTurnout=(
            f"----------------------\n"
            f"Largest County Turnout: {winning_county}\n"
            f"----------------------\n")  
    print(LargestCountyTurnout)
    txt_file.write(LargestCountyTurnout) 

# Retrieve candidate vote count and percentage and winning candidate summary and print to terminal and text file

    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        vote_percentage = float(votes)/float(total_votes)*100
        candidate_results= (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)
    
        if (votes>winning_count) and (vote_percentage > winning_percentage):
            winning_count=votes
            winning_candidate=candidate
            winning_percentage=vote_percentage 
    
    winning_candidate_summary=(
        f"----------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"----------------------\n")
    
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
