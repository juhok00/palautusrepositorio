from urllib import request
from project import Project
import tomli


class ProjectReader:
	def __init__(self, url):
		self._url = url

	
	def get_project(self):
		# tiedoston merkkijonomuotoinen sisältö
		content = request.urlopen(self._url).read().decode("utf-8")	

	        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
		data = tomli.loads(content)



		self.name = data["tool"]["poetry"]["name"]
		self.description = data["tool"]["poetry"]["description"]
		self.license = data["tool"]["poetry"].get("license", "N/A")
		self.authors = data["tool"]["poetry"].get("authors", [])
		self.dependencies = list(data["tool"]["poetry"]["dependencies"].keys())
		self.dev_dependencies = list(data["tool"]["poetry"]["group"]["dev"]["dependencies"].keys())






		return self

		
	def __str__(self):
		result = f"Name: {self.name}\n"
		result += f"Description: {self.description}\n"
		result += f"License: {self.license}\n"


		if self.authors:
			result += "\nAuthors:\n"
			for author in self.authors:
				result += f"- {author}\n"

		if self.dependencies:
			result += "\nDependencies:\n"
			for dep in self.dependencies:
				result += f"- {dep}\n"

		if self.dev_dependencies:
			result += "\nDevelopment dependencies:\n"
			for dev_dep in self.dev_dependencies:
				result += f"- {dev_dep}\n"

		return result.strip()
