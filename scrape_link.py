import requests
from bs4 import BeautifulSoup

url = 'https://www.nps.gov/subjects/nationalregister/database-research.htm'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

pretty = soup.prettify()

file_name = pretty[20373:20381]

print(file_name)