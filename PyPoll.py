# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list ofcandidates who recieved votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the the election based on popular vote. 

# Import the datetime class from the datetime module.
import datetime as dt
from os import read

# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)

#Add our dependencies
import csv
import os


#Assign a variable for the file to load and the path
file_to_load = "/Users/Kris/Desktop/module_work_challenges/mod_3_challenge/Resources/election_results.csv"

# Create a filename variable to a direct or indirect path to the file.
file_to_save ="/Users/Kris/Desktop/module_work_challenges/mod_3_challenge/analysis/election_analysis.txt"

# 1. Initialize a total vote counter.
total_votes = 0

# Candidate Options
candidate_options = []

# 1. Declare the empty dictionary.
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# Open the election results and read the file.
with open(file_to_load) as election_data:              
     # To do: read and analyze the data here. w/ reader funtion
     file_reader = csv.reader(election_data)

     # Read Header Row
     headers = next(file_reader)
    
     # Print each row in the CSV file.
     for row in file_reader:
               #Add to the total vote count.
               total_votes += 1
               # print the candidate name from each row
               candidate_name = row[2]

          # If the candidate does not match any existing candidate...
               if candidate_name not in candidate_options:
               # Add it to the list of candidates.
                    candidate_options.append(candidate_name)
               # Begin tracking that candidate's vote count.
                    candidate_votes[candidate_name] = 0
          # Add a vote to that candidate's count.
               candidate_votes[candidate_name] += 1

# Determine the percentage of votes for each candidate by looping through the counts.
# Iterate through the candidate list.
for candidate_name in candidate_votes:
    # Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100

#  To do: print out each candidate's name, vote count, and percentage of
    # votes to the terminal.
 # Print the candidate name and percentage of votes.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    
    # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent =
         # vote_percentage.
         winning_count = votes
         winning_percentage = vote_percentage
         # And, set the winning_candidate equal to the candidate's name.
         winning_candidate = candidate_name
         
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)

   


# Print the candidate vote dictionary.
#print(candidate_votes)

# Print the total votes.
#print(total_votes)
     

































# Print the candidate list.
#print(candidate_options)
 

#Use the open statement to open the file as a text file.
#outfile = open(file_to_save, "w")

# Write some data to the file.
#outfile.write("Hello World")


# Use with statement to open save the file as a text file.
# with open(file_to_save, "w") as text_file:
 #   print("Hello")


# Notes & old commands that were switched to make code cleaner
#Use the open statement to open the file as a text file.
#outfile = open(file_to_save, "w")

# Write some data to the file.
# outfile.write("Hello World")
 
# Write some data to the file. remember to indent because of above :
#outfile.write("Hello World")

#method 2 to writeing counties to file
 #    text_file.write("Arapahoe, Denver, Jefferson")

# Write some data to the file. remember to indent because of above :
# text_file.write("Counties in the Elections")
# text_file.write("\n--------------------------")
# Write three counties to the file.  \n at begining starts new line otherwise the line above would run into 
#text_file.write("\nArapahoe\nDenver\nJefferson")

#Close the file:
