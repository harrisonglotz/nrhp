#!/usr/bin/env python3
import pandas as pd
import sqlite3
import requests

#get latest verison of the spreadsheet and download
url = 'https://www.nps.gov/subjects/nationalregister/upload/national_register_listed_20200108.xlsx'
r = requests.get(url, allow_redirects=True)
open('nrhp.xlsx', 'wb').write(r.content)

#name database
dbname = 'nrhp'

#connect to database
conn = sqlite3.connect(dbname + '.sqlite')

#read excel file with pandas
df = pd.read_excel('nrhp.xlsx')

#convert dataframe into a sqlite file
df.to_sql(name='AdvSearchResults', con=conn)
