
# coding: utf-8

# In[114]:


import pandas as pd
import csv
import re

f = open("Massachusetts_Unclaimed_Property_20191113.txt", 'rt', encoding="utf")
linenumber = 1
data = []
manual_fix_required = []

row = True

try:
    while row:
        row = f.readline()
        if row:
            linenumber += 1
            split_data = re.split(r"\s{3,100}", row)
            if(linenumber > 3):
                if(len(split_data) > 7):
                    data_row = {}
                    data_row["Property ID"] = split_data[0]
                    data_row["Property Received Date"] = split_data[1].split(" ")[0]
                    data_row["Property Type Code"] = split_data[1].split(" ")[-1]
                    data_row["Holder Name"] = split_data[2]
                    data_row["Report Year"] = split_data[4]
                    data_row["Reported Cash"] = split_data[5]
                    data_row["Reported Shares"] = split_data[6]
                    data_row["Reported Tangible Items"] = split_data[7]
                    data_row["Address"] = split_data[8:]
                    data.append(data_row)
                else:
                    manual_fix_required.append(row)
            if linenumber % 1000000 == 0:
                print("Writing Chunk " + str(linenumber))
                df = pd.DataFrame(data)
                print(df.shape)
                df.to_csv("Chunk_" + str(linenumber) + ".csv")
                data = []
            print(linenumber, end="\r")
except e:
    print(e)
    print (("Error line %d" % (linenumber)))
#         continue



#%%
