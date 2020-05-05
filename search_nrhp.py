#!/usr/bin/env python3
#query_sql.py - this currently just searches and returns listings in given locality, 
#but can be changed quickly to return other data from the database.
import pandas
import sqlite3

conn = sqlite3.connect('nrhp.sqlite')
cur = conn.cursor()

#get user's state from command line
user_input_state = input('Enter state: ')
user_input_state = user_input_state.upper()
user_input_state_pretty = user_input_state.lower()
user_input_state_pretty = user_input_state.capitalize()

#get user's county, if using
user_input_county = input('Enter county (leave blank if city): ')
user_input_county = user_input_county.lower()
user_input_county = user_input_county.capitalize()

#get user's city, if using
user_input_city = input('Enter city (leave blank if county): ')
user_input_city = user_input_city.lower()
user_input_city = user_input_city.capitalize()

if len(user_input_city) == 0:
	#get # of hits with the inputted critera
	cur.execute(f"SELECT 'index' FROM AdvSearchResults WHERE State='{user_input_state}' AND County='{user_input_county}'")
	counter = 0
	for row in cur:
		counter = counter + 1
		
	#return data from query and place external_link in list
	cur.execute(f"SELECT Property_Name, External_Link FROM AdvSearchResults WHERE State='{user_input_state}' AND County='{user_input_county}'")
	i = 1
	print(f'\nThere are {counter} NRHP Listings in {user_input_county} County, {user_input_state_pretty}: ')
	counter = 0
	link_list = ["Placeholder"]
	for row in cur:
		print(f'{i}: ' + row[0])
		link_list.append(row[1])
		i = i + 1

else:
		#get # of hits with the inputted critera
	cur.execute(f"SELECT 'index' FROM AdvSearchResults WHERE State='{user_input_state}' AND City='{user_input_city}'")
	counter = 0
	for row in cur:
		counter = counter + 1

	#return data from query and place external_link in list
	cur.execute(f"SELECT Property_Name, External_Link FROM AdvSearchResults WHERE State='{user_input_state}' AND City='{user_input_city}'")
	i = 1
	print(f'\nThere are {counter} NRHP Listings in {user_input_city}, {user_input_state_pretty}: ')
	counter = 0
	link_list = ["Placeholder"]
	for row in cur:
		print(f'{i}: ' + row[0])
		link_list.append(row[1])
		i = i + 1

cur.close()

#prompt user for listing selection
listing_selection = input("\nEnter the number of listing for more information: ")
listing_selection = int(listing_selection)
print("The nomination form for this listing is located at: ") 
print(link_list[listing_selection])




