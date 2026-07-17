import smtplib
import random
import datetime as dt
import pandas as pd
import os

email = os.environ.get("my_email")
password = os.environ.get("my_password")

birthdays_data = pd.read_csv("birthdays.csv")
letter_number = random.randint(1, 3)
letter_name = "letter_templates/letter_" + str(letter_number) + ".txt"


for row in birthdays_data.itertuples(index=True):
    if row.day == dt.datetime.now().day and row.month == dt.datetime.now().month:

        with open(letter_name) as file:
            letter = file.read()
            letter = letter.replace("[NAME]", row.name)

        with smtplib.SMTP("smtp.gmail.com", port=587) as server:
            server.starttls()
            server.login(email, password)
            server.sendmail(from_addr="sethleung0719@gmail.com",
                            to_addrs=row.email,
                            msg="".join(letter))




