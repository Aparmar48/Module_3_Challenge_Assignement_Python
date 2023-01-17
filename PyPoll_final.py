import os
import csv

csvpath = os.path.join("C:/Users/agp07/Instructions/PyPoll/Resources/election_data.csv")
with open(csvpath, newline ='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)

    count = 0
    candidatelist = []
    unique_candidate = []
    vote_count = []
    vote_percent = []

    for row in csvreader:
        count = count + 1
        candidatelist.append(row[2])
    for x in set(candidatelist):
        unique_candidate.append(x)
        y = candidatelist.count(x)
        vote_count.append(y)
        z = (y/count)*100
        vote_percent.append(z)

    winning_vote_count = max(vote_count)
    winner = unique_candidate[vote_count.index(winning_vote_count)]

    print("-----------------------------")
    print("Election Results")
    print("-----------------------------")
    print("Total Votes :" + str(count))
    print("------------------------------")
    for i in range(len(unique_candidate)):
        print(unique_candidate[i] + ":" + str(vote_percent[i]) +"% (" + str(vote_count[i])+ ")")
    print("-----------------------------")
    print("The winner is: " + winner)
    print("-----------------------------")

filename = os.path.join("C:/Users/agp07/Instructions/PyPoll/Resources/election_data.csv")
exportName = os.path.join("Desktop/results.txt")
           
