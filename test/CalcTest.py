from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://ashwald.github.io/first-project/")

first_num = int(input("First Num"))
second_num = int(input("Second Num"))
first_input_field = driver.find_element(By.ID, "a-input")
first_input_field.send_keys(first_num)
first_input_field.screenshot("first-input.png")

driver.find_element(By.ID, "b-input").send_keys(second_num)
driver.find_element(By.ID, "submit-button").click()

header_text = driver.find_element(By.XPATH, "//h1").text
result = int(driver.find_element(By.ID, "result-input").get_attribute("value"))

driver.save_screenshot("result.png")

print(header_text)
assert header_text == "Calculator"
assert result == first_num + second_num


