"""
Reading file
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

import collections

gun_data = gun_data_fixed
gun_data_year = [row[1] for row in gun_data]

gun_stats_year = collections.Counter()

for year in gun_data_year:
    gun_stats_year[year] += 1

# print(gun_stats_year)

# ==================================================================

from datetime import datetime
import matplotlib.pyplot as plt

#extracting year, month
gun_dates = [datetime(year=int(row[1]), month=int(row[2]), day=1) for row in gun_data]

gun_stats_month = collections.Counter()

for date in gun_dates:
    gun_stats_month[date] += 1

# print(gun_stats_month.most_common(10))

# Drawing graph with it.
gun_stats_month_List = list(gun_stats_month.items())
graph_gun_stats_month_dates = [row[0] for row in gun_stats_month_List]
graph_gun_stats_month_counts = [row[1] for row in gun_stats_month_List]

plt.style.use('ggplot')
# plt.plot(graph_gun_stats_month_dates, graph_gun_stats_month_counts)
# plt.show()

# ==================================================================

def get_counts(column_number):
    temp_data = [row[column_number] for row in gun_data]
    temp_counter = collections.Counter()
    for item in temp_data:
        temp_counter[item] += 1
    return temp_counter

def get_graph_data(collection):
    collection_list = list(collection.items())
    x_list = [row[0] for row in collection_list]
    y_list = [row[1] for row in collection_list]
    return x_list, y_list

'''
# print(plt.style.available)
plt.style.use('fivethirtyeight')

# Showing gun stats by gender
gun_stats_sex = get_counts(5) #5 is position of sex
x_gun_stats_sex, y_gun_stats_sex = get_graph_data(gun_stats_sex)

plt.title('By gender')
plt.xlabel('Death')
plt.ylabel('Gender')
plt.bar(range(len(x_gun_stats_sex)), y_gun_stats_sex)
plt.xticks(range(len(x_gun_stats_sex)), x_gun_stats_sex)

plt.tight_layout()
plt.show()

# Showing gun stats by race
gun_stats_race = get_counts(7) #7 is position of race
x_gun_stats_race, y_gun_stats_race = get_graph_data(gun_stats_race)

plt.title('By race')
plt.xlabel('Death')
plt.ylabel('Race')
plt.bar(range(len(y_gun_stats_race)), y_gun_stats_race)
plt.xticks(range(len(x_gun_stats_race)), x_gun_stats_race)

plt.tight_layout()
plt.show()
'''



"""
Issue, I don't know total number of population by race so even though 'Native American/Native Alaskan' is lowest, it might be because they are tiny population.

Really need to look by percentage of crime.
Maybe do a parody?
"""

# ==================================================================


file_census = open('b_census.csv')
reader_census = csv.reader(file_census)

census_data = list(reader_census)
print(census_data)