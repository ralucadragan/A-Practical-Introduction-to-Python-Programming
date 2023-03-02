'''
5. Repeatedly ask the user to enter a team name and the how many games the team won and
how many they lost. Store this information in a dictionary where the keys are the team names
and the values are lists of the form [wins, losses].
(a) Using the dictionary created above, allow the user to enter a team name and print out
the team’s winning percentage.
(b) Using the dictionary, create a list whose entries are the number of wins of each team.
(c) Using the dictionary, create a list of all those teams that have winning records.
'''

dict = {}

team_name = input('Enter your team name: ')
games_won = int(input('Enter haw many games thy won: '))
games_lost = int(input('Enter haw many games thy lost: '))

dict[team_name] = [games_won, games_lost]
print(dict)

team = {
    'a' : [1,2], 'b' : [2,3], 'c' : [3,4],
    'd' : [4,5], 'e' : [5,4], 'f' : [4,1]
}
# (a) Using the dictionary created above, allow the user to enter a team name and print out
# the team’s winning percentage.

ask1 = input("Enter a team name: ")
for k,v in team.items():
    if k == ask1:
        print(f'The team - {k} - as won {v[0]} times!')

# (b) Using the dictionary, create a list whose entries are the number of wins of each team.

list_win = []
for k,v in team.items():
    list_win.append(v[0])
print(f'The list of scores of wins: {list_win}')

# (c) Using the dictionary, create a list of all those teams that have winning records.

list_teams = []

for k,v in team.items():
    if v[0] > 0 and v[0] > v[1]:
        list_teams.append(k)
print(f'The liste of teams that have winning records: {list_teams}')


