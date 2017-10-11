"""
Reading file
"""

import csv

file = open('full_data.csv')
reader = csv.reader(file)

# for row in reader:
#     print(row)

gun_data = list(reader)
print(gun_data[0:5])