"""
Simple example for loading JSON data into a list.


"""


import json
import pandas as pd

jsonSales = {}

# please adapt the path accordingly to your settings
with open('Code\python_exercises\load json and db for cleansing\SalesRecords.json') \
    as in_file:
        jsonSales = json.load(in_file)
        
#print(jsonSales['SalesRecords'][0:])

df_merged = pd.DataFrame()

# print((jsonSales['SalesRecords'][0]).len)
for salesrecord in jsonSales['SalesRecords']:
    df = pd.DataFrame.from_dict(salesrecord, orient ='index')
    print(df)
    df_merged = pd.concat([df, df_merged], ignore_index=False)

print (df_merged)
