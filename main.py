from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_option)

driver.get("https://profile.w3schools.com/log-in?redirect_url=https%3A%2F%2Fmy-learning.w3schools.com")
Email = driver.find_element(By.NAME, value="email")
Email.send_keys(" enter your mail id ")
Password = driver.find_element(By.NAME, value="current-password")
Password.send_keys("enter your password")
submit = driver.find_element(By.CLASS_NAME, "Button_primary__d2Jt3")
submit.click()
