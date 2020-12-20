#Import OS Module to enable cross platform functionality across operating systems
import os 

#Import Module to read csv files
import csv

#Import Module to write output to txt files
import sys

#Assign csv file path to a variable
csvpath = os.path.join('resources', 'budget_data.csv')

#Read csv file in to program
with open(csvpath) as csvfile:

    #Assign contents of csv file to variable and specify delimiter
    csvreader = csv.reader(csvfile, delimiter=',')

    #Read csv data into a list
    rows = list(csvreader)

    ## Create containers for each columnar derived list
    months = []
    profitLoss = []

    ##Calculate total number of months and total profit/loss
    for row in rows[1:]:
        months.append(row[0])
        profitLoss.append(int(row[1]))
    totalProfitloss = sum(profitLoss)
    totalMonths = len(months)    
  
    ##Calculate the changes in Profit/Losses over the entire period, then find the average
    change = []
    i = 0

    for i in range(len(profitLoss)-1):
        change.append(profitLoss[i+1]-profitLoss[i]) 
    sumChange = sum(change)
    numChange = len(change)
    avgChange = sumChange/numChange

    ##Find greatest increase in profit (date and amount) over the entire period
    max_prof = max(profitLoss)
    max_prof_date = months[profitLoss.index(max_prof)]

    ##Find greatest decrease in profit (data and amount) over the entire period
    min_prof = min(profitLoss)
    min_prof_date = months[profitLoss.index(min_prof)]
    
    ##Print results to terminal
    print(f'\n\nFinancial Analysis\n-------------------')
    print(f'Total Months: {totalMonths}\nTotal: ${totalProfitloss}')
    print(f'Average Change: ${round(avgChange,2)}')
    print(f'Greatest Increase in Profits: {max_prof_date} (${max_prof})')
    print(f'Greatest Decrease in Profits: {min_prof_date} (${min_prof})')

    ##Output results to txt file using 'sys' dependancy
    txtpath = os.path.join('analysis', 'analysis.txt')

    with open(txtpath, 'w') as txtfile:

        print(f'\n\nFinancial Analysis\n-------------------', file=txtfile)
        print(f'Total Months: {totalMonths}\nTotal: ${totalProfitloss}', file=txtfile)
        print(f'Average Change: ${round(avgChange,2)}', file=txtfile)
        print(f'Greatest Increase in Profits: {max_prof_date} (${max_prof})', file=txtfile)
        print(f'Greatest Decrease in Profits: {min_prof_date} (${min_prof})', file=txtfile)

        txtfile.close()

csvfile.close()
