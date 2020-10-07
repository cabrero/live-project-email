#!/usr/bin/env python3

import sys
import time
from pathlib import Path

from faker import Faker

if len(sys.argv) > 2:
    print()
    print(f"Usage: {Path(__file__).name} [seed]")
    print()
    print()
    sys.exit(1)
    
if len(sys.argv) > 1:
    try:
        seed = int(sys.argv[1])
    except ValueError:
        seed = hash(sys.argv[1])
else:
    seed = time.time_ns()    

fake = Faker(['es_ES', 'en_US', 'ja_JP'])
print(f"seed= {seed}", file= sys.stderr)
Faker.seed(seed)

n = fake.random_int(min=5, max= 273)
for _ in range(0, n):
    print(
        fake.email(), #Email
        f'"{fake.last_name()}"', # Last Name
        f'"{fake.first_name()}"', # First Name
        fake.random_int(min=0, max=10), # Problem 1 score
        f'"{fake.text(max_nb_chars= 40)}"', # Problem 1 comments
        fake.random_int(min=0, max=10), # Problem 2 score
        f'"{fake.text(max_nb_chars= 40)}"',# Problem 2 comments
        fake.random_int(min=0, max=10), # Problem 3 score
        f'"{fake.text(max_nb_chars= 40)}"', # Problem 3 comments
        sep= " , "
    )
