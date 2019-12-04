import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

name = "John Doe Smith"
name_parts = name.split(" ")
for name in name_parts:
    print(name)

for i in range(1, 6):
    print("Hunor " + str(i))

animals_tuple = ("dog", "cat")
print(animals_tuple[0])

city = ("Florida", 12, True)
print(city)

