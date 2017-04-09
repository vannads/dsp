# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import csv
#from pprint import pprint
infile = csv.DictReader(open("~/football.csv"))
topTeams = []
team =()
for row in infile:
    team = (row["Team"], abs(int(row["Goals"]) - int(row["Goals Allowed"])))
    topTeams.append(team)
topList = sorted(topTeams, key = lambda teamSort : teamSort[1])
#pprint(topList) #Print the complete list of teams and difference in ‘for’ and ‘against’ goals
print("Team with smallest difference in ‘for’ and ‘against’ goals:", topList[0][0])
