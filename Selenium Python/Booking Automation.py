from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()
driver.get("https://www.yatra.com/")
wait = WebDriverWait(driver,10)
time.sleep(10)
wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div/div[1]/div[2]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/p[2]"))).click()
wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div/div[1]/div[2]/div[3]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div/div/input"))).send_keys("Chennai")
time.sleep(5)
wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div/div[1]/div[2]/div[3]/div[2]/div[1]/div[1]/div[1]/div[3]/div[2]/div/div[1]/div/ul/div/li/div"))).click()
time.sleep(3)
wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div/div[1]/div[2]/div[3]/div[2]/div[1]/div[4]/div/button"))).click()
