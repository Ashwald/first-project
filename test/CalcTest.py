from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://ashwald.github.io/first-project/")

driver.find_element(By.XPATH, "/html/body/form/input[1]").send_keys("1")
driver.find_element(By.XPATH, "/html/body/form/input[2]").send_keys("2")

header_text = driver.find_element(By.XPATH, "//h1").text

print(header_text)
assert header_text == "Calculator"

driver.find_element(By.XPATH, "/html/body/form/input[3]").click()

