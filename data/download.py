import requests

url = "https://raw.githubusercontent.com/dD2405/Twitter_Sentiment_Analysis/master/train.csv"

response = requests.get(url)

with open("raw_data.csv", "wb") as file:
    file.write(response.content)

print("Dataset downloaded!")