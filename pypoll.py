# find sum of votes cast
# find list of candidates that received votes

import os
import csv

filepath = os.path.join("..", "Resources", "election_data.csv")


voterid= []
county = []
candidate = []
votecount = {}

with open(filepath, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = (next(csvreader))


    for row in csvreader:
        voterid.append(row[0])
        county.append(row[1])
        # candidate.append(row[2])

        politician = row[2]
        if politician not in candidate:
            candidate.append(politician)
        if politician not in votecount:
            votecount[politician] = 1
        else:
            votecount[politician] = votecount[politician] + 1

countofvotes = len(voterid)
# print(len(voterid))
# print(votecount)
# print(candidate)
results = ""
for x in candidate:
    results += f"{x}: {votecount[x]/(len(voterid))*100:.3f}% ({votecount[x]})\n"
# print(results)

winner = max(votecount.values())
for key, value in votecount.items():
        if value == winner:
            winning = key
            break
# print(winning)

# print("Total Votes : ", countofvotes)
# print(results)
# print(winning)


text_output = (
"Election Results\n"
"-------------------------------\n"
f"Total Votes : {countofvotes}\n"
"-------------------------------\n"
f"{results}"
"-------------------------------\n"
"-------------------------------\n"
f"Winner : {winning}\n"

)


file = "pypoll.txt"
with open (file, "w") as text:
        text.write(text_output)
        text.close