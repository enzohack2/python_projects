from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pwinput import pwinput
from generator import generate_random_password
from sys import exit

epod_username = "itservicedesk"
epod_password = pwinput(f"\n### Enter EPOD password: ")
new_epod_account_email = pwinput(f"\n### Enter email address for new EPOD user: ")
user_acc_password = generate_random_password()
create_user_url = "https://epod.phdmail.co.uk/hybridmail/rmg/User/Create?returnUrl=%252fhybridmail%252frmg%252fUser%252fList&CompanyId=5079041"

chrome_options = Options()
chrome_options.add_argument("start-maximized")
chrome_options.headless = True

class CREATE_USER:
    def __init__(self, epod_url, epod_username, epod_password, user_email_address, driver_options, user_pwd):
        self.epod_url = epod_url
        self.epod_username = epod_username
        self.epod_password = epod_password
        self.user_email_address = user_email_address
        self.driver_options = driver_options
        self.user_pwd = user_pwd
        
        self.email_address_split = self.user_email_address.split("@")
        self.full_name = self.email_address_split[0].split(".")
        self.forename = self.full_name[0]
        self.surname = self.full_name[1]

    def epod_sign_in(self):
        "Sign in to EPOD user accounts page"
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.driver_options) 
        driver = self.driver
        driver.get(self.epod_url)

        username_xpath = '//*[@id="userName"]'
        password_xpath = '//*[@id="password"]'
        login_button_xpath = '//*[@id="submit"]'

        login_name_field = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, username_xpath))).send_keys(self.epod_username)
        password_field = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, password_xpath))).send_keys(self.epod_password)
        login_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, login_button_xpath))).click()

    def create_account(self):
        """Create EPOD user account based on provided email address"""
        driver = self.driver 

        new_user_login_name_xpath = '//*[@id="Name"]'
        password_xpath = '//*[@id="password1"]'
        password_confirm_xpath = '//*[@id="password2"]'
        first_name_xpath = '//*[@id="FirstName"]'
        surname_field_xpath = '//*[@id="Surname"]'
        email_xpath = '//*[@id="Email"]'
        create_user_button_xpath = '//*[@id="submitButton"]'
        
        logon_name_field = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, new_user_login_name_xpath))).send_keys(f"{self.forename.title()} {self.surname.title()}")
        password_field = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, password_xpath))).send_keys(self.user_pwd)
        confirm_password_field = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, password_confirm_xpath ))).send_keys(self.user_pwd)
        firstname_field = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, first_name_xpath ))).send_keys(self.forename.title())
        surename_field = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, surname_field_xpath))).send_keys(self.surname.title())
        email_field = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, email_xpath))).send_keys(self.user_email_address)
        create_user = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, create_user_button_xpath))).click()
        
        driver.quit()
        exit(1)

    def main(self):
        self.epod_sign_in()
        self.create_account()



if __name__ == "__main__":
    run = CREATE_USER(create_user_url, epod_username, epod_password, new_epod_account_email, chrome_options, user_acc_password)
    print(f"Mote de passe: {user_acc_password}")
    run.main()



