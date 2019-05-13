#!/bin/python3

"""
input file :parameters.txt
output file:parsed.json

"""
import csv
import json

f = open('parameters.txt', 'r')
reader = csv.DictReader(f, fieldnames=("first_name", "surname", "age", "nationality", "favourite_colour"))
out = json.dumps([row for row in reader])

# Save JSON file
f = open('parsed.json', 'w')
f.write(out)
print("parsed.json saved")
