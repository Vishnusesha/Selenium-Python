from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome()
driver.get("https://console.harmony.a2z.com/internal-ai-assistant?playground=")

wait = WebDriverWait(driver,5)
wait.until(EC.presence_of_element_located((By.ID,"user_name"))).send_keys("ubsvishn")

wait.until(EC.presence_of_element_located((By.ID,"password"))).send_keys("04052002")

wait.until(EC.element_to_be_clickable((By.ID,"verify_btn"))).click()

time.sleep(5)

wait.until(EC.presence_of_element_located((By.ID,"otp-field"))).send_keys("enecccfefcneinlvbkbugbejunvudhtrcrkivfijbdth")

wait.until(EC.element_to_be_clickable((By.ID,"otp-submit-btn"))).click()

wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/main/div/main/div[1]/div[2]/div/div[1]/div/div[2]/div/div[2]/div/div/div/div[2]/button"))).click()

time.sleep(5)

wait.until(EC.presence_of_element_located((By.ID,"formField:r1s:"))).send_keys("enecccfefcneinlvbkbugbejunvudhtrcrkivfijbdth")

wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id=':r5:']/div[2]/div/div[2]/div/div/div/div[3]/div/div/div[3]/button"))).click()

wait.until(EC.presence_of_element_located((By.NAME,"password"))).send_keys("04052002")

wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id=':r5:']/div[2]/div/div[2]/div/div/div/div[3]/div/div/div[3]/button"))).click()
