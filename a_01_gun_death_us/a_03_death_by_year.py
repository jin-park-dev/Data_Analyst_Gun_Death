"""
Previous work on data
"""

import csv

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

# ==================================================================

"""
Looking at death by year

Using collections to count that number of death in that year. Collections has advantage over dictionary here in that 
we don't have to define key at start, and it can add automatically as required.
"""

import collections


gun_data = gun_data_fixed
gun_data_year = [row[1] for row in gun_data]

gun_stats_year = collections.Counter()

for year in gun_data_year:
    gun_stats_year[year] += 1

print(gun_stats_year)
