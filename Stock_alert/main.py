import requests
import email
import datetime
from datetime import *
import smtplib


my_email = "coder.subbu@gmail.com"
password = "password"

today = date.today()
if today.weekday() == 0:
    diff = 3
elif today.weekday() == 6:
    diff = 2
else:
    diff = 1

last_bday = today - timedelta(days=diff)
next_last_bday = last_bday - timedelta(days=1)


STOCK = "AAPL"
COMPANY_NAME = "Apple"

API_KEY = "RKWISJCB583VYS1Y"
parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": API_KEY,
}
news_parameters = {
    "q": f"{COMPANY_NAME}",
    "from": f"{next_last_bday}",
    "to": f"{last_bday}",
    "sortBy": "popularity",
    "apiKey": "5cc63a3eb3784392bc26080be1fc476e"
}

request = requests.get(
    url="https://www.alphavantage.co/query?", params=parameters)
request.raise_for_status()

stock_data = request.json()

daily_data = stock_data["Time Series (Daily)"]
last_bday_data = daily_data[f"{last_bday}"]["4. close"]
next_last_bday_data = daily_data[f"{next_last_bday}"]["4. close"]
percentage_change = 100*(float(next_last_bday_data) -
                         float(last_bday_data))/float(last_bday_data)


def percentage():

    if percentage_change > 0:
        return (f"{COMPANY_NAME} 🔺 {round(percentage_change,2)}%\n")
    elif percentage_change < 0:
        return (f"{COMPANY_NAME} 🔻 {round(percentage_change,2)*-1}%\n")


response = requests.get(
    url="https://newsapi.org/v2/top-headlines?", params=news_parameters)
response.raise_for_status()

news_data = response.json()

news_slice = news_data["articles"][:4]


def newslet():
    with open("Stock_alert\\text.txt", "w") as file:

        for article in news_slice:
            file.write(
                f"Headline: {article['title']}. \nBrief: {article['description']}")
            
def newsbody():
    with open("Stock_alert\\text.txt", "r") as file:
        content = file.readlines()
        return content



with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="boyexplorer0@gmail.com",
        msg=f"Subject:Stocks Alert❗\n\n{percentage()}\n{newsbody()}",


    )
