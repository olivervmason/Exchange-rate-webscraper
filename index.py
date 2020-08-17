import requests                             # Required to make url request
import datetime                             # Required to set dynamic url request
import bs4                                  # Required to parse through http response

# Set variables for url:
date = datetime.datetime.now()
year = date.year
month = date.strftime("%m") 
day = date.day - 1                          # - 1 as current day rates are sometimes not available until evening Australia time

# Set url:
url = f"https://www.xe.com/currencytables/?from=AUD&date={year}-{month}-{day}"

print(url)
# The "result" sends a request to the url and returns the http data from the target webpage, type <class 'requests.models.Response'>
result = requests.get(url)

# Use BeautifulSoup to identify different parts of webpage. "lxml" is the engine used to parse the string.
soup = bs4.BeautifulSoup(result.text, "lxml")

title = soup.select('title')[0].getText()                # Set title to match the <title> tag on the webpage

# Set the rates to be returned in the terminal:

aud_to_usd = float(soup.select('.historicalRateTable-rateHeader')[3].getText())
usd_to_aud = float(soup.select('.historicalRateTable-rateHeader')[2].getText())

aud_to_nzd = float(soup.select('.historicalRateTable-rateHeader')[25].getText())
nzd_to_aud = float(soup.select('.historicalRateTable-rateHeader')[24].getText())

aud_to_jpy = float(soup.select('.historicalRateTable-rateHeader')[21].getText())
jpy_to_aud = float(soup.select('.historicalRateTable-rateHeader')[20].getText())

aud_to_eur = float(soup.select('.historicalRateTable-rateHeader')[5].getText())
eur_to_aud = float(soup.select('.historicalRateTable-rateHeader')[4].getText())

aud_to_rub = float(soup.select('.historicalRateTable-rateHeader')[63].getText())
rub_to_aud = float(soup.select('.historicalRateTable-rateHeader')[62].getText())

aud_to_col = float(soup.select('.historicalRateTable-rateHeader')[79].getText())
col_to_aud = float(soup.select('.historicalRateTable-rateHeader')[78].getText())

# Identify any extraordinary FX movements - threshold set at 5% variance from initial start:

def variance_check():
    if (aud_to_usd / 1.3943009086) > 1.05 or (aud_to_usd / 1.3943009086) < 0.95:
        return "FAILED - check AUD:USD rate"
    
    if (usd_to_aud / 0.7172052990) > 1.05 or (usd_to_aud / 0.7172052990) < 0.95:
        return "FAILED - check USD:AUD rate"

    if (aud_to_nzd / 0.9119575285) > 1.05 or (aud_to_nzd / 0.9119575285) < 0.95:
        return "FAILED - check AUD:NZD rate"

    if (nzd_to_aud / 1.0965422936) > 1.05 or (nzd_to_aud / 1.0965422936) < 0.95:
        return "FAILED - check NZD:AUD rate"

    if (aud_to_jpy / 0.0130836400) > 1.05 or (aud_to_jpy / 0.0130836400) < 0.95:
        return "FAILED - check AUD:JPY rate"

    if (jpy_to_aud / 76.4313295293) > 1.05 or (jpy_to_aud / 76.4313295293) < 0.95:
        return "FAILED - check JPY:AUD rate"

    if (aud_to_eur / 1.6511313406) > 1.05 or (aud_to_eur / 1.6511313406) < 0.95:
        return "FAILED - check AUD:EUR rate"

    if (eur_to_aud / 0.6056453387) > 1.05 or (eur_to_aud / 0.6056453387) < 0.95:
        return "FAILED - check EUR:AUD rate"

    if (aud_to_rub / 0.0191311081) > 1.05 or (aud_to_rub / 0.0191311081) < 0.95:
        return "FAILED - check AUD:RUB rate"

    if (rub_to_aud / 52.2708876046) > 1.05 or (rub_to_aud / 52.2708876046) < 0.95:
        return "FAILED - check RUB:AUD rate"

    if (aud_to_col / 0.0003675963) > 1.05 or (aud_to_col / 0.0003675963) < 0.95:
        return "FAILED - check AUD:COL rate"

    if (col_to_aud / 2720.3758756422) > 1.05 or (col_to_aud / 2720.3758756422) < 0.95:
        return "FAILED - check COL:AUD rate"
    else:
        return "passed"

view = f'''
    AUD:USD = {aud_to_usd}           
    USD:AUD = {usd_to_aud}              

    AUD:NZD = {aud_to_nzd}
    NZD:AUD = {nzd_to_aud}

    AUD:JPY = {aud_to_jpy}
    JPY:AUD = {jpy_to_aud}

    AUD:EUR = {aud_to_eur}
    EUR:AUD = {eur_to_aud}

    AUD:RUB = {aud_to_rub}
    RUB:AUD = {rub_to_aud}

    AUD:COL = {aud_to_col}
    COL:AUD = {col_to_aud}

    The FX variance sense checks have {variance_check()}...
'''

print(view)
