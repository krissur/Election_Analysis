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

# Open the election results and read the file.
with open(file_to_load) as election_data:              
     # To do: read and analyze the data here. w/ reader funtion
     file_reader = csv.reader(election_data)

     # Print each row in the CSV file.
     headers = next(file_reader)
     print(headers)

# Use with statement to open save the file as a text file.
#with open(file_to_save, "w") as text_file:
 #    election_data.close()















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
