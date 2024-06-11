import json
import pandas as pd

# some pandas settings for displaying the data
pd.set_option('display.max_columns', 20)
pd.set_option('display.max_rows', 10)
pd.set_option('display.max_colwidth', 90)
pd.set_option('display.width' ,100)
pd.set_option('expand_frame_repr', True)


with open('.\SalesRecords.json') \
    as in_file:
        jsonSales = json.load(in_file)

data = jsonSales['SalesRecords']
df = pd.json_normalize(data) # the nested json is put into a normalized state

print(df[['DeliveryTo.Surname', 'DeliveryTo.Firstname']])
# print(df)


# writing the data to the sqlite database with pandas
import sqlalchemy
#C:\\Users\\magru\\Documents\\A_Uni\\01a_Python-Projekte\\SIMProgrammierung\\Code\\python_exercises\\1) SIM - Integration Example (pandas json sqlite)\\sales.db
db = sqlalchemy.create_engine('sqlite:///C:\\Users\\magru\\Documents\\A_Uni\\01a_Python-Projekte\\SIMProgrammierung\\Code\\python_exercises\\1) SIM - Integration Example (pandas json sqlite)\\sales.db')
df.to_sql('jsondata', db, if_exists='replace')

# you can now check on the output in SQLite3 command line:
# select `Product.Description` from jsondata;
# Attention: quotation marks need to be like the ones given.

