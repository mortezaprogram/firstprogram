import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT="https://www.alphavantage.co/query"
NEWS_ENDPOINT="https://newsapi.org/v2/everything"

STOCK_API_KEY="M5X60XAL2NZ1E23W"
NEWS_API_KEY="5109f5dc1e184945a1b35a00a3b0469f"
TWILIO_SID=""
TWILIO_AUTH_TOKEN=""


stock_params={
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY

}
response=requests.get(STOCK_ENDPOINT,params=stock_params)
data=response.json()['Time Series (Daily)']
data_list=[value for (key,value) in data.items()]
yesterday_data=data_list[0]
yesterday_closing_data=yesterday_data['4. close']
print(yesterday_closing_data)

day_before_yesterday_data=data_list[1]
day_before_yesterday_closing_data=day_before_yesterday_data['4. close']
print(day_before_yesterday_closing_data)

difference=(float(day_before_yesterday_closing_data)-float(yesterday_closing_data))
up_down=None
if difference>0:
    up_down="🔺"
else:
    up_down="🔻"

print(difference)

diff_percent=round((difference/float(yesterday_closing_data))*100)
print(diff_percent)

if abs(diff_percent)>0.001:
    news_param={
        "apikey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
    news_response=requests.get(NEWS_ENDPOINT,params=news_param)
    articles=news_response.json()["articles"]
    three_articles=articles[:3]
    print(three_articles)

    formatted_articles=[f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}.\nBrief {article['description']}" for article in three_articles]
    print(formatted_articles)
    client=Client(TWILIO_SID,TWILIO_AUTH_TOKEN)


    # for article in formatted_articles:
    #     message=client.messages.create(
    #         body=article,
    #         from="+4235433344",
    #         to="+1245"
    #     )




## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


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

