import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

gun_data = pd.read_csv('full_data.csv', index_col='Unnamed: 0')

education_replace = {
    'Less than HS': 1,
    'HS/GED': 2,
    'Some college': 3,
    'BA+': 4,
    np.NaN: 5
}

gun_data['education'] = gun_data['education'].map(education_replace)

# ==================================================================

"""
Looking at 
(Gun death per 100,000) vs (Race) 
"""

count_by_year = gun_data['year'].value_counts()
print(count_by_year)
plt.style.use('ggplot')
count_by_year.plot(kind='bar')
plt.show()
