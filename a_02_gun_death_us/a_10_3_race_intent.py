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

gun_data['day'] = 1
gun_data['date'] = gun_data['year'].astype(str) + '-' + gun_data['month'].astype(str) + '-' + gun_data['day'].astype(str)
gun_data['date'] = pd.to_datetime(gun_data['date'], format='%Y-%m-%d')

# ==================================================================

race_mapping = {
    "Asian/Pacific Islander": 15159516 + 674625,
    "Native American/Native Alaskan": 3739506,
    "Black": 40250635,
    "Hispanic": 44618105,
    "White": 197318956
}

def race_per_fix(row):
    race = row['x_label']
    count = row['count']/race_mapping[race] * 100000
    return count


plt.style.use('seaborn')

def display_info_by(col, col_filter, intent_filter):

    gun_data_filtered = gun_data[gun_data[col_filter] == intent_filter]
    print(gun_data_filtered[col].value_counts(sort=True))

    count_by_col = gun_data_filtered[col].value_counts(sort=False)
    count_by_col = count_by_col.to_frame('count')
    count_by_col['x_label'] = count_by_col.index
    count_by_col = count_by_col.sort_index(0)
    count_by_col_per = count_by_col.apply(race_per_fix, axis=1)
    print(count_by_col_per)

    ax = count_by_col_per.plot.bar()
    ax.set_xticklabels(count_by_col['x_label'])
    ax.set_title('Gun Deaths by {} - (cause: {})'.format(col, intent_filter))
    ax.set_xlabel(col)
    ax.set_ylabel('Gun death per 100000')
    ax.legend().remove()
    plt.tight_layout()
    plt.show()


display_info_by('race', col_filter='intent', intent_filter='Suicide')
display_info_by('race', col_filter='intent', intent_filter='Homicide')
