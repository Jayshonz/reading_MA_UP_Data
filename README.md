# reading_MA_UP_Data
MA for SF

# Read_Data
This script is built specifically for reading in the fixed-width .txt file of unclaimed property delivered by the UP division of the MA treasury. The data will be read into the a database with columns broken out for each of the properties of the records. 

Note: Addresses in this script will be lumped together into one single column.

Use the Address_cleaner.py script to clean these Addresses.

# address_cleaner

This script breaks out the single-column address into:
Street Address
Street Address 2
City 
State
Zip Code

Note: Zip Code could be further broken out to only include the first 5 digits and remove any instances where a zip+4 exists. 
