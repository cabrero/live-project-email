#!/usr/bin/env python3

import sys
from pathlib import Path
import csv

if len(sys.argv) != 2:
    print(f"Usage: {Path(sys.argv[0]).name} file.csv")
    exit(1)
    
filename = sys.argv[1]

data = {}

with open(filename, newline= '') as f:
    reader = csv.reader(f, skipinitialspace= True, quotechar= '"')
    for row in reader:
        print(row, sep= ' , ')
        assert len(row) == 9
        email, *student_data = row 
        data[email] = student_data

print(data)
