#!/usr/bin/env python3

import sys
from pathlib import Path
import csv
import smtplib
import configparser
import random

def read_data(filename):
    students_data = None
    with open(filename, newline= '') as f:
        reader = csv.reader(f, skipinitialspace= True, quotechar= '"')
        students_data = { email: student_data for email, *student_data in reader }
    return students_data

config = configparser.ConfigParser()
env = Path(__file__).parent / ".env"
config.read(env)
username = config['DEFAULT']['username']
password = config['DEFAULT']['password']
from_email = config['DEFAULT']['from'] 

to_email = "test@gmail.com"


def send_email(server, to, data):
    last_name, first_name, score_1, comments_1, score_2, comments_2, score_3, comments_3 = data
    chosen = "You’ve been randomly chosen to present a summary of the book in the next class. Looking forward to it!" if random.choice([True, False]) else ""
    
    text = f"""Dear {first_name}, Your score for the book assignment is broken down below by question number.

    1. 88%: good job
    2. 75%: needs a bit of work
    3. 90%: clear and concise

    {chosen}
"""
    print(f"Sending email to: {to}")
    print(text)
    server.sendmail(from_email, to, text)


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {Path(sys.argv[0]).name} file.csv")
        exit(1)
    filename = sys.argv[1]
    students_data = read_data(filename)

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(username, password)
    try:
        for email, data in students_data.items():
            send_email(server, email, data)
    finally:
        server.quit()

if __name__ == '__main__':
    main()
