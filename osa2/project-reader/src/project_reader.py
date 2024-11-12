from urllib import request
from project import Project
import tomllib

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        try:
            content = request.urlopen(self._url).read().decode("utf-8")
           # print("alkuperäinen: ",content)
            data = tomllib.loads(content)
            #print("muutettu: ",data)
            nimi = data['tool']['poetry']['name']
            descr = data['tool']['poetry']['description']
            license = data['tool']['poetry']['license']
            authors = data['tool']['poetry']['authors']
            depe = data['tool']['poetry']['dependencies']
            devdepe = data['tool']['poetry']['group']['dev']['dependencies']
        except:
            print("Eipä toiminut oikein!")
        

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(nimi, descr, depe, devdepe, license, authors)

