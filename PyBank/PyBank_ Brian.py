# -*- coding: UTF-8 -*-

# Dependencies
import csv
import os

filepath = "C:/Users/Brian/OneDrive/Desktop/UCF BOOT CAMP/UCF BOOT CAMP _ Brian M/Homeworks_Brian M/03-Python/Starter_Code/PyBank/Resources/budget_data - Copy.csv"
# Define variables to track the financial data
total_months = 0
total_profit =0
average_change = 0
profit_change = 0
current_profits=0
prev_profit = 0
decrease_profit=0
increase_profit=0
last_month_profit=0
max_diffrence = 0
small_diffrence = 0
max_month = ""
small_month = ""

# Code ripped 3.2.8
with open(filepath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
     csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first 
     csv_header = next(csvreader)
     #print(f"CSV Header: {csv_header}")

#current_month = row
  
    # for loop 
     for row in csvreader:
          #print(type(row), row)
          total_profit += int(row[1]) # (row = row by row )
          total_months += 1    # total_months = total_months + 1
        

     if total_months == 1 :
          last =int(row[1])
     else :
          current_profits += int(row[1])
    
     profit_change = current_profits-last_month_profit
     
# max diffrence
     if profit_change > max_diffrence:
          max_diffrence = profit_change
          max_month = row[0]
#min diffrence
     if profit_change < small_diffrence:
          small_diffrence = profit_change
          small_month = row[0]
          
     output = f"""
      data
-----------------------------

 Total Months: {total_months}
 Total : ${total_profit}
 Average Change: $ {( total_profit/total_months - 1 )} # average is the sum of profit/loss divided by 86 the number of months
Greatest Decrease Profit : {small_month} ({small_diffrence})
Greatest Increase Profit : {max_month}({max_diffrence})
"""

     print(output)