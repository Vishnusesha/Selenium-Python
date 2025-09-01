from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome()
driver.get("https://www.facebook.com")
wait = WebDriverWait(driver,30)
wait.until(EC.presence_of_element_located((By.NAME,"email"))).send_keys("9791945425")
wait.until(EC.presence_of_element_located((By.NAME,"pass"))).send_keys("926247383221")
wait.until(EC.element_to_be_clickable((By.NAME,"login"))).click()
time.sleep(20)
try:
    wait.until(EC.element_to_be_clickable((By.XPATH,"//div[starts-with(@class,'x78zum5') and starts-with(@class,'x1uvtmcs')] and //label[starts-with(@class,'x1a2a7pz')]"))).click()
except Exception as e:
    print(f"Exception {e}")

#wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div/div[1]/div/div[2]/div[5]/div[1]/div[2]/span/span/div/div[1]"))).click()
#wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/a/div[1]/div/svg/g/image"))).click()
#driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[2]/div[5]/div[1]/span/div/div[1]/div/svg/g/image").click()

#/html/body/div[1]/div/div[1]/div/div[2]/div[5]/div[1]/span/div/div[1]/div/div[1]
