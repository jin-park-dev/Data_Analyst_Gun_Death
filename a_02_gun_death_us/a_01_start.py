"""
Reading file
"""

import pandas as pd

gun_data = pd.read_csv('full_data.csv', index_col='Unnamed: 0')

print(gun_data.head(10))
print(gun_data.columns.values)