""" Sample taken from
    https://towardsdatascience.com/yes-python-has-a-built-in-database-heres-how-to-use-it-b3c033f172d3
    
    date 11-06-2023
 """
 
import sqlite3

conn = sqlite3.connect('sales.db')
c = conn.cursor()  # cursor

c.execute("""
          SELECT * from jsondata""")

print(c.fetchall())

conn.commit()

conn.close()