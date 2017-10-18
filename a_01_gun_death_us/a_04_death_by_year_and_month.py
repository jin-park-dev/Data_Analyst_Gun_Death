"""
Previous work on data
"""

import csv
import collections


file = open('full_data.csv')
reader = csv.reader(file)

gun_data = list(reader)
header = gun_data[0]
gun_data = gun_data[1:]

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

gun_data_year = [row[1] for row in gun_data]

gun_stats_year = collections.Counter()

for year in gun_data_year:
    gun_stats_year[year] += 1

# ==================================================================

"""
Looking at Death VS year-month
Part 1 is similar to previous of looking at count every month.
Part 2 is drawing graph with it.
"""

from datetime import datetime
import matplotlib.pyplot as plt

#extracting year, month
gun_dates = [datetime(year=int(row[1]), month=int(row[2]), day=1) for row in gun_data]

gun_stats_month = collections.Counter()

for date in gun_dates:
    gun_stats_month[date] += 1

print(gun_stats_month.most_common(10))

# Drawing graph with it.
gun_stats_month_List = list(gun_stats_month.items())
graph_gun_stats_month_dates = [row[0] for row in gun_stats_month_List]
graph_gun_stats_month_counts = [row[1] for row in gun_stats_month_List]

plt.style.use('ggplot')
plt.bar(graph_gun_stats_month_dates, graph_gun_stats_month_counts, width=10)
plt.show()