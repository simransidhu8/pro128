from bs4 import BeautifulSoup as bs 
import requests 
import pandas as pd

START_URL = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'

page = requests.get(START_URL)
print(page)

Star_Name = []
Distance = []
Mass = []
Radius = []
Lum = []

soup= bs(page.text, 'html.parser')
star_table = soup.find('table')

temp_list = []
table_rows = star_table.find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

for i in range(1, len(temp_list)):
    Star_Name.append(temp_list[i][1])
    Distance.append(temp_list[i][3])
    Mass.append(temp_list[i][5])
    Radius.append(temp_list[i][6])
    Lum.append(temp_list[i][7])

df = pd.DataFrame(list(zip(Star_Name, Distance, Mass, Radius, Lum)), columns = ['Star Name', 'Distance', 'Mass', 'Radius', "Luminosity"])
print(df)

df.to_csv('bright_stars.csv')