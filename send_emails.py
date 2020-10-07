#!/usr/bin/env python3

import sys
from pathlib import Path
import csv

if len(sys.argv) != 2:
    print(f"Usage: {Path(sys.argv[0]).name} file.csv")
    exit(1)
    
filename = sys.argv[1]

with open(filename, newline= '') as f:
    reader = csv.reader(f, skipinitialspace= True, quotechar= '"')
    data = { email: student_data for email, *student_data in reader }

print(data)
