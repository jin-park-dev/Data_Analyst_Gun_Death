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
Investigating death by race
Investigating death by sex
"""

def display_info_by(col):
    count_by_col = gun_data[col].value_counts(sort=False)
    count_by_col = count_by_col.to_frame('count')
    count_by_col['x_label'] = count_by_col.index
    count_by_col = count_by_col.sort_index(0)
    print(count_by_col)

    ax = count_by_col.plot.bar(count_by_col['count'])
    ax.set_xticklabels(count_by_col['x_label'])
    ax.set_title('Gun Deaths: {}'.format(col))
    ax.set_xlabel(col)
    ax.set_ylabel('How many')
    ax.legend().remove()
    plt.show()

display_info_by('sex')
display_info_by('race')
