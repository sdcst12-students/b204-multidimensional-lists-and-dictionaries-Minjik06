#!python3

'''
Create a program to iterate through the games and determine the win loss record 
for each time

Create a dictionary for each team and store their number of wins, games played,
goals for and goals against.  A dictionary template has been prepped for you to 
use, although you can probably build one faster using iteration or list comprehension
'''

teams = ['AB','BC','MN','SK','ON','QC','PE','NS','NB','NL','YT','NT','NU']
games = [{'home': 'BC', 'homeScore': 0, 'away': 'YT', 'awayScore': 0},
     {'home': 'NU', 'homeScore': 2, 'away': 'NS', 'awayScore': 2}, {'home': 'PE', 'homeScore': 0, 'away': 'YT', 'awayScore': 2}, 
     {'home': 'NU', 'homeScore': 1, 'away': 'YT', 'awayScore': 3}, {'home': 'NT', 'homeScore': 3, 'away': 'ON', 'awayScore': 1}, 
     {'home': 'NU', 'homeScore': 2, 'away': 'ON', 'awayScore': 1}, {'home': 'BC', 'homeScore': 0, 'away': 'SK', 'awayScore': 3}, 
     {'home': 'SK', 'homeScore': 2, 'away': 'NU', 'awayScore': 0}, {'home': 'MN', 'homeScore': 1, 'away': 'NS', 'awayScore': 3}, 
     {'home': 'ON', 'homeScore': 0, 'away': 'AB', 'awayScore': 1}, {'home': 'MN', 'homeScore': 3, 'away': 'NU', 'awayScore': 2},
     {'home': 'NB', 'homeScore': 0, 'away': 'NL', 'awayScore': 1}, {'home': 'BC', 'homeScore': 3, 'away': 'NT', 'awayScore': 2}, 
     {'home': 'ON', 'homeScore': 1, 'away': 'NU', 'awayScore': 3}, {'home': 'NS', 'homeScore': 1, 'away': 'ON', 'awayScore': 1}, 
     {'home': 'NL', 'homeScore': 3, 'away': 'BC', 'awayScore': 1}, {'home': 'NL', 'homeScore': 2, 'away': 'NT', 'awayScore': 1}, 
     {'home': 'NU', 'homeScore': 2, 'away': 'AB', 'awayScore': 3}, {'home': 'MN', 'homeScore': 1, 'away': 'YT', 'awayScore': 1}, 
     {'home': 'BC', 'homeScore': 1, 'away': 'PE', 'awayScore': 0}, {'home': 'QC', 'homeScore': 1, 'away': 'NL', 'awayScore': 0}, 
     {'home': 'NL', 'homeScore': 1, 'away': 'NT', 'awayScore': 3}, {'home': 'BC', 'homeScore': 1, 'away': 'ON', 'awayScore': 0}, 
     {'home': 'SK', 'homeScore': 0, 'away': 'AB', 'awayScore': 1}, {'home': 'YT', 'homeScore': 2, 'away': 'QC', 'awayScore': 2}, 
     {'home': 'NT', 'homeScore': 2, 'away': 'NU', 'awayScore': 3}, {'home': 'NB', 'homeScore': 2, 'away': 'NT', 'awayScore': 2}, 
     {'home': 'PE', 'homeScore': 2, 'away': 'BC', 'awayScore': 0}, {'home': 'PE', 'homeScore': 2, 'away': 'NB', 'awayScore': 0}, 
     {'home': 'PE', 'homeScore': 0, 'away': 'YT', 'awayScore': 0}, {'home': 'NB', 'homeScore': 3, 'away': 'MN', 'awayScore': 2}, 
     {'home': 'AB', 'homeScore': 0, 'away': 'NL', 'awayScore': 2}, {'home': 'QC', 'homeScore': 2, 'away': 'NL', 'awayScore': 1}, 
     {'home': 'SK', 'homeScore': 0, 'away': 'MN', 'awayScore': 0}, {'home': 'QC', 'homeScore': 2, 'away': 'BC', 'awayScore': 3}, 
     {'home': 'NU', 'homeScore': 2, 'away': 'AB', 'awayScore': 2}, {'home': 'NS', 'homeScore': 3, 'away': 'AB', 'awayScore': 3}, 
     {'home': 'QC', 'homeScore': 1, 'away': 'NT', 'awayScore': 1}, {'home': 'SK', 'homeScore': 3, 'away': 'AB', 'awayScore': 0}, 
     {'home': 'NL', 'homeScore': 3, 'away': 'QC', 'awayScore': 1}, {'home': 'NL', 'homeScore': 2, 'away': 'SK', 'awayScore': 1}, 
     {'home': 'YT', 'homeScore': 1, 'away': 'BC', 'awayScore': 3}, {'home': 'NL', 'homeScore': 2, 'away': 'PE', 'awayScore': 2}, 
     {'home': 'YT', 'homeScore': 1, 'away': 'NL', 'awayScore': 1}, {'home': 'NS', 'homeScore': 0, 'away': 'QC', 'awayScore': 1}, 
     {'home': 'BC', 'homeScore': 1, 'away': 'NB', 'awayScore': 3}, {'home': 'NL', 'homeScore': 3, 'away': 'NU', 'awayScore': 1}, 
     {'home': 'QC', 'homeScore': 0, 'away': 'SK', 'awayScore': 0}, {'home': 'NS', 'homeScore': 0, 'away': 'SK', 'awayScore': 0}, 
     {'home': 'AB', 'homeScore': 1, 'away': 'NT', 'awayScore': 2}, {'home': 'YT', 'homeScore': 2, 'away': 'QC', 'awayScore': 2}, 
     {'home': 'YT', 'homeScore': 1, 'away': 'NB', 'awayScore': 3}, {'home': 'NT', 'homeScore': 0, 'away': 'QC', 'awayScore': 2}, 
     {'home': 'ON', 'homeScore': 2, 'away': 'BC', 'awayScore': 2}, {'home': 'BC', 'homeScore': 0, 'away': 'ON', 'awayScore': 1}, 
     {'home': 'MN', 'homeScore': 1, 'away': 'ON', 'awayScore': 3}, {'home': 'SK', 'homeScore': 2, 'away': 'NU', 'awayScore': 1}, 
     {'home': 'MN', 'homeScore': 3, 'away': 'PE', 'awayScore': 1}, {'home': 'NU', 'homeScore': 2, 'away': 'YT', 'awayScore': 3}, 
     {'home': 'AB', 'homeScore': 0, 'away': 'NT', 'awayScore': 0}]
