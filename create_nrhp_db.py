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

#rename colums rows so there are no spaces
cur = conn.cursor()
cur.execute("ALTER TABLE 'AdvSearchResults' RENAME COLUMN 'Property Name' TO 'Property_Name'") 
cur.execute("ALTER TABLE 'AdvSearchResults' RENAME COLUMN 'Listed Date' TO 'Listed_Date'")
cur.execute("ALTER TABLE 'AdvSearchResults' RENAME COLUMN 'Ref#' TO 'Ref_Num'")
cur.execute("ALTER TABLE 'AdvSearchResults' RENAME COLUMN 'NHL Designated Date' TO 'NHL_Designated_Date'")
cur.execute("ALTER TABLE 'AdvSearchResults' RENAME COLUMN 'Restricted Address' TO 'Restricted_Address'")
cur.execute("ALTER TABLE 'AdvSearchResults' RENAME COLUMN 'Name of Multiple Property Listing' TO 'Name_Of_Multiple_Property_Listing'")
cur.execute("ALTER TABLE 'AdvSearchResults' RENAME COLUMN 'Street & Number' TO 'Street_And_Number'")
cur.execute("ALTER TABLE 'AdvSearchResults' RENAME COLUMN 'Federal Agencies' TO 'Federal_Agencies'")
cur.execute("ALTER TABLE 'AdvSearchResults' RENAME COLUMN 'Level of Significance - Local' TO 'Level_Of_Significance_Local'")
cur.execute("ALTER TABLE 'AdvSearchResults' RENAME COLUMN 'Level of Significance - State' TO 'Level_Of_Significance_State'")
cur.execute("ALTER TABLE 'AdvSearchResults' RENAME COLUMN 'Level of Significance - National' TO 'Level_Of_Significance_National'")
cur.execute("ALTER TABLE 'AdvSearchResults' RENAME COLUMN 'Level of Significance - International' TO 'Level_Of_Significance_International'")
cur.execute("ALTER TABLE 'AdvSearchResults' RENAME COLUMN 'Level of Significance - Not Indicated' TO 'Level_Of_Significance_Not_Indicated'")
cur.execute("ALTER TABLE 'AdvSearchResults' RENAME COLUMN 'Other Names' TO 'Other_Names'")
cur.execute("ALTER TABLE 'AdvSearchResults' RENAME COLUMN 'Park Name' TO 'Park_Name'")
cur.execute("ALTER TABLE 'AdvSearchResults' RENAME COLUMN 'Significant Persons' TO 'Significant_Persons'")
cur.execute("ALTER TABLE 'AdvSearchResults' RENAME COLUMN 'External Link' TO 'External_Link'")


