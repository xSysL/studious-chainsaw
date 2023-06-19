import smtplib
import datetime as dt
import random


def quote_generator():

    with open("SMTP Mail\\quotes copy.txt", 'r') as file:
        words = file.read()
        quote = random.choice(words.split("\n"))
        return quote


my_email = "test@gmail.com"
password = "testpass"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 0:

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="boyexplorer0@gmail.com",
            msg=f"Subject:Quote For the Day\n\n{quote_generator()}"
        )
