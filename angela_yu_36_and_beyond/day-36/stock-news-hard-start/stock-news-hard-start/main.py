import os, requests, datetime
from twilio.rest import Client

STOCK = "NVDA"
COMPANY_NAME = "Nvidia"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

date = []
today = datetime.date.today()
date.append(str(today))
yesterday = today - datetime.timedelta(days=1)
date.append(str(yesterday))
before_yesterday = yesterday - datetime.timedelta(days=1)
date.append(str(before_yesterday))

price_request_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": os.environ.get("AV_API_KEY")
}

price_response = requests.get(url=STOCK_ENDPOINT, params=price_request_parameters)
price_response.raise_for_status()
yesterday_close = float(price_response.json()["Time Series (Daily)"][date[1]]["4. close"])
before_yesterday_close = float(price_response.json()["Time Series (Daily)"][date[2]]["4. close"])
price_difference = round((yesterday_close - before_yesterday_close) / yesterday_close * 100,2)
up_down = None
if price_difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

if abs(price_difference) >= 5:
    news_parameters = {
        "apiKey": os.environ.get("NEWS_API_KEY"),
        "qInTitle": COMPANY_NAME,
        "from": before_yesterday,
        "to": today,
        "sortBy": "popularity",
        "language": "en"
    }
    news_response = requests.get(url=NEWS_ENDPOINT,params=news_parameters)
    news = news_response.json()["articles"][:3]

formatted_articles = [f"{STOCK}: {up_down}{price_difference}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in news]
client = Client(os.environ.get("TWILIO_SID"), os.environ.get("TWILIO_AUTH_TOKEN"))
for article in formatted_articles:
    message = client.messages.create(body=article, from_= os.environ.get("MY_FROM_NUMBER"),to=os.environ.get("MY_NUM"))