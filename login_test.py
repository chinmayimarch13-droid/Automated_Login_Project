from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Open Chrome browser
driver = webdriver.Chrome()

# Open demo login page
driver.get("https://the-internet.herokuapp.com/login")
time.sleep(2)

# --- VALID LOGIN ---
driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
driver.find_element(By.CLASS_NAME, "radius").click()
time.sleep(2)

# Get success message
success_message = driver.find_element(By.ID, "flash").text
print("Valid Login Result:", success_message)

# --- INVALID LOGIN ---
driver.get("https://the-internet.herokuapp.com/login")
time.sleep(2)
driver.find_element(By.ID, "username").send_keys("wronguser")
driver.find_element(By.ID, "password").send_keys("wrongpassword")
driver.find_element(By.CLASS_NAME, "radius").click()
time.sleep(2)

# Get error message
error_message = driver.find_element(By.ID, "flash").text
print("Invalid Login Result:", error_message)

# Close browser
driver.quit()
