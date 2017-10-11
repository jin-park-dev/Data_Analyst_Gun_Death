import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

gun_data = pd.read_csv('full_data.csv', index_col='Unnamed: 0')

# Changing category to number

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

######
# Finding intent of gun education vs intent
######

plt.style.use('seaborn')


def make_graph_data(df, col):
    count_by_col = df[col].value_counts(sort=False)
    count_by_col = count_by_col.to_frame('count')
    count_by_col['x_label'] = count_by_col.index
    count_by_col = count_by_col.sort_index(0)

    print(df[col].value_counts())

    return count_by_col['count'], count_by_col['x_label']

gun_data_male_intent_sui = gun_data[gun_data['intent'] == 'Suicide']
gun_data_male_intent_homo = gun_data[gun_data['intent'] == 'Homicide']

g_data_race_male_sui, g_x_race_male_sui = make_graph_data(gun_data_male_intent_sui, 'education')
g_data_race_male_homo, g_x_race_male_homo = make_graph_data(gun_data_male_intent_homo, 'education')


#Drawing graph
fig1, ax1 = plt.subplots()

ind = np.arange(len(g_data_race_male_sui))
width = 0.35

rect1 = ax1.bar(ind, g_data_race_male_sui, width, color='grey')
rect2 = ax1.bar(ind + width, g_data_race_male_homo, width, color='crimson')

ax1.set_xticks(ind + width / 2)
ax1.set_xticklabels(education_replace)


ax1.set_title('Gun Deaths')
ax1.set_xlabel('Education')
ax1.set_ylabel('Gun')

ax1.legend((rect1[0], rect2[0]), ('Suicide', 'Homicide'))


plt.tight_layout()
plt.show()