from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.learnwebservices.com/locations/server/")
coords = driver.find_element(By.XPATH, "//td[text()='Velence']/following-sibling::*").text
coords = float(coords)
print(coords)
print("The type of coords is " + str(type(coords)))

driver.close()
