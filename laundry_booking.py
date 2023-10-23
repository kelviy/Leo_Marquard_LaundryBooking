"""
Code adaped from https://www.lambdatest.com/blog/how-to-automate-filling-in-web-forms-with-python-using-selenium/
This program automates the laundry booking process in Vula for Leo Marquard Hall
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

import os
from dotenv import load_dotenv
load_dotenv()
# make sure the imports are working from initial set-up from "https://www.lambdatest.com/blog/how-to-automate-filling-in-web-forms-with-python-using-selenium/"

# add an .env file for your email and password credidentials
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')

#Change your booking slot here:

# floor option - starting from 0 in the list
option_number = 0
# time slot - starting from 0 in the list
sign_up_number = 2


def login():
    login_link = browser.find_element(By.ID, "loginLink1")
    login_link.click()

    username = browser.find_element(By.ID, "userNameInput")
    # your username
    username.send_keys(USERNAME)
    password = browser.find_element(By.ID, "passwordInput")
    # your password
    password.send_keys(PASSWORD)
    submit_button = browser.find_element(By.ID, "submitButton")
    submit_button.click()


# Fixed Error from https://stackoverflow.com/questions/76724939/there-is-no-such-driver-by-url-https-chromedriver-storage-googleapis-com-lates
# service = Service()
# options = webdriver.ChromeOptions()
# browser = webdriver.Chrome(service=service, options=options)

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

browser.get("http://vula.uct.ac.za/portal")

#login process
login()

browser.get("https://vula.uct.ac.za/portal/directtool/f5b131b3-a4de-419c-aa5c-dc8b66a9c5d2/")

option_link = browser.find_element(By.ID, f"items:meetinglist:{option_number}:cmdlink90")
option_link.click()

# Refreashes until the targetted sign-up button pops up
while True:
    try:
        sign_up = browser.find_element(By.ID, f"meeting:timeslots:{sign_up_number}:addMe")
        sign_up.click()

        save = browser.find_element(By.ID, "meeting:save")
        save.click()
        break
    except NoSuchElementException:
        browser.refresh()

time.sleep(10)
browser.quit

