import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

gun_data = pd.read_csv('full_data.csv', index_col='Unnamed: 0')

# Changing category to number

#1. Finding all unique values

education_replace = {
    'Less than HS': 1,
    'HS/GED': 2,
    'Some college': 3,
    'BA+': 4,
    np.NaN: 5
}

gun_data['education'] = gun_data['education'].map(education_replace)

# ==================================================================

count_by_year = gun_data['year'].value_counts()
print(count_by_year)
count_by_year.plot(kind='bar')
plt.style.use('ggplot')
plt.show()
