#Dependencies
import os
import csv

#get csv from Resources file
poll_data_csv = os.path.join("Resources","election_data.csv")

#initialize variables for analysis as list
candidate_votes = {}
results = []

#open csv above in read-mode for use
with open(poll_data_csv, 'r') as data_csv:
    csv_reader = csv.reader(data_csv)
    next(csv_reader, None)   #skip first row, which is header

    #iterate a calculation from the rest of the rows
    for row in csv_reader:
        candidate = row[2]  
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

#Total votes cast 
vote_total = sum(candidate_votes.values())

#Percentage of Votes per Candidate 
for candidate, votes in candidate_votes.items():
    percent = (votes/vote_total) * 100
    election_results = f"{candidate}: {percent:.3f}% ({votes})"
    results.append(election_results)     #append format string to a list

#Max number of vote = election winner
winner = max(candidate_votes, key=candidate_votes.get)


#print info within Python
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(vote_total))
print("-------------------------")

for election_results in results:
    print(election_results)

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

#Output results to a text file named named "Poll_Analysis"
output_file = os.path.join("analysis", "Poll_Analysis.txt")

with open(output_file, 'w') as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {vote_total}\n")
    txtfile.write("-------------------------\n")
    for election_results in results:
        txtfile.write(election_results + "\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-------------------------\n")