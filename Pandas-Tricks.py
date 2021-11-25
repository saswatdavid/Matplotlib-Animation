from os import SEEK_DATA
import pandas as pd

#Create Sample Data
df = pd.DataFrame({'name': ['Sam', 'Mike', 'Lisa'], 'items': [24, 44, 55]})

#Counting Number Of Values
df['name'].value_counts()

#Querying Data
df.query('name == "Sam"')
df.query('items >= 20')