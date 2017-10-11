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

# Adding arbitrary day to make date
gun_data['day'] = 1
gun_data['date'] = gun_data['year'].astype(str) + '-' + gun_data['month'].astype(str) + '-' + gun_data['day'].astype(str)
gun_data['date'] = pd.to_datetime(gun_data['date'], format='%Y-%m-%d')

count_by_month = gun_data['date'].value_counts(sort=False)
count_by_month = count_by_month.to_frame('count')
count_by_month['x_label'] = count_by_month.index
count_by_month['x_label'] = count_by_month['x_label'].dt.year.astype(str) + '-' + count_by_month['x_label'].dt.month.astype(str)
count_by_month = count_by_month.sort_index(0)
print(count_by_month)

ax = count_by_month.plot.bar(count_by_month['count'])
ax.set_xticklabels(count_by_month['x_label'])
ax.set_title('Gun Deaths By Month And Year')
ax.set_xlabel('Date')
ax.set_ylabel('How many')
ax.legend().remove()
plt.show()