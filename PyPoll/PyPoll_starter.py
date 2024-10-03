# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("PyPoll","Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("PyPoll","analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
cantidates_names =[]
# Store the candiate name and votes 
cantidates_votes = {}
# Winning Candidate and Winning Count Tracker

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader) 

    # Loop through each row of the dataset and process it
    for row in reader:

        # Increment the total vote count for each row
        total_votes +=1

        # Get the candidate's name from the row
        candidate_name= row[2]


        # If the candidate is not already in the candidate list, add 
        if candidate_name not in cantidates_names: 
             cantidates_names.append(candidate_name)
             cantidates_votes[candidate_name]=0 # {Charles Casper Stockham: 0}
        
        # Add a vote to the candidate's count
        cantidates_votes[candidate_name]+=1

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)
    print(f'total_votes: {total_votes}')


    # Write the total vote count to the text file
    election_results = (
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n"
    )
    print(election_results, end="")
    txt_file.write(election_results)


    # Loop through the candidates to determine vote percentages and identify the winner
    winning_candidate = ""
    winning_count = 0
    winning_percentage=0

    # Get the vote count and calculate the percentage
    for candidate in cantidates_names:
        votes = cantidates_votes [candidate]
        candiate_vote_percentage = (votes /total_votes)* 100

         # Print and write each candidate's vote count and percentage
        candidate_results = f"{candidate}: {candiate_vote_percentage:.3f}% ({votes})\n"
        print(candidate_results, end="")
        txt_file.write(candidate_results)

        # Update the winning candidate if this one has more votes
        if votes > winning_count:
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = candiate_vote_percentage

        # Print and save each candidate's vote count and percentage
        print(f' {cantidates_names}: {candiate_vote_percentage:.3f}% ({total_votes})')

    # Print and write the winner information
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n"
    )
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)