from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def is_element_present_by_xpath(xpath):
    elements_found = len(driver.find_elements(By.XPATH, xpath))
    if elements_found > 0:
        return True
    else:
        return False


def assert_title_is(title):
    print("Title: " + driver.title)
    assert driver.title == title
    print("Title is OK.")


def assert_header_is(header):
    header_text = driver.find_element(By.XPATH, "//h2").text
    print("Header: " + header_text)
    assert header_text == header
    print("Header is OK.")


def assert_image_is_present(image):
    xpath = "//img[contains(@src, 'image')]"
    xpath = xpath.replace("image", image)
    print("Searching image " + image)
    assert is_element_present_by_xpath(xpath)
    print("Image OK.")


def test_home_page(title, header, image):
    assert_title_is(title)
    assert_header_is(header)
    assert_image_is_present(image)


def goto_home_page():
    driver.find_element(By.XPATH, "//a[contains(@title, 'home')]").click()


def goto_home_page_via_logo():
    driver.find_element(By.CLASS_NAME, "navbar-brand").click()


def goto_find_owners():
    driver.find_element(By.XPATH, "//a[contains(@title, 'owner')]").click()


def goto_veterinarians():
    driver.find_element(By.XPATH, "//a[contains(@title, 'vet')]").click()


def test_find_owners_page(title, header):
    goto_find_owners()
    label_xpath = "//label[contains(text(), 'Last name')]"
    input_xpath = "//input[@id = 'lastName']"
    assert_title_is(title)
    assert_header_is(header)
    is_element_present_by_xpath(label_xpath)
    is_element_present_by_xpath(input_xpath)


def print_veterinarian_count():
    goto_veterinarians()
    vet_num = len(driver.find_elements(By.XPATH, "//tbody/tr"))
    print(vet_num)


def print_veterinarian_names():
    goto_veterinarians()
    vets = driver.find_elements(By.XPATH, "//tbody/tr/td[1]")
    for vet in vets:
        print(vet.text)


def print_veterinarian_with_speciality(speciality):
    goto_veterinarians()
    xpath = "//span[contains(text(), 'speciality')]/../preceding-sibling::td"
    xpath = xpath.replace("speciality", speciality)
    print("Look for " + xpath)
    vets = driver.find_elements(By.XPATH, xpath)
    for vet in vets:
        print(vet.text)


def print_veterinarian_skill_count():
    goto_veterinarians()
    vet_xpath = "//tr/td[1]"
    vets = driver.find_elements(By.XPATH, vet_xpath)
    spec_xpath_base = "//td[text()='name']/following-sibling::td/*[not(contains(text(), 'none'))]"
    for vet in vets:
        vet_name = vet.text
        spec_xpath = spec_xpath_base.replace("name", vet_name)
        spec_num = len(driver.find_elements(By.XPATH, spec_xpath))
        print(vet_name + " has " + str(spec_num) + " specialities.")


def get_veterinarian_names():
    goto_veterinarians()
    names = []  # Üres lista létrehozása
    vets = driver.find_elements(By.XPATH, "//tbody/tr/td[1]")
    for vet in vets:
        names.append(vet.text)  # Új elem hozzáadása
    return names


def print_veterinarian_name_contains(part):
    names = get_veterinarian_names()
    for name in names:
        if part in name:
            print(name + " contains " + part)


def print_veterinarian_longer_than(number_of_characters):
    names = get_veterinarian_names()
    for name in names:
        if len(name) > number_of_characters:
            print(name + "'s name is longer than " + str(number_of_characters))


def print_longest_name():
    char_len = 0
    names = get_veterinarian_names()
    for name in names:
        if len(name) > char_len:
            char_len = len(name)
    winners = []
    for name in names:
        if len(name) == char_len:
            winners.append(name)
    print("These vets have the longest names of " + str(char_len) + str(winners))


driver = webdriver.Chrome()
driver.get("http://localhost:8081/")


#test_home_page("PetClinic :: a Spring Framework demonstration", "Welcome", "pets.png")
#test_find_owners_page("PetClinic :: a Spring Framework demonstration", "Find Owners")
#print_veterinarian_count()
#print_veterinarian_names()
#print_veterinarian_with_speciality("surgery")
#print_veterinarian_skill_count()
#print("Names list " + str(get_veterinarian_names()))
#print_veterinarian_name_contains("a")
#print_veterinarian_longer_than(11)
#print_longest_name()

driver.close()
