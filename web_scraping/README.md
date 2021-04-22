# Web scraping dynamic price information 

### Introduction 
Web scraping, aka web harvesting, is the process of extracting data from websites. This process can be automated to improve effeciency when filtering through multiple sources and is a useful alternative if a website doesn't have an [API](https://www.ibm.com/cloud/learn/api). Static websites contain information that is infrequently updated. However, the aim of this project is to scrape dynamic currency price information for the currency pair GBP/JPY, of which is constantly being updated, every 5 minutes. This data will be fed into a .txt file and can be graphed later on. The [selenium](https://selenium-python.readthedocs.io/) module can help us acheive this task. However, there are many alternative methods of acheiving this goal. Furthermore, the script can be hosted on an Amazon Web Server as a long running selenium task. To make use of the code `scrapper001.py`, you can alter the webpage, webdriver and source element to extract as needed for your requirements.

### Usage

Script is run in terminal `scrapper001.py` and a firefox browser opens up to the desired webpage. Selenium searches for the given element and extracts the price information and feeds it into a .txt file. Image below shows the .txt file after running for 1 hour.

![image](https://user-images.githubusercontent.com/77082071/115739813-249ac500-a386-11eb-8eee-73ed1678d502.png)



### Links
1. [Geckodriver download page](https://github.com/mozilla/geckodriver/releases) 
2. [Instructions for installing selenium package within anaconda environment](https://anaconda.org/conda-forge/selenium)
3. [Installing selenium with pip](https://selenium-python.readthedocs.io/installation.html)
4. Selenium simple usage [tutorial](https://selenium-python.readthedocs.io/getting-started.html#simple-usage)
5. Stackoverflow looping algorithm [examples](https://stackoverflow.com/questions/35722465/python-repeat-an-algorithm-exactly-every-5th-minute-of-the-hour)
