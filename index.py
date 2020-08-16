import requests                             # Required to make url request
import datetime                             # Required to set dynamic url request
import bs4                                  # Required to parse through http response

# Set variables for url:
date = datetime.datetime.now()
year = date.year
month = date.strftime("%m") 
day = date.day

# Set url:
url = f"https://www.xe.com/currencytables/?from=AUD&date={year}-{month}-{day}"

# The "result" sends a request to the url and returns the http data from the target webpage, type <class 'requests.models.Response'>
result = requests.get(url)

# Use BeautifulSoup to identify different parts of webpage. "lxml" is the engine used to parse the string.
soup = bs4.BeautifulSoup(result.text, "lxml")

title = soup.select('title')[0].getText()                # Set title to match the <title> tag on the webpage
print(title)


