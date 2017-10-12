"""
Previous work on data
"""

import csv
import collections
import matplotlib.pyplot as plt


file = open('full_data.csv')
reader = csv.reader(file)

gun_data = list(reader)
header = gun_data[0]
gun_data = gun_data[1:]

# Changing category to number

# Finding all unique values

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

# ==================================================================

"""
Investigating death by race
Investigating death by sex
"""

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


# print(plt.style.available) # An way to see all the pre-made ways to make graph look pretty.
plt.style.use('fivethirtyeight')

# 1. Showing gun stats by gender
gun_stats_sex = get_counts(5) #5 is position of sex
x_gun_stats_sex, y_gun_stats_sex = get_graph_data(gun_stats_sex)

plt.title('By gender')
plt.xlabel('Death')
plt.ylabel('Gender')
plt.bar(range(len(x_gun_stats_sex)), y_gun_stats_sex)
plt.xticks(range(len(x_gun_stats_sex)), x_gun_stats_sex)

plt.tight_layout()
plt.show()

# 2. Showing gun stats by race
gun_stats_race = get_counts(7) #7 is position of race
x_gun_stats_race, y_gun_stats_race = get_graph_data(gun_stats_race)

plt.title('By race')
plt.xlabel('Death')
plt.ylabel('Race')
plt.bar(range(len(y_gun_stats_race)), y_gun_stats_race)
plt.xticks(range(len(x_gun_stats_race)), x_gun_stats_race)

plt.tight_layout()
plt.show()


"""
Note:
Issue, I don't know total number of population by race so even though 'Native American/Native Alaskan' is lowest.
It might be because they are tiny population.

This is addressed in next.
"""

