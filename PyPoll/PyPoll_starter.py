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

        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
        total_votes +=1

        # Get the candidate's name from the row
        candidate_name= row[2]


        # If the candidate is not already in the candidate list, add 
        votes=0
        candidate_obj= {"name": candidate_name, "votes":votes+1 }
        cantidates_names.append(candidate_name) 
        # Add a vote to the candidate's count
        cantidates_names[candidate_name]+1

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)
    print(f'total_votes: {total_votes}')


    # Write the total vote count to the text file
    txt_file.write(f"Total Votes: {total_votes}\n")
    txt_file.write("-------------------------\n")


    # Loop through the candidates to determine vote percentages and identify the winner
    winning_candidate = ""
    winning_count = 0
    

        # Get the vote count and calculate the percentage
    votes = cantidates_votes [cantidates_names]
    Percentage = (votes /total_votes)* 100

        # Update the winning candidate if this one has more votes
    if votes > winning_count:
            winning_candidate = cantidates_names

        # Print and save each candidate's vote count and percentage
    print(f' {cantidates_names}: {Percentage:.3f}% ({total_votes})')

    # Generate and print the winning candidate summary
    print("-------------------------")
    print(f"Winner: {winning_candidate}")
    print("-------------------------")
    
    # Save the winning candidate summary to the text file
    txt_file.write("-------------------------\n")
    txt_file.write(f"Winner: {winning_candidate}\n")
    txt_file.write("-------------------------\n")