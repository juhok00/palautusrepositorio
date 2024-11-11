import requests
from player import Player
from rich.console import Console
from rich.table import Table


class PlayerReader:
	def __init__(self, url):
		self.url = url

	def get_players(self):
		response = requests.get(self.url).json()

		return [Player(player_dict) for player_dict in response]


class PlayerStats:
	def __init__(self, reader):
		self.players = reader.get_players()

	def top_scorers_by_nationality(self, nationality):
		filtered = filter(lambda p: p.nationality == nationality, self.players)
		
		return sorted(filtered, key=lambda p: p.total_points(), reverse =True)

def main():	
	console = Console()

	season = input("Select season: ")
	nationality = input("Select nationality: ")




	url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
	reader = PlayerReader(url)
	stats = PlayerStats(reader)
	
	players = stats.top_scorers_by_nationality(nationality)        


	table = Table(title=f"Top scorers of {nationality} season {season}")

	table.add_column("name", justify="left")
	table.add_column("team", justify="center")
	table.add_column("goals", justify="right")
	table.add_column("assists", justify="right")
	table.add_column("points", justify="right")
        
	for player in players:
		table.add_row(
			player.name,
			player.team,
			str(player.goals),
			str(player.assists),
			str(player.total_points())
		)

	console.print(table)


if __name__ == "__main__":
	main()