teamData = {
    'AB' : {
        'gamesPlayed' : 0,
        'wins' : 0,
        'losses' : 0,
        'ties' : 0,
        'goalsFor' : 0,
        'goalsAgainst' : 0
    },
}



def app():
    teamData['BC']={
        'gamesPlayed' : 0,
        'wins' : 0,
        'losses' : 0,
        'ties' : 0,
        'goalsFor' : 0,
        'goalsAgainst' : 0
    }
    teamData['MN']={
        'gamesPlayed' : 0,
        'wins' : 0,
        'losses' : 0,
        'ties' : 0,
        'goalsFor' : 0,
        'goalsAgainst' : 0
    }
    teamData['SK']={
        'gamesPlayed' : 0,
        'wins' : 0,
        'losses' : 0,
        'ties' : 0,
        'goalsFor' : 0,
        'goalsAgainst' : 0
    }
    teamData['ON']={
        'gamesPlayed' : 0,
        'wins' : 0,
        'losses' : 0,
        'ties' : 0,
        'goalsFor' : 0,
        'goalsAgainst' : 0
    }
    teamData['QC']={
        'gamesPlayed' : 0,
        'wins' : 0,
        'losses' : 0,
        'ties' : 0,
        'goalsFor' : 0,
        'goalsAgainst' : 0
    }
    teamData['PE']={
        'gamesPlayed' : 0,
        'wins' : 0,
        'losses' : 0,
        'ties' : 0,
        'goalsFor' : 0,
        'goalsAgainst' : 0
    }
    teamData['NS']={
        'gamesPlayed' : 0,
        'wins' : 0,
        'losses' : 0,
        'ties' : 0,
        'goalsFor' : 0,
        'goalsAgainst' : 0
    }
    teamData['NB']={
        'gamesPlayed' : 0,
        'wins' : 0,
        'losses' : 0,
        'ties' : 0,
        'goalsFor' : 0,
        'goalsAgainst' : 0
    }
    teamData['NL']={
        'gamesPlayed' : 0,
        'wins' : 0,
        'losses' : 0,
        'ties' : 0,
        'goalsFor' : 0,
        'goalsAgainst' : 0
    }
    teamData['YT']={
        'gamesPlayed' : 0,
        'wins' : 0,
        'losses' : 0,
        'ties' : 0,
        'goalsFor' : 0,
        'goalsAgainst' : 0
    }
    teamData['NT']={
        'gamesPlayed' : 0,
        'wins' : 0,
        'losses' : 0,
        'ties' : 0,
        'goalsFor' : 0,
        'goalsAgainst' : 0
    }
    teamData['NU']={
        'gamesPlayed' : 0,
        'wins' : 0,
        'losses' : 0,
        'ties' : 0,
        'goalsFor' : 0,
        'goalsAgainst' : 0
    }

