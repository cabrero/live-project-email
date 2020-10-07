#!/usr/bin/env python3

import sys
from pathlib import Path
import csv
import smtplib
import configparser

if len(sys.argv) != 2:
    print(f"Usage: {Path(sys.argv[0]).name} file.csv")
    exit(1)
    
filename = sys.argv[1]

with open(filename, newline= '') as f:
    reader = csv.reader(f, skipinitialspace= True, quotechar= '"')
    data = { email: student_data for email, *student_data in reader }

config = configparser.ConfigParser()
env = Path(__file__).parent / ".env"
config.read(env)
username = config['DEFAULT']['username']
password = config['DEFAULT']['password']
from_email = config['DEFAULT']['from'] 

to_email = "test@gmail.com"

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(username, password)
server.sendmail(
    from_email, 
    to_email,
  "this message is from python")
server.quit()
