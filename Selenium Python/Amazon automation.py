from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://www.amazon.com")
driver.find_element(By.ID,"twotabsearchtextbox").send_keys("echo")
driver.find_element(By.ID,"nav-search-submit-button").click()
driver.find_element(By.CLASS_NAME,"s-image").click()
try:
    driver.find_element(By.ID,"add-to-cart-button").click()
except Exception as e:
    print(f"An error name {type(e).__name__} occured:{e}")

finally:
    print("Successfully Completed")
    time.sleep(5)
    driver.quit()
