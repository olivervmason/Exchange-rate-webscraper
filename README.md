## Foreign Currency conversion webscraper

#### Description
This is a terminal app designed to return very recent (not quite live) exchange rates for the currency pairs of personal interest.

The website XE.com not only provides a platform for making ad hoc foreign currency transactions and running a speculative trading account, but it also tables publishes tables of historic rates.

However retrieving this information through the browser is tedious as there are many rates that are of no interest. XE.com provides an API for this purpose, however it is subscription only.

#### Features
Once installed, running the index.py file from the terminal will return a list of the rates of interest.

In recognition of the fact that the HTML page format can change and that subsequently the position of the elements is a potentially unreliable way of identifying the FX pairs, a  function has been built to flag to the user any FX movements of greater than 5% from the original starting values. If these thresholds are breached the user will check the live site, and if the rate is correct update the index.py file with the latest rate to adjust the future expectation.

For ease of use on a Linux operating system, a shortcut for the command to run this file can be created in the bash shell aliases at ~/.bashrc file in the following format (noting that the relative file path depends on where index.py is saved):

alias fx_check='cd file_path_of_index.py && python3 index.py'

#### Dependencies
This app requires the following libraries, installed using the commands listed:

<li>Requests (pip install requests --user);</li>
<li>Datetime (pip install lxml --user);</li>
<li>BeautifulSoup; (pip install bs4 --user);</li>