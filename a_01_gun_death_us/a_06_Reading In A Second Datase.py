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


# ==================================================================

"""
Reading in data which shows number of whole population per race.
"""

file_census = open('b_census.csv')
reader_census = csv.reader(file_census)

census_data = list(reader_census)
print(census_data)