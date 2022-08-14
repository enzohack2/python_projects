#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pyperclip import copy
import sys

from pwinput import pwinput

# information inputted at runtime
epod_login = "itservicedesk"
epod_password = pwinput(prompt=f"\n ### Enter EPOD adminstrator password: ", mask="*")
search_email = pwinput(prompt=f"\n ### Enter full email address of the user whose EPOD password will be reset: ", mask="*")


epod_user_accont_url = "https://epod.phdmail.co.uk/hybridmail/rmg/User/List?hideSearch=False"

chrome_options = Options()
chrome_options.headless = True
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])



class DELETE_USER:
    def __init__(self, epod_url, epod_username, epod_password, user_email_address, driver_options):
        self.epod_url = epod_url
        self.epod_username = epod_username
        self.epod_password = epod_password
        self.user_email_address = user_email_address
        self.driver_options = driver_options
        
        # what if I had an explicit variable for user's firstname and lastname? So as to not need to split the email address all the time \n
        # this could be done outside of the class and refernced as a global variable 
        
    def epod_sign_in(self):
        "Sign in to EPOD user accounts page"
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.driver_options) 
        driver = self.driver
        driver.get(self.epod_url)

        # what if I read the xpaths from a separate file? As that would make the code neater
        username_xpath = '//*[@id="userName"]'
        password_xpath = '//*[@id="password"]'
        login_button_xpath = '//*[@id="submit"]'

        login_name_field = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, username_xpath))).send_keys(self.epod_username)
        password_field = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, password_xpath))).send_keys(self.epod_password)
        login_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, login_button_xpath))).click()

    def delete_user(self):
        try:
            """Reset user's EPOD password"""
            driver = self.driver 

            email_search_field_xpath = '//*[@id="userSearch"]'
            search_button_xpath = '//*[@id="searchSubmit"]'
            delete_user_icon = '//*[@id="content"]/table/tbody/tr/td[5]/a[2]'
            logout_button_xpath = '//*[@id="user"]/li[3]/a'
            
            search_for_user_by_email = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, email_search_field_xpath))).send_keys(self.user_email_address)
            user_search_by_email = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, search_button_xpath))).click()
            delete_user = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, delete_user_icon))).click()
            
            # might be better to place the image in the temp file 
            driver.save_screenshot(fr"C:\Users\Joshua.Musiyarira\Downloads\deleted_epod_account.png")

            
            logout = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, logout_button_xpath))).click()

            print("\n ### EPOD user deleted.")
        except:
            print("\n ### Error occured during user account deletion process. \n ### Does the user's account exist? \n ### Have you entered the correct email address? \n Did you enter the correct EPOD admin password? \n ### Check the above mentioned points and try launch this script again. \n ### Gracefully exiting. Have a nice day...")
            sys.exit(1)


    def main(self):
        self.epod_sign_in()
        self.delete_user()
 
 

if __name__ == "__main__":
    run = DELETE_USER(epod_user_accont_url, epod_login, epod_password, search_email, chrome_options)
    run.main()

    