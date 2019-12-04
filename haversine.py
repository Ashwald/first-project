from math import radians, cos, sin, asin, sqrt
from selenium import webdriver
from selenium.webdriver.common.by import By

def haversine(lat1, lon1, lat2, lon2):

      R = 6372.8

      dLat = radians(lat2 - lat1)
      dLon = radians(lon2 - lon1)
      lat1 = radians(lat1)
      lat2 = radians(lat2)

      a = sin(dLat/2)**2 + cos(lat1)*cos(lat2)*sin(dLon/2)**2
      c = 2*asin(sqrt(a))

      return R * c

driver = webdriver.Chrome()
driver.get("http://www.learnwebservices.com/locations/server/")
coords1 = driver.find_element(By.XPATH, "//td[text()='Tiszakerecseny']/following-sibling::*").text
print(coords1)
coords1 = coords1.split(",")
lat1 = float(coords1[0])
print(lat1)
print(type(lat1))
lon1 = float(coords1[1])
print(type(lon1))

coords2 = driver.find_element(By.XPATH, "//td[text()='Tiszarád']/following-sibling::*").text
print(coords2)
coords2 = coords2.split(",")
lon2 = float(coords2[1])
print(type(lon1))
lat2 = float(coords2[0])
print(lat2)
print(type(lat2))

driver.close()

# Usage
print("Distance is " + str(haversine(lat1, lon1, lat2, lon2)))
