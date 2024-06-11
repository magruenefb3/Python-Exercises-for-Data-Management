""" Sample taken from
    https://towardsdatascience.com/yes-python-has-a-built-in-database-heres-how-to-use-it-b3c033f172d3
    
    date 11-06-2023
 """
 
import sqlite3

conn = sqlite3.connect('sales.db')
c = conn.cursor()  # cursor

c.execute("""CREATE TABLE customer (
	custId INTEGER PRIMARY KEY, 
	custFirst_name TEXT NOT NULL,
	custLast_name TEXT NOT NULL,
	custEmail TEXT NOT NULL,
	custPhone TEXT
)
          """)
c.execute("""INSERT INTO customer 
VALUES 
(1, 'Herber', 'Meier', 'h.meier@mail.co.uk', '+44 1 4543543988'),
(2, 'Sally', 'Hayek', 'supersally@protomail.com', '+69 69 333 3331')   """)

c.execute("""CREATE TABLE account (
    accNumber TEXT PRIMARY KEY,
	accBalance REAL NOT NULL,
	accHolderId INTEGER)
          """)

c.execute("""
INSERT INTO account 
VALUES 
('GB29NWBK60161331926819', -300.94, 1), 
('DE89370400440532013000', 120.78, 2)
""")

conn.commit()

conn.close()