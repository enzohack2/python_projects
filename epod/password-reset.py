#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from generator import generate_random_password
from pyperclip import copy
import sys
# used for terminal ipnut that does not display values (need an alternative)
from pwinput import pwinput

# information inputted at runtime
epod_login = "itservicedesk"
epod_password = pwinput(prompt=f"\n ### Enter EPOD adminstrator password: ", mask="*")
search_email = pwinput(prompt=f"\n ### Enter full email address of the user whose EPOD password will be reset: ", mask="*")

# url opens straight to the search for users section within epod 
url = "https://epod.phdmail.co.uk/hybridmail/rmg/User/List?hideSearch=False"

# chrome driver options applied to chrome web browser once launched 
chrome_options = Options()
# I wonder if maximising the chrome browser will affect the quality of the final screenshot or not
chrome_options.add_argument("start-maximized")
# run selenium in a headless state, in the background so as to not open up a browser
chrome_options.headless = True
# suppress console information from Selenium or browser
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

# creating a random password form the "generate_random_password" module 
generated_epod_password = generate_random_password()

class EPOD_PASSWORD:
    def __init__(self, epod_url, epod_username, epod_password, user_email_address, driver_options, rand_password):
        self.epod_url = epod_url
        self.epod_username = epod_username
        self.epod_password = epod_password
        self.user_email_address = user_email_address
        self.driver_options = driver_options
        self.rand_password = rand_password

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

    def reset_epod_password(self):
        try:
            """Reset user's EPOD password"""
            driver = self.driver 

            email_search_field_xpath = '//*[@id="userSearch"]'
            search_button_xpath = '//*[@id="searchSubmit"]'
            edit_user_pencil_xpath = '//*[@id="content"]/table/tbody/tr/td[5]/a[1]'
            reset_button_xpath = '//*[@id="properties"]/div[5]/a'
            save_button_xpath = '//*[@id="submitButton"]'
        
            search_for_user_by_email = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, email_search_field_xpath))).send_keys(self.user_email_address)
            user_search_by_email = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, search_button_xpath))).click()
            edit_user_epod_details =  WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, edit_user_pencil_xpath))).click()
            reset_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, reset_button_xpath))).click()

            # set random password generated as an instance variable for use in another method ticket_notes()
            rand_password = self.rand_password



            # entering password twice to confirm change 
            for val in range(1,3):
                reset_password_xpath = f'//*[@id="password{val}"]'
                new_password = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, reset_password_xpath))).send_keys(rand_password)
        
                
            select_save_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, save_button_xpath))).click()

            logout_button_xpath = '//*[@id="user"]/li[3]/a'
            logout = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, logout_button_xpath))).click()
        except:
            print("\n ### Error occured during reset process. \n ### Does the user's account exist? \n ### Or did you enter the correct EPOD admin password? \n ### Check the above mentioned points and try launch this script again. \n ### Gracefully exiting. Have a nice day...")
            sys.exit(1)
            # What if at this point the script then displays an image of users found that are somewhat close to the user being searched for as well as their email address?

    def validate_password_reset_occured(self):
        """Confirm user's EPOD account can be logged in to and send a screenshot to my inbox containing a screenshot of the user's account logged in to"""
        driver = self.driver
        
        login_page_xpath = '//*[@id="content"]/a'
        login_page_select = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, login_page_xpath))).click()

        username_xpath = '//*[@id="userName"]'
        password_xpath = '//*[@id="password"]'
        login_button_xpath = '//*[@id="submit"]'

        user_name = self.user_email_address

        login = user_name.split("@")
        login = login[0].split(".")

        login = f"{login[0]} {login[1]}"

        login_name_field = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, username_xpath))).send_keys(login)
        password_field = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, password_xpath))).send_keys(self.rand_password)
        login_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, login_button_xpath))).click()

        # take a screenshot of the user's logged in account and save it in downloads under name epod_verification_<firstname_lastname of user>.png
        driver.save_screenshot(fr"C:\Users\Joshua.Musiyarira\Downloads\epod_password_reset_{login}.png")

        # logout of epod 
        logout_button_xpath = '//*[@id="user"]/li[3]/a'
        logout = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, logout_button_xpath))).click()

        # close driver
        driver.quit()

    def ticket_notes(self):    
        """
        Creates closing notes for user to paste onto the EPOD ticket they are working on.
        """
        user_first_name = self.user_email_address.split(".")
        work_note = f"""Reset {user_first_name[0]}'s EPOD password and verified their account can be signed in to."""
        copy(work_note)

        paste_worknote = input(f"\n ### ENTER Y after pasting the worknote from your clipboard onto your EPOD ticket: ")

        while True:
            if paste_worknote != "Y":
                paste_worknote = input(f"\n ### ENTER Y after pasting the worknote from your clipboard onto your EPOD ticket: ")
            else:
                resolution_note = open("resolution_note.txt").read().format(user_first_name[0], self.rand_password)
                copy(resolution_note)
                paste_resolution_note = input(f"\n ### ENTER Y after pasting the resolution note from your clipboard onto your EPOD ticket: ")

                if paste_resolution_note != "Y":
                    paste_resolution_note = input(f"\n ### ENTER Y after pasting the resolution from your clipboard onto your EPOD ticket: ")
                else:
                    break
        
        print(f"\n ### Gracefully exiting, have a nice day.....")
        sys.exit(1)

    def main(self):
        self.epod_sign_in()
        self.reset_epod_password()
        self.validate_password_reset_occured()
        self.ticket_notes()

    

if __name__ == "__main__":
    run = EPOD_PASSWORD(url, epod_login, epod_password, search_email, chrome_options, generated_epod_password )
    run.main()

    