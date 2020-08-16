import requests
import datetime

date = datetime.datetime.now()
year = date.year
month = date.strftime("%m") 
day = date.day

url = f"https://www.xe.com/currencytables/?from=AUD&date={year}-{month}-{day}"

result = requests.get(url)

print("https://www.xe.com/currencytables/?from=AUD&date=2020-08-16")
