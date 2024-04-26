from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from twilio.rest import Client
import time
from datetime import datetime
import twilio

LOGIN_URL = "LOGIN PAGE"
ACCOUNT = "ACCOUNT"
TWILIO_USER = "TWILIO USER"
PASSWORD = "PASSWORD"
TWILIO_PASS = "TWILIO PASSWORD"

def send_message(client, message):
    message = client.messages \
                .create(
                     body=message,
                     from_='TWILIO PHONE',
                     to='PERSONAL PHONE'
                 )

def main():
    client = Client(TWILIO_USER,TWILIO_PASS)
    options = webdriver.ChromeOptions()
    options.add_argument('--headless=new')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    driver = webdriver.Chrome(options=options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})
    driver.get("LOGIN URL")
    username = driver.find_element("name", "email")
    username.send_keys(ACCOUNT)
    time.sleep(2)
    password = driver.find_element("name", "password")
    password.send_keys(PASSWORD)
    submit_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/form/div[3]/button")
    submit_button.click()
    time.sleep(4)

    while True:
        driver.get("STORE PURCHASE SITE")
        time.sleep(300)
        text_element = driver.page_source
        newsite = text_element
        time.sleep(1)
        if "NOT IN STOCK STRING" in newsite:
            print("not in stock" , datetime.now().strftime('%H:%M:%S'))
        else:
            send_message(client,"Might be in stock" , datetime.now().strftime('%H:%M:%S'))

if __name__ == "__main__":
    main()