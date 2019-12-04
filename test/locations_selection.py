from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def find_lat_by_name(name):
    xpath = "//td[text()='name']/following-sibling::td"
    xpath = xpath.replace("name", name)
    print(xpath)
    coords = driver.find_element(By.XPATH, xpath).text
    lat = float(coords[0:coords.index(",")])
    return lat


def print_if_lat_greater_than(name, base_lat):
    lat = find_lat_by_name(name)
    if lat > base_lat:
        print("Greater")
    else:
        print("Not greater")


def print_if_lat_between_by_name(name, lower, greater):
    lat = find_lat_by_name(name)
    if lower <= lat <= greater:
        print("Lat between " + str(lower) + " and " + str(greater))
    else:
        print("Lat NOT between " + str(lower) + " and " + str(greater))


driver = webdriver.Chrome()
driver.get("http://www.learnwebservices.com/locations/")
WebDriverWait(driver, 10).until(
    expected_conditions.presence_of_element_located((By.XPATH, "//tbody/tr"))
)
print_if_lat_greater_than("Ajax", 10)
print_if_lat_between_by_name("Ajax", 40, 60)


driver.close()
