
# coding: utf-8

# In[123]:


import pandas as pd
import re

def processAddress(row):
    split_address = row.replace('[', '')
    split_address = split_address.replace(']', '')
    split_address = split_address.replace(r'\n', '')
    split_address = split_address.split(",")
    
    split_address = [elem.replace('"', '') for elem in split_address]
    split_address = [elem.replace("'", '') for elem in split_address]
    split_address = ''.join(str(elem) +", " for elem in split_address if elem.rstrip() != "")
#     split_address = split_address.replace(", ","")
    return split_address.rstrip().upper()

ADDRESS_IDENTIFIERS = ["ST", "CIR", "RD", "AVE", "LN", "UNKNOWN", "ROAD", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE", "TEN"]
def hasNumbersOrStreetIdentifiers(inputString):
    hasNumbers = any(char.isdigit() for char in inputString)
    hasIdentifiers = any(findWholeWord(identifier)(inputString) for identifier in ADDRESS_IDENTIFIERS)
    return hasNumbers or hasIdentifiers

def findWholeWord(w):
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search

def returnFirstTrue(address_list):
    for i in range(0, len(address_list)):
        if hasNumbersOrStreetIdentifiers(address_list[i]):
            return i
    return -1

def extractAddress(address_string):
    if returnFirstTrue(address_string.split(",")) >= 0:
        return ''.join(address_string.split(",")[returnFirstTrue(address_string.split(",")):])
    else:
        return "UNKNOWN"


# In[124]:


CHUNK = "Chunk_2000000"
df = pd.read_csv(CHUNK + ".csv")
df["Address Complete"] = df.Address.apply(processAddress)
df["Address Extracted"] = df["Address Complete"].apply(extractAddress)

    
# In[125]:


df.to_csv(CHUNK + "_Cleaned_Addresses.csv")


# In[126]:


df

