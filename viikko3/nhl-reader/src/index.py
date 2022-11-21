from player import PlayerReader, PlayerStats

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    reader = PlayerReader(url)
    reader.get_players()
    stats = PlayerStats(reader)
    stats.top_scorers_by_nationality("FIN")

    
main()
