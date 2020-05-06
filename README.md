# NRHP
These scripts a.) create a sqlite database of all current National Register of Historic Places listings and b.) provide the current listings in a given locality and print information about a selcted listing.

Due to the size of the National Register of Historic Places, the database creation is a separate script. I encourage anyone using this to run it every week or so to ensure accurate listing data.

# Run the scripts

Create the database by running create_nrhp_db.py:
```
$ python3 create_nrhp_db.py  #run weekly to update new listings
```
In the same directory of the newly created .sqlite database, run the search script:
```
$ python3 search_nrhp.py
```
In it's current form, the query script will return all listings in a given locality (sorted alphabetically) and give the user an option to access the address/location and external link for further research.
```
$ python3 search_nrhp.py
Enter state: virginia
Enter county (leave blank if city): greene
Enter city (leave blank if county): 

There are 7 NRHP Listings in Greene County, Virginia: 
1: Beadles House
2: Gibson Memorial Chapel and Martha Bagby Battle House at Blue Ridge School
3: Greene County Courthouse
4: Locust Grove
5: Octonia Stone
6: Powell--McMullan House
7: Stanardsville Historic District

Enter listing # for more information: 1

Information for Beadles House:
Address/Location: 515 Greene Acres Rd.
External Link: https://catalog.archives.gov/id/41681015
```

Unfortunately, some addresses provided by the NPS are vague, and will only give general descriptions based on state routes. Along with this, even very well known listings are missing external links:
```
Information for Tuckahoe:
Address/Location: SE of Manakin near jct. of Rtes. 650 and 647
External Link: None
```

Listings with clear addresses can be mapped via Google Maps (addresses with only 1 street number are currently not supported). Because information data is inconsistant throughout the NPS database, you may get a false positive and Google Maps will not be able to link the listing.   



# Future Ideas
This project is still a work in progress and I hope to implement these features in the future:

-Ability to automatically fetch nomination pdfs for a specific listing, or for all listings in a given locality

-Map listings of a given locality for user interaction, directions, etc.

-National Historic Landmark support

# Contact
Shoot me an email at harrisonglotz28@gmail.com
