"""
Previous work on data
"""

import csv
import collections
from datetime import datetime
import matplotlib.pyplot as plt

file = open('full_data.csv')
reader = csv.reader(file)

gun_data = list(reader)
header = gun_data[0]
gun_data = gun_data[1:]

# Changing category to number

#1. Finding all unique values

education_list = []
for row in gun_data:
    education_list.append(row[10])

education_replace = {
    'Less than HS': 1,
    'HS/GED': 2,
    'Some college': 3,
    'BA+': 4,
    'NA': 5
}

gun_data_fixed = []

for row in gun_data:
    row[10] = education_replace[row[10]]
    gun_data_fixed.append(row)

gun_data = gun_data_fixed

# Makings some methods dues to repeating of code.

# Shows count of an column
def get_counts(column_number):
    temp_data = [row[column_number] for row in gun_data]
    temp_counter = collections.Counter()
    for item in temp_data:
        temp_counter[item] += 1
    return temp_counter

# Using collections data of above method, makes data to draw graph with.
def get_graph_data(collection):
    collection_list = list(collection.items())
    x_list = [row[0] for row in collection_list]
    y_list = [row[1] for row in collection_list]
    return x_list, y_list

"""
Reading in data which shows number of whole population per race.
"""

file_census = open('b_census.csv')
reader_census = csv.reader(file_census)
census_data = list(reader_census)

# ==================================================================

"""
Looking at 
(Gun death per 100,000) vs (Race) 
"""

# Using census data to convert death count to death count per 100,000 of that race.
census_data_dict = dict(zip(census_data[0], census_data[1]))

race_mapping = {
    "Asian/Pacific Islander": 15159516 + 674625,
    "Native American/Native Alaskan": 3739506,
    "Black": 40250635,
    "Hispanic": 44618105,
    "White": 197318956
}

gun_stats_race = get_counts(7)
gun_stats_race_dict = dict(gun_stats_race)

gun_stats_race_per = gun_stats_race_dict

for key, value in gun_stats_race_dict.items():
    gun_stats_race_dict[key] = (value / race_mapping[key]) * 100000

print(gun_stats_race_dict)


# Drawing graph with data
plt.style.use('fivethirtyeight')
x_gun_stats_race_per = gun_stats_race_dict.keys()
y_gun_stats_race_per = gun_stats_race_dict.values()

plt.title('By race')
plt.xlabel('Race')
plt.ylabel('Death per 100,000')
plt.bar(range(len(y_gun_stats_race_per)), y_gun_stats_race_per)
plt.xticks(range(len(x_gun_stats_race_per)), x_gun_stats_race_per)

plt.tight_layout()
plt.show()
