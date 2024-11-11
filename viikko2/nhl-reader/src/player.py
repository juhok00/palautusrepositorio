class Player:
	def __init__(self, data):
		self.name = data["name"]
		self.nationality = data.get("nationality", "")
		self.assists = data.get("assists", 0)
		self.goals = data.get("goals", 0)
		self.team = data.get("team", "")
		self.games = data.get("games", 0)
		self.id = data.get("id", 0)


	def total_points(self):
		return self.goals + self.assists

    
	def __str__(self):
		return f"{self.name:20} {self.team} {self.goals} + {self.assists} = {self.total_points()}"
