#!/usr/bin/env python3
'''search_nrhp.py: a program to provide quick information for further reading into a property(s) listed on the 
   National Register of Historic Places.'''

import pandas
import sqlite3

conn = sqlite3.connect('nrhp.sqlite')
cur = conn.cursor()

#get user's state from command line and format for query
user_input_state = input('Enter state: ')
user_input_state = user_input_state.upper()
#format user's state for printing
user_input_state_pretty = user_input_state.lower()
user_input_state_pretty = user_input_state.capitalize()

#get user's county, if using, and format for query. Query and printing can use the same variable here, no need for two variables
user_input_county = input('Enter county (leave blank if city): ')
user_input_county = user_input_county.lower()
user_input_county = user_input_county.capitalize()

#get user's city, if using, and format for query. Query and printing can use the same variable here, no need for two variables
user_input_city = input('Enter city (leave blank if county): ')
user_input_city = user_input_city.lower()
user_input_city = user_input_city.capitalize()

if len(user_input_city) == 0:
	#get the amount of listings that match the search/query criteria 
	cur.execute(f"SELECT 'index' FROM AdvSearchResults WHERE State='{user_input_state}' AND County='{user_input_county}'")
	counter = 0
	for row in cur:
		counter = counter + 1
	print(f'\nThere are {counter} NRHP Listings in {user_input_county} County, {user_input_state_pretty}: ')

	#query relevant data
	cur.execute(f"SELECT Property_Name, External_Link, Street_And_Number FROM AdvSearchResults WHERE State='{user_input_state}' AND County='{user_input_county}'")
	i = 1
	counter = 0
	name_list = ["Place holder"]
	link_list = ["Placeholder"]
	address_list =["Placeholder"]

	#place external link, and address into lists for later use
	for row in cur:
		print(f'{i}: ' + row[0])
		name_list.append(row[0])
		link_list.append(row[1])
		address_list.append(row[2])
		i = i + 1
else:
	#get the amount of listings that match the search/query criteria 
	cur.execute(f"SELECT 'index' FROM AdvSearchResults WHERE State='{user_input_state}' AND City='{user_input_city}'")
	counter = 0
	for row in cur:
		counter = counter + 1
	print(f'\nThere are {counter} NRHP Listings in {user_input_city}, {user_input_state_pretty}: ')

	#query relevant data
	cur.execute(f"SELECT Property_Name, External_Link, Street_And_Number FROM AdvSearchResults WHERE State='{user_input_state}' AND City='{user_input_city}' OR City='{user_input_city} (Independent City)'")
	i = 1
	counter = 0
	name_list = ["Placeholder"]
	link_list = ["Placeholder"]
	address_list =["Placeholder"]
	#place external link, and address into lists for later use
	for row in cur:
		print(f'{i}: ' + row[0])
		name_list.append(row[0])
		link_list.append(row[1])
		address_list.append(row[2])
		i = i + 1

cur.close()


#prompt user to select a listing and turn into int
listing_selection = input("\nEnter listing # for more information: ")
listing_selection = int(listing_selection)

#assign variables based on selection
selected_name = name_list[listing_selection]
selected_address = address_list[listing_selection]
selected_external_link = link_list[listing_selection]

print(f"\nInformation for {selected_name}:") 
print(f"Address/Location: {selected_address}")
print(f"External Link: {selected_external_link}\n")




