#!/usr/bin/env python3


import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 


def scrape_price():
    """Gets GBPY/JPY currency price information every 5 minutes and appends it to a .txt file in the relative directory."""

    geckodriver = r"C:\Users\joshj\Downloads\geckodriver.exe" # Geckodriver executable file location on host as a raw string 
    driver = webdriver.Firefox(executable_path=geckodriver) # Establishing usage of a FireFox web browser 
    driver.get("https://finance.yahoo.com/quote/GBPJPY=X")  # Opening yahoo finance webpage 

    cookie_button = "/html/body/div/div/div/div/form/div[2]/div[2]/button" # Accepting cookies
    cookies = driver.find_element_by_xpath(cookie_button).click()
    time.sleep(2) # Explicit wait for webpage to wait 
    
    price_elem = driver.find_element_by_xpath('//*[@id="quote-header-info"]/div[3]/div[1]/div/span[1]')
    price_val = price_elem.text

    # Appending price information to a .txt file every 5 minutes and refreshing the driver 
    while True:
        time.sleep(300 - time.time() % 300)
        
        with open("gjPriceData.txt", mode="a", encoding="utf-8") as f:
            time_format = time.strftime("%d:%m:%Y - %H:%M:%S")

            f.writelines(f"{time_format},{price_val}\n") 

            # reload the driver to the same webpage 
            driver.refresh()


if __name__ == "__main__":
    scrape_price()