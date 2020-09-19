# Sum of months (length)
# Sum of profit/losses (sum all numbers)
# Average change month to month ()
# Biggest one month increase profit (date and amount)
# Biggest decrease in losses one month (date and amount)


import csv
import os

csvpath = os.path.join('..','Resources','budget_data.csv')
months = 0
revenue= 0
date = []
profitloss = []
difflist = []
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    # print(csvreader)
    for row in csvreader:
        date.append(row[0])
# print(date)
        profitloss.append(int(row[1]))
# print(profitloss)
        # print(months)

# print(diff)
for x in range(1,len(profitloss)):
    diff = profitloss[x] - profitloss[x-1]
    difflist.append(diff)
# print(sum(difflist))

sumofdiff = sum(difflist)
lengthofdifflist = len(difflist)
averagechange = sumofdiff/lengthofdifflist
# print(averagechange)

maxincrease = max(difflist)
indexofmaxincrease = difflist.index(maxincrease)
maxincreasemonths = date[indexofmaxincrease + 1]
# print(maxincreasemonths)

maxdecrease = min(difflist)
indexofmaxdecrease = difflist.index(maxdecrease)
maxdecreasemonths = date[indexofmaxdecrease + 1] 
# print(maxdecreasemonths)

months = len(date)
revenue = sum(profitloss)

# print(diff)    
# print(date)
# print(len(date))
# print(profitloss)
# print(len(profitloss))

text_output = (
        "Financial Analysis\n"
        "-------------------------------\n"
f"Total Months : , {months}\n"
f"Total : , {revenue}\n"
f"Average Change : , {round(averagechange)}\n"
f"Greatest Increase in Profits: , ${maxincrease}\n"
f"Greatest Decrease in Losses:, ${maxdecrease}\n"
)

# to print to a text file
file = "pypank.txt"
with open (file, "w") as text:
        text.write(text_output)
        text.close

print("Total Months : ", months)
print("Total : " , revenue)
print("Average Change : ", (round(averagechange)))
print("Greatest Increase in Profits:" , "$",maxincrease)
print("Greatest Decrease in Losses:" , "$",maxdecrease)


    
