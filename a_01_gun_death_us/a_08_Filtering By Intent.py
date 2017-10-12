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

# ==================================================================

"""
Looking at 
"""

# Filtering for intent
intent = [(row[0], row[3]) for row in gun_data]

filtered_intent = []
for col_id, col_intent in intent:
    if col_intent == 'Homicide':
        filtered_intent.append(gun_data[int(col_id)-1]) # ID starts from 1. Need to -1 to offset and use as list position.


# get_count now also takes in custom data instead of only looking at original gun data.
def get_counts_2(column_number, data):
    temp_data = [row[column_number] for row in data]
    temp_counter = collections.Counter()
    for item in temp_data:
        temp_counter[item] += 1
    return temp_counter


filtered_gun_stats_race = get_counts_2(7, filtered_intent)
filtered_gun_stats_race_dict = dict(filtered_gun_stats_race)

filtered_gun_stats_race_per = filtered_gun_stats_race_dict

for key, value in filtered_gun_stats_race_dict.items():
    filtered_gun_stats_race_dict[key] = (value / race_mapping[key]) * 100000

x_filtered_gun_stats_race_per = filtered_gun_stats_race_dict.keys()
y_filtered_gun_stats_race_per = filtered_gun_stats_race_dict.values()

plt.style.use('fivethirtyeight')
plt.title('By race, homicide only')
plt.xlabel('Race')
plt.ylabel('Death per 100,000')
plt.bar(range(len(y_filtered_gun_stats_race_per)), y_filtered_gun_stats_race_per)
plt.xticks(range(len(x_filtered_gun_stats_race_per)), x_filtered_gun_stats_race_per)

plt.tight_layout()
plt.show()

print(filtered_gun_stats_race)

# Just checking I have right set and it's filtering correctly
print(set(row[3] for row in gun_data))
print(set(row[3] for row in filtered_intent))