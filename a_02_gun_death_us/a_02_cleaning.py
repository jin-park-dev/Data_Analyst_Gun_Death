"""
Reading file
"""

import pandas as pd
import numpy as np

gun_data = pd.read_csv('full_data.csv', index_col='Unnamed: 0')

# Changing category to number

#1. Finding all unique values

education_replace = {
    'Less than HS': 1,
    'HS/GED': 2,
    'Some college': 3,
    'BA+': 4,
    np.NaN: 5   # Pandas helpfully (unhelpfully) assumes NaN, NA and other variations to be np.NaN type.
                #'NA' is taken as NaN unhelpfully in this case.
}

#2. Replacing education to values
gun_data['education'] = gun_data['education'].map(education_replace)
print(gun_data['education'].value_counts())
