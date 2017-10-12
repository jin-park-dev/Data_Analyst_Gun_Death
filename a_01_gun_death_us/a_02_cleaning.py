"""
Reading file
"""

import csv

file = open('full_data.csv')
reader = csv.reader(file)


# ==================================================================

"""
Cleaning Data 
"""

gun_data = list(reader)
header = gun_data[0]
gun_data = gun_data[1:]

# Changing category to number
#1. Finding all unique values

education_list = []
for row in gun_data:
    education_list.append(row[10])

print(set(education_list))

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

print(gun_data_fixed[0:5])
print(set([row[10] for row in gun_data_fixed]))