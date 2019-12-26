#import libraries 
import os
import csv

#path the csv
csvpath = os.path.join("..", "assets", "budget_data.csv")

print(csvpath)

#define all variables
total_months = 0

#read the cvs file in assets 
with open(csvpath, newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

#create the loop to read through all the csv data sets
for row in csv_reader:
#create functions or define new variables that will target all the keys and values for

#total number of months
    total_months += 1
    print(total_months)

#net total for Profit/Losses over the entire period

#average change in Profit/Losses over the entire period

#greatest increase in Profit/Losses (date and amount) over the entire period

#greatest decrease in losses (date and amount over the entire period)

#print all reseults

#export out or write to text