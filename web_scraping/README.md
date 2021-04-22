# Web scraping dynamic price information 

### Introduction 
Web scraping, aka web harvesting, is the process of extracting data from websites. This process can be automated to improve effeciency when filtering through multiple sources and is a useful alternative if a website doesn't have an [API](https://www.ibm.com/cloud/learn/api). Static websites contain information that is infrequently updated. However, the aim of this project is to scrape dynamic currency price information for the currency pair GBP/JPY, of which is constantly being updated, every 5 minutes. This data will be fed into a .txt file and can be graphed later on. The [selenium](https://selenium-python.readthedocs.io/) module can help us acheive this task. However, there are many alternative methods of acheiving this goal. Furthermore, the script can be hosted on an Amazon Web Server as a long running selenium task. To make use of the code `scrapper001.py`, you can alter the webpage, webdriver and source element to extract as needed for your requirements.

### Usage

Script is run in terminal `scrapper001.py` and a firefox browser opens up to the desired webpage. Selenium searches for the given element storing live price information, extracts the price information and feeds it into a .txt file `gjPriceData.txt`. Images below shows the .txt file after running for 1 hour. It's been automatically updated with price data and will continue to do so for as long as the machine is not shut down. 

![image](https://user-images.githubusercontent.com/77082071/115752698-4437ea80-a392-11eb-9383-340276ef7ba1.png)

![image](https://user-images.githubusercontent.com/77082071/115753106-b8728e00-a392-11eb-8b0c-22284e381c9f.png)

![image](https://user-images.githubusercontent.com/77082071/115752726-4b5ef880-a392-11eb-8cc7-0d18abd7052b.png)

![image](https://user-images.githubusercontent.com/77082071/115752758-531e9d00-a392-11eb-8ce9-74a30e9aae1f.png)

### Links
1. [Geckodriver download page](https://github.com/mozilla/geckodriver/releases) 
2. [Instructions for installing selenium package within anaconda environment](https://anaconda.org/conda-forge/selenium)
3. [Installing selenium with pip](https://selenium-python.readthedocs.io/installation.html)
4. Selenium simple usage [tutorial](https://selenium-python.readthedocs.io/getting-started.html#simple-usage)
5. Stackoverflow looping algorithm [examples](https://stackoverflow.com/questions/35722465/python-repeat-an-algorithm-exactly-every-5th-minute-of-the-hour)
