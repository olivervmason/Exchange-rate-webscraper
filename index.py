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

'''
BeautifulSoup selector cheatsheet:
    soup.select('div')                  - Selects ALL based on tag type 
    soup.select('#special_id)           - Selects ALL elemments with the named id
    soup.select('.class_name')           - Select HTML elements by class name
    soup.select('div element_name')     - Select all instances of element_name within the named div
    soup.select('div > element_name')   - As above but with nothing in between
'''

# Set the rates to be returned in the terminal:

aud_to_usd = soup.select('.historicalRateTable-rateHeader')[3].getText()
usd_to_aud = soup.select('.historicalRateTable-rateHeader')[2].getText()

aud_to_nzd = soup.select('.historicalRateTable-rateHeader')[25].getText()
nzd_to_aud = soup.select('.historicalRateTable-rateHeader')[24].getText()

aud_to_jpy = soup.select('.historicalRateTable-rateHeader')[21].getText()
jpy_to_aud = soup.select('.historicalRateTable-rateHeader')[20].getText()

aud_to_eur = soup.select('.historicalRateTable-rateHeader')[5].getText()
eur_to_aud = soup.select('.historicalRateTable-rateHeader')[4].getText()

aud_to_rub = soup.select('.historicalRateTable-rateHeader')[63].getText()
rub_to_aud = soup.select('.historicalRateTable-rateHeader')[62].getText()

aud_to_col = soup.select('.historicalRateTable-rateHeader')[79].getText()
col_to_aud = soup.select('.historicalRateTable-rateHeader')[78].getText()



print("aud_to_usd should be 1.3943009086, and is: ", aud_to_usd)           
print("usd_to_aud should be 0.7172052990, and is: ", usd_to_aud)

print("aud_to_nzd should be 0.9119575285, and is: ", aud_to_nzd)
print("nzd_to_aud should be 1.0965422936, and is: ", nzd_to_aud)

print("aud_to_jpy should be 0.0130836400, and is: ", aud_to_jpy)
print("jpy_to_aud should be 76.4313295293, and is: ", jpy_to_aud)

print("aud_to_eur should be 1.6511313406, and is: ", aud_to_eur)
print("eur_to_aud should be 0.6056453387, and is: ", eur_to_aud)

print("aud_to_rub should be 0.0191310545, and is: ", aud_to_rub)
print("rub_to_aud should be 52.2710339969, and is: ", rub_to_aud)

print("aud_to_col should be 0.0003675975, and is: ", aud_to_col)
print("col_to_aud should be 2720.3668401739, and is: ", col_to_aud)