lengthg=len([d for d in games if isinstance(d, dict)])
   
def score():
    for i in range(lengthg):
        if games[i]['home']=='AB' or games[i]['away']=='AB':
            teamData['AB']['gamesPlayed']+=1
            if games[i]['homeScore']<games[i]['awayScore']:
                teamData['AB']['losses']+=1
            elif games[i]['homeScore']>games[i]['awayScore']:
                teamData['AB']['wins']+=1
            else:
                teamData['AB']['ties']+=1
            teamData['AB']['goalsFor']+=games[i]['homeScore']
            teamData['AB']['goalsAgainst']+=games[i]['awayScore']
        elif games[i]['home']=='BC'or games[i]['away']=='BC':
            teamData['BC']['gamesPlayed']+=1
            if games[i]['homeScore']<games[i]['awayScore']:
                teamData['BC']['losses']+=1
            elif games[i]['homeScore']>games[i]['awayScore']:
                teamData['BC']['wins']+=1
            else:
                teamData['BC']['ties']+=1
            teamData['BC']['goalsFor']+=games[i]['homeScore']
            teamData['BC']['goalsAgainst']+=games[i]['awayScore']
        elif games[i]['home']=='MN' or games[i]['away']=='MN':
            teamData['MN']['gamesPlayed']+=1
            if games[i]['homeScore']<games[i]['awayScore']:
                teamData['MN']['losses']+=1
            elif games[i]['homeScore']>games[i]['awayScore']:
                teamData['MN']['wins']+=1
            else:
                teamData['MN']['ties']+=1
            teamData['MN']['goalsFor']+=games[i]['homeScore']
            teamData['MN']['goalsAgainst']+=games[i]['awayScore']
        elif games[i]['home']=='SK'or games[i]['away']=='SK':
            teamData['SK']['gamesPlayed']+=1
            if games[i]['homeScore']<games[i]['awayScore']:
                teamData['SK']['losses']+=1
            elif games[i]['homeScore']>games[i]['awayScore']:
                teamData['SK']['wins']+=1
            else:
                teamData['SK']['ties']+=1
            teamData['SK']['goalsFor']+=games[i]['homeScore']
            teamData['SK']['goalsAgainst']+=games[i]['awayScore']
        elif games[i]['home']=='ON' or games[i]['away']=='ON':
            teamData['ON']['gamesPlayed']+=1
            if games[i]['homeScore']<games[i]['awayScore']:
                teamData['ON']['losses']+=1
            elif games[i]['homeScore']>games[i]['awayScore']:
                teamData['ON']['wins']+=1
            else:
                teamData['ON']['ties']+=1
            teamData['ON']['goalsFor']+=games[i]['homeScore']
            teamData['ON']['goalsAgainst']+=games[i]['awayScore']
        elif games[i]['home']=='QC' or games[i]['away']=='QC':
            teamData['QC']['gamesPlayed']+=1
            if games[i]['homeScore']<games[i]['awayScore']:
                teamData['QC']['losses']+=1
            elif games[i]['homeScore']>games[i]['awayScore']:
                teamData['QC']['wins']+=1
            else:
                teamData['QC']['ties']+=1
            teamData['QC']['goalsFor']+=games[i]['homeScore']
            teamData['QC']['goalsAgainst']+=games[i]['awayScore']
        elif games[i]['home']=='PE' or games[i]['away']=='PE':
            teamData['PE']['gamesPlayed']+=1
            if games[i]['homeScore']<games[i]['awayScore']:
                teamData['PE']['losses']+=1
            elif games[i]['homeScore']>games[i]['awayScore']:
                teamData['PE']['wins']+=1
            else:
                teamData['PE']['ties']+=1
            teamData['PE']['goalsFor']+=games[i]['homeScore']
            teamData['PE']['goalsAgainst']+=games[i]['awayScore']
        elif games[i]['home']=='NS'or games[i]['away']=='NS':
            teamData['NS']['gamesPlayed']+=1
            if games[i]['homeScore']<games[i]['awayScore']:
                teamData['NS']['losses']+=1
            elif games[i]['homeScore']>games[i]['awayScore']:
                teamData['NS']['wins']+=1
            else:
                teamData['NS']['ties']+=1
            teamData['NS']['goalsFor']+=games[i]['homeScore']
            teamData['NS']['goalsAgainst']+=games[i]['awayScore']
        elif games[i]['home']=='NB'or games[i]['away']=='NB':
            teamData['NB']['gamesPlayed']+=1
            if games[i]['homeScore']<games[i]['awayScore']:
                teamData['NB']['losses']+=1
            elif games[i]['homeScore']>games[i]['awayScore']:
                teamData['NB']['wins']+=1
            else:
                teamData['NB']['ties']+=1
            teamData['NB']['goalsFor']+=games[i]['homeScore']
            teamData['NB']['goalsAgainst']+=games[i]['awayScore']
        elif games[i]['home']=='NL'or games[i]['away']=='NL':
            teamData['NL']['gamesPlayed']+=1
            if games[i]['homeScore']<games[i]['awayScore']:
                teamData['NL']['losses']+=1
            elif games[i]['homeScore']>games[i]['awayScore']:
                teamData['NL']['wins']+=1
            else:
                teamData['NL']['ties']+=1
            teamData['NL']['goalsFor']+=games[i]['homeScore']
            teamData['NL']['goalsAgainst']+=games[i]['awayScore']
        elif games[i]['home']=='YT'or games[i]['away']=='YT':
            teamData['YT']['gamesPlayed']+=1
            if games[i]['homeScore']<games[i]['awayScore']:
                teamData['YT']['losses']+=1
            elif games[i]['homeScore']>games[i]['awayScore']:
                teamData['YT']['wins']+=1
            else:
                teamData['YT']['ties']+=1
            teamData['YT']['goalsFor']+=games[i]['homeScore']
            teamData['YT']['goalsAgainst']+=games[i]['awayScore']
        elif games[i]['home']=='NT'or games[i]['away']=='NT':
            teamData['NT']['gamesPlayed']+=1
            if games[i]['homeScore']<games[i]['awayScore']:
                teamData['NT']['losses']+=1
            elif games[i]['homeScore']>games[i]['awayScore']:
                teamData['NT']['wins']+=1
            else:
                teamData['NT']['ties']+=1
            teamData['NT']['goalsFor']+=games[i]['homeScore']
            teamData['NT']['goalsAgainst']+=games[i]['awayScore']
        elif games[i]['home']=='NU'or games[i]['away']=='NU':
            teamData['NU']['gamesPlayed']+=1
            if games[i]['homeScore']<games[i]['awayScore']:
                teamData['NU']['losses']+=1
            elif games[i]['homeScore']>games[i]['awayScore']:
                teamData['NU']['wins']+=1
            else:
                teamData['NU']['ties']+=1
            teamData['NU']['goalsFor']+=games[i]['homeScore']
            teamData['NU']['goalsAgainst']+=games[i]['awayScore']

def tests():
    assert teamData['BC']['gamesPlayed'] == 12
    assert teamData['BC']['wins'] == 5

app()
score()
tests()

#print(teamData['NK']['gamesPlayed'])

