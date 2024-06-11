""" attention, running this might fail in VSCode.
    This is due to PowerShell. 

"""

import sqlite3
import pandas as pd

# please adapt the path accordingly to your settings
conn = sqlite3.connect('''C:\SIMProgrammierung\Code\python_exercises\load json and db for cleansing\sales.db''')
df = pd.read_sql_query("SELECT * FROM customer;", conn)
print(df)
conn.commit()
conn.close()