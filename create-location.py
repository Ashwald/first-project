from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.learnwebservices.com/locations/server/")
driver.find_element(By.ID, "nameInput").send_keys("Hello Python")

title = driver.find_element(By.XPATH, "//h1").text
print(title)

assert title == "Locations"
# driver.close()