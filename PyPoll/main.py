'''----------PyPoll----------
* This Python script is designed to analyze an election dataset with VoterID, County, and Candidate columns
* Input file is in CSV (comma seperated value format)
* Output tasks include:
    * Calcuate total number of votes cast
    * Calculate a complete list of candidates that received votes
    * Calculate percentage of the total vote each candiate won
    * Calculate the total number of votes each candidate won
    * Find the winner of the election based on popular vote
* Print output to terminal and text file in "Analysis" folder
'''

#Import Dependancies
import os
import csv
import sys

#Create Variable for CSV File Path
csvpath = os.path.join('resources', 'election_data.csv')

#Read CSV File into program
with open(csvpath) as csvfile:

    #Assign csvfile to iterable variable
    csvreader = csv.reader(csvfile, delimiter = ',')

    #Read the header row first to move cursor to first data row
    csv_header = next(csvreader)

    #Build container for election dictionary    
    election = {}

    #Define candidate counting function
    def CountCandidates(candidates):
        
        for candidate in candidates:
            if candidate in election:
                election[candidate] += 1
            else:
                election[candidate] = 1
        return election

    #Build list container for candidates
    candidates = []

    #Loop through csv and extract candidates into list
    for row in csvreader:
        candidates.append(row[2])

    #Calculate Total # of Votes in election
    totVote = len(candidates)
    print('\n---------------\nElection Results\n---------------\n')
    print(f'Total Votes: {totVote}')

    #Call function to tally candidate totals (frequency function)
    CountCandidates(candidates)

    #Loop though election dictionary to calculate vote spread
    for key, value in election.items(): 
            pctTot =round((value / totVote) *100, 2)
            print(f'{key}: {pctTot}%  ({value})')

    #Calculate & Print Winner of Election 
    winner = max(election, key=election.get) 
    print(f'---------------\nWinner: {winner}\n---------------')

    #Write results to txt file using sys dependancy 
    txtpath = os.path.join('analysis', 'analysis.txt')

    with open(txtpath, 'w') as txtfile:

        print('\n----------------', file=txtfile)
        print('Election Results', file=txtfile)
        print('----------------\n', file=txtfile)
        print(f'Total Votes: {totVote}', file=txtfile)
        for key, value in election.items():
            pctTot =round((value / totVote) *100, 2) 
            print(f'{key}: {pctTot}%  ({value})', file=txtfile)

        print(f'---------------\nWinner: {winner}\n---------------', file=txtfile)

    txtfile.close()

csvfile.close()