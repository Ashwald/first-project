from selenium import webdriver


def go_to_list():
    driver.get("http://localhost:8080/server")


def assert_table_contains_location(name, expected_coords):
    # Use literal string interpolation
    # https://realpython.com/python-string-formatting/
    xpath = "//tr[td[text() = 'name']]/td[2]".replace("name", name)
    coords = driver.find_element_by_xpath(xpath).text
    print("Actual:" + coords)
    print("Expected: " + expected_coords)
    # Doesn't print actual and expected values
    assert coords == expected_coords


def assert_count_of_table_rows_is(expected_count):
    xpath = "//tbody/tr"
    count = len(driver.find_elements_by_xpath(xpath))
    assert count == expected_count


def test_empty_locations():
    go_to_list()
    assert_count_of_table_rows_is(6)
    assert_table_contains_location("alma", "1.0, 2.0")


def click_to_create_location_link():
    driver.find_element_by_link_text("Create location").click()


# Use default values
def fill_create_location_form(name, coordinates):
    driver.find_element_by_id("name-input").send_keys(name)
    driver.find_element_by_id("coords-input").send_keys(coordinates)


def click_to_create_button():
    driver.find_element_by_class_name("btn-primary").click()


def assert_message_has_been_appeared(expected_message):
    message = driver.find_element_by_class_name("alert").text
    assert message == expected_message


def assert_details_are(expected_name, expected_coords):
    name = driver.find_element_by_xpath("//tr[td[1][text() = 'Name']]/td[2]").text
    coords = driver.find_element_by_xpath("//tr[td[1][text() = 'Coordinates']]/td[2]").text
    assert name == expected_name
    assert coords == expected_coords


def assert_field_error_has_been_appeared(expected_message):
    message = driver.find_element_by_class_name("invalid-feedback").text
    assert message == expected_message


def test_create_location():
    go_to_list()
    click_to_create_location_link()
    fill_create_location_form("Budapest", "1,1")
    click_to_create_button()
    assert_message_has_been_appeared("Location has been created.")
    assert_details_are("Budapest", "1.0, 1.0")
    go_to_list()
    assert_table_contains_location("Budapest", "1.0, 1.0")


def test_create_with_invalid_name():
    go_to_list()
    click_to_create_location_link()
    fill_create_location_form("", "1,1")
    click_to_create_button()
    assert_field_error_has_been_appeared("must not be blank")


#chrome_options = webdriver.ChromeOptions()
#chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
#driver = webdriver.Chrome("/home/vicziani/Softwares/chromedriver", options=chrome_options)
driver = webdriver.Chrome()


#test_empty_locations()
#test_create_location()
test_create_with_invalid_name()