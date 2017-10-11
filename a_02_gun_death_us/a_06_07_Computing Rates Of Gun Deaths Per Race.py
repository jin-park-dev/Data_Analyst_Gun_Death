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


def display_info_by_race(col):
    count_by_race = gun_data[col].value_counts(sort=False)
    count_by_race = count_by_race.to_frame('count')
    count_by_race['x_label'] = count_by_race.index
    count_by_race = count_by_race.sort_index(0)
    count_by_race_per = count_by_race.apply(race_per_fix, axis=1)

    print(count_by_race)

    ax = count_by_race_per.plot.bar()
    ax.set_xticklabels(count_by_race['x_label'])
    ax.set_title('Gun Deaths: {}'.format(col))
    ax.set_xlabel(col)
    ax.set_ylabel('Gun death per 100000')
    ax.legend().remove()
    plt.show()

display_info_by_race('race')

