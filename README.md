## Foreign Currency conversion webscraper

#### Description
This is a terminal app designed to return very recent (not quite live) exchange rates for the currency pairs of personal interest.

The website XE.com not only provides a platform for making foreign currency trades and transactions, but it also tables publishes tables of historic.

However retrieving this information through the browser is tedious as there is a lot of information that is not relevant. XE.com provides an API, however it is subscription only.

#### Features
Once installed, running the index.py file from the terminal will return a list of the rates of interest.

In recognition of the fact that the HTML page format can change and that subsequently the position of the elements is a potentially unreliable way of identifying the FX pairs, a  function has been built to flag to the user any FX movements of greater than 5% from the starting values, which have been saved to a separate file. This can be updated as required in the future.

For ease of use on a Linux operating system, a shortcut for the command to run this file can be created in the <> file in the following format (noting that the relative file path depends on where index.py is saved):

"fx" = "........ / python3 index.py"

#### Dependencies
This app requires the following libraries, installed using the commands listed:

<li>Requests (pip install requests --user);</li>
<li>Datetime (pip install lxml --user);</li>
<li>BeautifulSoup; (pip install bs4 --user);</li>


  
  
  

