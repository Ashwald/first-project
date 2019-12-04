from selenium import webdriver
from selenium.webdriver.common.by import By


def get_coords_by_name(name):
    xpath = "//td[text()='name']/following-sibling::*"
    xpath = xpath.replace("name", name)
    coords = driver.find_element(By.XPATH, xpath).text
    print(coords)
    return coords


def get_name_by_id(id):
    xpath = "//td[text()='id']/following-sibling::*"
    xpath = xpath.replace("id", id)
    name = driver.find_element(By.XPATH, xpath).text
    print(name)
    coords = driver.find_element(By.XPATH, xpath + "[2]").text
    print(coords)
    return name


def add_place(name, lat=47.21283333, lon=16.8435):
    name_element = driver.find_element(By.ID, "nameInput")
    name_element.send_keys(name)
    coords = str(lat) + "," + str(lon)
    coords_element = driver.find_element(By.ID, "coordsInput")
    coords_element.send_keys(coords)
    button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
    button.click()


def modify_place_by_id(id, name, lat, lon):
    button = "//td[text()='id']/following-sibling::a"
    button = button.replace("id", id)
    driver.find_element(By.XPATH, button).click()
    add_place(name, lat, lon)


driver = webdriver.Chrome()
driver.get("http://www.learnwebservices.com/locations/server/")

# get_coords_by_name("Velence")
# get_name_by_id("11502")
# add_place("Gotham", "66.66", "66.66")
modify_place_by_id(11495, "Metropolis", "69", "69")

driver.close()
