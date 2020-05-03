#!/usr/bin/env python3
import pandas as pd
import sqlite3

#name database
dbname = 'nrhp'

#idk what this does tbh
conn = sqlite3.connect(dbname + '.sqlite')

#read excel file with pandas
df = pd.read_excel('nrhp.xlsx')

#convert datafram into a sqlite file
df.to_sql(name='AdvSearchResults', con=conn)

