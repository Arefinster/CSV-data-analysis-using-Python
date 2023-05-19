# Modules
import os
import csv
from operator import itemgetter
import my_functions as mf

# Get the current script file directory
thisFile_path = os.path.dirname(__file__)
print(thisFile_path)

# Set path for the data csv file
csvpath = os.path.join(thisFile_path, "Resources", "election_data.csv")
print(csvpath)
print("\n")

# Open the file
with open(csvpath, 'r', encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",") # read the file
    header = next(csvreader) # Isolate the header  
    csv_rows = [[int(row[0]), row[1], row[2]] for row in csvreader] # Lets obtain all the rows after converting the first column to integers
    total_votes = len(csv_rows) # Total Months    [r for r in csv_rows]
    election_results = mf.vote_counter(csv_rows)
    winner_stat = max(election_results, key=itemgetter(2))

# Store all the results in a dictionary
election_info = {
    'nVotes' : total_votes,
    'results': election_results,
    'winner_name': winner_stat[0]
}

# Print the results to console and file
analysis_file = os.path.join(thisFile_path, "Analysis", "Results.txt")
mf.print_ElectionResults(election_info, analysis_file)