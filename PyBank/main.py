# Modules
import os
import csv
from statistics import mean
import my_functions as mf

# Get the current script file directory
thisFile_path = os.path.dirname(__file__)
print(thisFile_path)

# Set path for the data csv file
csvpath = os.path.join(thisFile_path, "Resources", "budget_data.csv")
print(csvpath)
print("\n")

# Open the file
with open(csvpath, 'r', encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",") # read the file
    header = next(csvreader) # Isolate the header   
    csv_rows = [[row[0], int(row[1])] for row in csvreader] # Lets obtain all the rows after converting the second column to integers
    total_months = len(csv_rows) # Total Months    [r for r in csv_rows]
    total_prof_loss = sum([r[1] for r in csv_rows]) # Total
    p_l_changes = [csv_rows[r+1][1]-csv_rows[r][1] for r in range (total_months-1)] # The changes in "Profit/Losses" over the entire period
    mean_change = round(mean(p_l_changes), 2) # Average Change  
    max_inc_prof = max(p_l_changes) #Greatest Increase in Profits
    max_inc_date = [csv_rows[r+1][0] for r in range (total_months-1) if csv_rows[r+1][1]-csv_rows[r][1] == max_inc_prof] # Date of Greatest Increase in Profits
    max_dec_prof = min(p_l_changes) #Greatest Increase in Profits
    max_dec_date = [csv_rows[r+1][0] for r in range (total_months-1) if csv_rows[r+1][1]-csv_rows[r][1] == max_dec_prof] # Date of Greatest Increase in Profits

# Store the results in a dictionary
summary = {
    'nMonths': total_months,
    'total_prof_loss' : total_prof_loss,
    'avg_change' : mean_change,
    'max_inc' : {
        'date': max_inc_date,
        'value' : max_inc_prof
    },
    'max_dec' : {
        'date': max_dec_date,
        'value' : max_dec_prof
    }
}

# Print the results to console and file
analysis_file = os.path.join(thisFile_path, "Analysis", "Results.txt")
mf.print_finAnalysis(summary, analysis_file)
1