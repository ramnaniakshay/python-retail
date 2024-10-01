import numpy as np
import pandas as pd

ser = pd.Series()

print(ser)

data = np.array([1,2,3,4,5])
data = ["2",3,"4",True,9,9]

output = pd.Series(data)

print(output)

#custom index with pandas

data = [5,6,7,8]
CustomIndex = ['a','b','c','d']

result = pd.Series(data,index=CustomIndex)
print(result)

#dictionary

data = { 'a' : 100 , 'b' : 200, 'c': 300}

output = pd.Series(data)

print(output)

import sqlite3

conn = sqlite3.connect("Car_Database.db")
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

cursor.execute("SELECT * FROM Customers;")
response = cursor.fetchall()

print(response)

print("Available Tables:")
for table in tables:
    print(table[0])
