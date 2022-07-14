import requests
from twilio.rest import Client
import keys

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": keys.alphavantage_api_key
}

response = requests.get(url="https://www.alphavantage.co/query", params=parameters)
data = response.json()["Time Series (Daily)"]
# short_data = data["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_stock_price = float(data_list[0]["4. close"])
previous_day_price = float(data_list[1]["4. close"])

price_change_percentage = abs(((yesterday_stock_price / previous_day_price) - 1) * 100)


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.


news_params = {
    "q": COMPANY_NAME,
    "apiKey": keys.newsapi_api_key
}

response_news = requests.get(url="https://newsapi.org/v2/everything", params=news_params)
news = response_news.json()["articles"]

three_articles = news[:3]

formatted_articles = [f"Headline: {item['title']}. \nBrief: {item['description']}" for item in three_articles]


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.

account_sid = keys.twilio_account_sid
auth_token = keys.twilio_auth_token

client = Client(account_sid, auth_token)

if price_change_percentage > 2.0:
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_=keys.twilio_number,
            to=keys.my_number
        )
        print(message.status)


#Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

