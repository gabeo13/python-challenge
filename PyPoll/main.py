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

    #Read the header row first
    csv_header = next(csvreader)

    #Define candidate counting function
    def CountCandidates(candidates, totVote):

        election = {}
        for candidate in candidates:
            if candidate in election:
                election[candidate] += 1
            else:
                election[candidate] = 1

        for key, value in election.items(): 
            pctTot =round((value / totVote) *100, 2)
            print(f'{key}: {value} {pctTot}%')

        winner = max(election, key=election.get) 
        print(f'\nWinner: {winner}')

        #Write results to txt file
        txtpath = os.path.join('analysis', 'analysis.txt')

        with open(txtpath, 'w') as txtfile:

            print('\n----------------', file=txtfile)
            print('Election Results', file=txtfile)
            print('----------------\n', file=txtfile)
            print(f'Total Votes: {totVote}', file=txtfile)
            for key, value in election.items(): 
                print(f'{key}: {value} {pctTot}%', file=txtfile)

            print(f'\nWinner: {winner}', file=txtfile)

        txtfile.close()

    #Build list container
    candidates = []

    #Loop through data set
    for row in csvreader:

        #Fill Candiate List
        candidates.append(row[2])

    #Calculate Total # of Votes
    totVote = len(candidates)
    print('\n---------------\nElection Results\n---------------\n')
    print(f'Total Votes: {totVote}')

    #Call function to tally candidate totals and declare winner
    CountCandidates(candidates, totVote)    

csvfile.close()

    






    



    







