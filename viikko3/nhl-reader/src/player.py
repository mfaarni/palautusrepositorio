import requests
class PlayerReader:

    def __init__(self, url):
        self.url = url
        self.players = []

    def get_players(self):
        response = requests.get(self.url).json()
        players = []
        for player_dict in response:
            player = Player(
                player_dict['name'],
                player_dict['nationality'],
                player_dict['assists'],
                player_dict['goals'],
                player_dict['penalties'],
                player_dict['team'],
                player_dict['games'],
            )

            players.append(player)
        return players

class Player:
    def __init__(self, name, nationality, assists, goals, penalties, team, games):
        self.name = name
        self.nationality = nationality
        self.assists = assists
        self.goals = goals 
        self.penalties = penalties
        self.team = team
        self.games = games
    
    def __str__(self):
        return f"{self.name:20} {self.team} {self.goals:2} + {self.assists:2} = {self.goals+self.assists}"

class PlayerStats:

    def __init__(self, reader):
        self.reader = reader
    
    def top_scorers_by_nationality(self, nationality):
        players = []
        for player in self.reader.get_players():
            if str(player.nationality) == nationality:
                players.append(player)
        
        players.sort(key=lambda player: (player.goals+player.assists), reverse=True)
        for player in players:
            print(player)