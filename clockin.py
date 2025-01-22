from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file
TU_USERNAME = os.getenv("TU_USERNAME")
TU_PASSWORD = os.getenv("TU_PASSWORD")

driver = webdriver.Chrome()

driver.get("https://prd-kronos.erp.temple.edu/wfcstatic/applications/navigator/html5/dist/container/index.html?version=8.1.19.335#/")

title = driver.title

time.sleep(5)
driver.implicitly_wait(10)

username = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[1]/form/div[4]/input")
password = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[1]/form/div[5]/input")
submit_button = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[1]/form/div[6]/button")

print("Loggin in to TU Portal")
username.send_keys(TU_USERNAME)
time.sleep(3)
password.send_keys(TU_PASSWORD)
submit_button.click()
time.sleep(3)
driver.implicitly_wait(10)

print("Waiting for duo confirmation")
time.sleep(10)

print("Saying this is my device")
device_button = driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div/div[2]/div[3]/button")
device_button.click()

driver.implicitly_wait(10)


driver.implicitly_wait(10)
record_time_button = driver.find_element(By.XPATH, "/html/body/div[1]/ui-view/krn-timestamp/div[3]/cc-button/button")
record_time_button.click()

# record_time_button = driver.find_element(By.CLASS_NAME, "record")
# print("Recording Time Stamp")
# record_time_button = driver.find_element(By.ID, "jqxWidgeta92b07fb5c78")
# record_time_button.click()

# message = driver.find_element(by=By.ID, value="message")
# text = message.text

driver.implicitly_wait(10)

# driver.quit()
