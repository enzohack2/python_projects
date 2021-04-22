# Web scraping dynamic price information 

### Introduction 
Web scraping, aka web harvesting, is the process of extracting data from websites. This process can be automated to improve effeciency when filtering through multiple sources. Static websites contain information that is infrequently updated. However, the aim of this project is to scrape dynamic currency price information for the currency pair GBP/JPY, of which is constantly being updated, every 5 minutes. This data will be fed into a .txt file and can be graphed later on. The [selenium](https://selenium-python.readthedocs.io/) module can help us acheive this task. However, there are many alternative methods of acheiving this goal. Furthermore, the script can be hosted on an Amazon Web Server as a long running selenium task. To make use of the code `scrapper001.py`, you can alter the webpage, websdrivevr and source elemnt to extract as required.


### Usage

Script is run in terminal `scrapper001.py` and a firefox browser opens up to the desired webpage. Selenium searches for the given element and extracts the price information and feeds it into a .csv file. The price information can later be graphed. 
