from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
wait = WebDriverWait(driver,100)
driver.get("https://www.google.com/webhp?authuser=1")
driver.find_element(By.XPATH,"/html/body/div[2]/div[4]/form/div[1]/div[1]/div[1]/div[1]/div[2]/textarea").send_keys("yahoo")
driver.find_element(By.XPATH,"/html/body/div[2]/div[4]/form/div[1]/div[1]/div[1]/div[1]/div[2]/textarea").submit()
wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT,"Yahoo"))).click()
wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div/div[3]/div[3]/div[2]/div[1]/form/div[1]/input"))).send_keys("oorum blood")
wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div/div[3]/div[3]/div[2]/div[1]/form/div[1]/input"))).submit()
wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT,"YouTube"))).click()

windows = driver.window_handles
driver.switch_to.window(windows[-1])


wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"ytp-play-button"))).click()
